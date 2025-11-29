from typing import Dict, List
import numpy as np
from app.services.simulation import SimulationParams, run_single_scenario

def montecarlo_simulate(base_params: SimulationParams, n: int, rng: np.random.Generator) -> Dict[str, object]:
    """
    Ejecuta simulaciones Monte Carlo variando revalorización, rentabilidad y vacancia.
    Devuelve estadísticas y la lista de resultados crudos.
    """
    results: List[float] = []

    # desviaciones por defecto (se pueden parametrizar)
    reval_sd = 0.01
    rent_sd = 0.08
    vacancia_sd = 0.03

    for _ in range(n):
        reval = rng.normal(loc=base_params.revalorizacion_anual, scale=reval_sd)
        rent = rng.normal(loc=base_params.rentabilidad_inversion_anual, scale=rent_sd)
        vac = rng.normal(loc=base_params.vacancia_pct, scale=vacancia_sd)

        # Boundear en rangos razonables
        reval = max(-0.2, min(0.5, reval))
        rent = max(-1.0, min(1.0, rent))
        vac = min(max(0.0, vac), 0.9)

        simp = SimulationParams(
            precio=base_params.precio,
            entrada_pct=base_params.entrada_pct,
            gastos_compra_pct=base_params.gastos_compra_pct,
            plazo_anos=base_params.plazo_anos,
            tasa_interes_anual=base_params.tasa_interes_anual,
            gastos_anuales=base_params.gastos_anuales,
            alquiler_mensual=base_params.alquiler_mensual,
            rentabilidad_inversion_anual=rent,
            revalorizacion_anual=reval,
            periodo_anos=base_params.periodo_anos,
            vacancia_pct=vac,
        )
        out = run_single_scenario(simp)
        results.append(out['capital_total'])

    arr = np.array(results)
    return {
        'n': n,
        'mean': float(arr.mean()),
        'median': float(np.median(arr)),
        'p10': float(np.percentile(arr, 10)),
        'p50': float(np.percentile(arr, 50)),
        'p90': float(np.percentile(arr, 90)),
        'raw': results,
    }
