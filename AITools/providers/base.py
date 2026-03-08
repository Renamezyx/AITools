from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


@dataclass
class ToolCallRequest:
    """A tool call request from the LLM."""
    id: str
    name: str
    arguments: dict[str, Any]


@dataclass
class LLMResponse:
    content: str | None
    tools_call: list[dict] = field(default_factory=list)

    @property
    def has_tool_calls(self) -> bool:
        return len(self.tools_call) > 0


class LLMProvider(ABC):
    """
    LLM 抽象基类
    """

    def __init__(self, api_key: str | None = None, api_base: str | None = None):
        self.api_key = api_key
        self.api_base = api_base

    @abstractmethod
    async def chat(self,
                   message: str | None = None,
                   tools: list[dict] | None = None,
                   ) -> LLMResponse:
        pass
