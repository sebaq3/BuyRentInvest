from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_analyze_api():
    """Test the /api/v1/analyze endpoint."""
    payload = {
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
    resp = client.post("/api/v1/analyze", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert "buy" in data
    assert "rent" in data
    assert "buy_to_rent" in data
    assert isinstance(data["buy"]["vf_inmueble"], float)
    assert isinstance(data["rent"]["vf_inversion"], float)
