"""Configuration schema using Pydantic."""

from pydantic import BaseModel, ConfigDict, Field
from pydantic_settings import BaseSettings

from pydantic.alias_generators import to_camel


class Base(BaseModel):
    """Base model that accepts both camelCase and snake_case keys."""
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class AgentsConfig(Base):
    """Agent configuration."""
    provider: str = None


class ProviderConfig(Base):
    """LLM provider configuration."""
    api_key: str = ""
    api_base: str | None = None


class ProvidersConfig(Base):
    """Configuration for LLM providers."""
    deepseek: ProviderConfig = Field(default_factory=ProviderConfig)
    openai: ProviderConfig = Field(default_factory=ProviderConfig)


class Config(BaseSettings):
    agents: AgentsConfig = Field(default_factory=AgentsConfig)
    providers: ProvidersConfig = Field(default_factory=ProvidersConfig)

    model_config = ConfigDict()


