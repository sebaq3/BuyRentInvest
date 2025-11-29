from typing import Dict
from dataclasses import dataclass
from app.utils import cuota_mensual, valor_futuro

@dataclass(frozen=True)
class SimulationParams:
    precio: float
    entrada_pct: float
    gastos_compra_pct: float
    plazo_anos: int
    tasa_interes_anual: float
    gastos_anuales: float
    alquiler_mensual: float | None
    rentabilidad_inversion_anual: float
    revalorizacion_anual: float
    periodo_anos: int
    vacancia_pct: float

def run_single_scenario(params: SimulationParams) -> Dict[str, float]:
    """
    Calcula métricas clave para un escenario determinista:
    - vf_inmueble: valor futuro del inmueble
    - deuda_final: deuda pendiente al final del periodo
    - capital_pagado: suma de capital amortizado
    - cashflow_acumulado: flujo neto total (ingresos menos pagos)
    - capital_total: suma de patrimonio final (entrada + capital_pagado + (VF - deuda) + cashflow)
    """
    precio = params.precio
    entrada = precio * params.entrada_pct
    gastos_compra = precio * params.gastos_compra_pct
    monto_hipoteca = max(0.0, precio - entrada)

    cuota = cuota_mensual(monto_hipoteca, params.tasa_interes_anual, params.plazo_anos)

    n_meses = params.periodo_anos * 12
    deuda = monto_hipoteca
    capital_pagado = 0.0
    cashflow_acumulado = 0.0

    for _ in range(n_meses):
        if deuda <= 0:
            interes_mes = 0.0
            amortizacion = 0.0
        else:
            interes_mes = deuda * (params.tasa_interes_anual / 12.0)
            amortizacion = cuota - interes_mes
            amortizacion = max(0.0, amortizacion)
            deuda -= amortizacion
            capital_pagado += amortizacion

        gastos_mes = params.gastos_anuales / 12.0
        alquiler_mes = 0.0
        if params.alquiler_mensual:
            alquiler_mes = params.alquiler_mensual * (1 - params.vacancia_pct)

        cashflow_acumulado += (alquiler_mes - cuota - gastos_mes)

    vf_inmueble = valor_futuro(precio, params.revalorizacion_anual, params.periodo_anos)
    deuda_final = max(0.0, deuda)

    capital_total = entrada + capital_pagado + (vf_inmueble - deuda_final) + cashflow_acumulado

    return {
        'vf_inmueble': round(vf_inmueble, 2),
        'deuda_final': round(deuda_final, 2),
        'capital_pagado': round(capital_pagado, 2),
        'cashflow_acumulado': round(cashflow_acumulado, 2),
        'capital_total': round(capital_total, 2),
    }

def run_analysis_dict(inp: Dict, config=None) -> Dict:
    """
    Adaptador para recibir dicts (p.ej. del API) y devolver el resultado
    de los 3 escenarios principales.
    """
    params = SimulationParams(
        precio=inp['precio'],
        entrada_pct=inp.get('entrada_pct', 0.2),
        gastos_compra_pct=inp.get('gastos_compra_pct', 0.08),
        plazo_anos=int(inp.get('plazo_anos', 25)),
        tasa_interes_anual=float(inp.get('tasa_interes_anual', 0.03)),
        gastos_anuales=float(inp.get('gastos_anuales', 2400.0)),
        alquiler_mensual=inp.get('alquiler_mensual'),
        rentabilidad_inversion_anual=float(inp.get('rentabilidad_inversion_anual', 0.05)),
        revalorizacion_anual=float(inp.get('revalorizacion_anual', 0.03)),
        periodo_anos=int(inp.get('periodo_anos', 20)),
        vacancia_pct=float(inp.get('vacancia_pct', 0.05)),
    )

    # 1) Comprar y vivir (sin ingresos por alquiler)
    buy_params = SimulationParams(**{**params.__dict__, 'alquiler_mensual': None})
    buy = run_single_scenario(buy_params)

    # 2) Alquilar e invertir entrada
    entrada = params.precio * params.entrada_pct
    gastos_compra = params.precio * params.gastos_compra_pct
    capital_inicial = entrada + gastos_compra
    r = params.rentabilidad_inversion_anual
    periodo = params.periodo_anos
    vf_inversion = round(capital_inicial * ((1 + r) ** periodo), 2)
    cashflow_alquilar = round(- (params.alquiler_mensual or 0.0) * 12 * periodo, 2)
    rent = {
        'vf_inversion': vf_inversion,
        'cashflow_acumulado': cashflow_alquilar,
        'capital_total': round(vf_inversion + cashflow_alquilar, 2),
    }

    # 3) Comprar y alquilar (puede incluir vacancia)
    buy_to_rent_params = SimulationParams(**{**params.__dict__})
    buy_to_rent = run_single_scenario(buy_to_rent_params)

    return {
        'buy': buy,
        'rent': rent,
        'buy_to_rent': buy_to_rent,
    }
