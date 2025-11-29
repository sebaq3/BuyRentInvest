from app.services.montecarlo import montecarlo_simulate
from app.services.simulation import SimulationParams
import numpy as np

def test_montecarlo_reproducible():
    base = SimulationParams(
        precio=200000,
        entrada_pct=0.2,
        gastos_compra_pct=0.08,
        plazo_anos=25,
        tasa_interes_anual=0.03,
        gastos_anuales=2400.0,
        alquiler_mensual=800.0,
        rentabilidad_inversion_anual=0.05,
        revalorizacion_anual=0.03,
        periodo_anos=20,
        vacancia_pct=0.05,
    )
    rng1 = np.random.default_rng(42)
    rng2 = np.random.default_rng(42)
    a = montecarlo_simulate(base, 1000, rng1)
    b = montecarlo_simulate(base, 1000, rng2)
    assert a['median'] == b['median']
