import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    """Fixture for FastAPI TestClient."""
    return TestClient(app)


@pytest.fixture
def sample_input():
    """Fixture for a sample analysis input."""
    return {
        "precio": 200000,
        "entrada_pct": 0.2,
        "gastos_compra_pct": 0.08,
        "plazo_anos": 25,
        "tasa_interes_anual": 0.03,
        "gastos_anuales": 2400.0,
        "alquiler_mensual": 800.0,
        "rentabilidad_inversion_anual": 0.05,
        "revalorizacion_anual": 0.03,
        "periodo_anos": 20,
        "vacancia_pct": 0.05,
    }