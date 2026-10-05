"""Model clients. Each returns the raw JSON text, so every call can be logged verbatim and
replayed later without an API key; validation happens one layer up, in agents.py."""

import os
from collections import deque
from dataclasses import dataclass
from typing import Protocol

from pydantic import BaseModel

MAX_TOKENS = 8000
DEFAULT_MODELS = {"anthropic": "claude-haiku-4-5-20251001", "openai": "gpt-4o-mini"}
# USD per million input/output tokens, from each provider's pricing page (Oct 2026).
PRICES = {"claude-haiku-4-5": (1.0, 5.0), "gpt-4o-mini": (0.15, 0.60)}
KEYS = {"openai": "OPENAI_API_KEY", "anthropic": "ANTHROPIC_API_KEY"}  # in order of preference


@dataclass
class Completion:
    raw: str
    input_tokens: int
    output_tokens: int
    model: str


class LLM(Protocol):
    model: str

    def complete(self, system: str, messages: list[dict], schema: type[BaseModel]) -> Completion: ...


class AnthropicLLM:
    def __init__(self, model: str | None = None, client=None):
        import anthropic

        self.model = model or DEFAULT_MODELS["anthropic"]
        self._schema = anthropic.transform_schema
        self.client = client or anthropic.Anthropic(max_retries=4)

    def complete(self, system: str, messages: list[dict], schema: type[BaseModel]) -> Completion:
        r = self.client.messages.create(
            model=self.model, max_tokens=MAX_TOKENS, system=system, messages=messages,
            output_config={"format": {"type": "json_schema", "schema": self._schema(schema)}},
        )
        if r.stop_reason in ("refusal", "max_tokens"):
            raise RuntimeError(f"{self.model} stopped with {r.stop_reason!r} before finishing the JSON")
        text = "".join(block.text for block in r.content if block.type == "text")
        return Completion(text, r.usage.input_tokens, r.usage.output_tokens, self.model)


class OpenAILLM:
    def __init__(self, model: str | None = None, client=None):
        import openai

        self.model = model or DEFAULT_MODELS["openai"]
        self.client = client or openai.OpenAI(max_retries=4)

    def complete(self, system: str, messages: list[dict], schema: type[BaseModel]) -> Completion:
        r = self.client.chat.completions.parse(
            model=self.model, messages=[{"role": "system", "content": system}, *messages], response_format=schema,
        )
        message = r.choices[0].message
        if message.refusal:
            raise RuntimeError(f"{self.model} refused: {message.refusal}")
        return Completion(message.content, r.usage.prompt_tokens, r.usage.completion_tokens, self.model)


class ScriptedLLM:
    """Plays back outputs in order: raw JSON strings (tests) or recorded llm events (`--replay`)."""

    def __init__(self, outputs: list[str | dict], model: str = "scripted"):
        self.outputs = deque(outputs)
        self.model = next((o["model"] for o in outputs if isinstance(o, dict)), model)

    def complete(self, system: str, messages: list[dict], schema: type[BaseModel]) -> Completion:
        if not self.outputs:
            raise RuntimeError("Scripted outputs exhausted: the replay diverged from the recorded run.")
        out = self.outputs.popleft()
        if isinstance(out, str):
            return Completion(out, 0, 0, self.model)
        return Completion(out["raw"], out["input_tokens"], out["output_tokens"], out["model"])


def make_llm(provider: str, model: str | None = None) -> LLM:
    if provider == "anthropic":
        return AnthropicLLM(model)
    if provider == "openai":
        return OpenAILLM(model)
    raise ValueError(f"Unknown provider {provider!r}; use anthropic or openai.")


def cost(model: str, input_tokens: int, output_tokens: int) -> float | None:
    price = next((p for prefix, p in PRICES.items() if model.startswith(prefix)), None)
    return round((input_tokens * price[0] + output_tokens * price[1]) / 1e6, 4) if price else None


def load_env(path) -> None:
    """Read KEY=VALUE lines from a .env file into the environment, without overriding real variables."""
    if path.exists():
        for line in path.read_text().splitlines():
            key, sep, value = line.strip().partition("=")
            if sep and key and not key.startswith("#"):
                os.environ.setdefault(key.strip(), value.strip().strip("'\""))


def default_provider() -> str | None:
    """OpenAI if its key is set (every recorded run used it), otherwise Anthropic if its key is set."""
    return next((p for p, key in KEYS.items() if os.environ.get(key)), None)


def has_key(provider: str) -> bool:
    return bool(os.environ.get(KEYS[provider]))
