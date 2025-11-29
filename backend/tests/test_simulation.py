from app.services.buy_vs_rent import (
    SimulationParams, run_single_scenario, run_analysis_dict
)


def test_cuota_mensual_zero_interest():
    """Test scenario with zero interest rate."""
    params = SimulationParams(
        precio=100000,
        entrada_pct=0.5,
        gastos_compra_pct=0.0,
        plazo_anos=10,
        tasa_interes_anual=0.0,
        gastos_anuales=0.0,
        alquiler_mensual=None,
        rentabilidad_inversion_anual=0.05,
        revalorizacion_anual=0.0,
        periodo_anos=10,
        vacancia_pct=0.0,
    )
    res = run_single_scenario(params)
    # entrada 50k -> hipoteca 50k amortizada en 10 años sin interés -> capital_pagado ~= 50000
    assert abs(res['capital_pagado'] - 50000) < 1


def test_run_analysis_dict_consistency():
    """Test that run_analysis_dict returns all three scenarios."""
    sample_input = {
        'precio': 200000,
        'entrada_pct': 0.2,
        'gastos_compra_pct': 0.08,
        'plazo_anos': 25,
        'tasa_interes_anual': 0.03,
        'gastos_anuales': 2400.0,
        'alquiler_mensual': 800.0,
        'rentabilidad_inversion_anual': 0.05,
        'revalorizacion_anual': 0.03,
        'periodo_anos': 20,
        'vacancia_pct': 0.05,
    }
    res = run_analysis_dict(sample_input)
    assert 'buy' in res and 'rent' in res and 'buy_to_rent' in res
    assert isinstance(res['buy']['vf_inmueble'], float)
    assert isinstance(res['rent']['vf_inversion'], float)
