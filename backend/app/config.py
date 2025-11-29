from typing import NamedTuple


class Config(NamedTuple):
default_period_years: int = 20
default_rentability: float = 0.05
default_revalorization: float = 0.03


# instancia por defecto que puede ser sobrescrita en tests
default_config = Config()