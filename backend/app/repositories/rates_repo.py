from typing import Protocol, List, Dict


class RatesRepo(Protocol):
    def get_rates(self) -> List[Dict]:
        ...


class InMemoryRatesRepo:
    """Simple in-memory implementation useful for tests."""

    def __init__(self) -> None:
        self._rates = [{"name": "default", "value": 3.5}]

    def get_rates(self) -> List[Dict]:
        return self._rates
