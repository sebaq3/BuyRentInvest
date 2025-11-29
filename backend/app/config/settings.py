"""Configuration and settings."""

from functools import lru_cache
from typing import NamedTuple


class Settings(NamedTuple):
    """Application settings with sensible defaults."""
    env: str = "development"
    default_period_years: int = 20
    default_rentability: float = 0.05
    default_revalorization: float = 0.03


@lru_cache()
def get_settings() -> Settings:
    """Get application settings (cached singleton)."""
    return Settings()
