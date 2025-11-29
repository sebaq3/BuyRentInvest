from typing import Tuple

def irpf_alquiler(renta_anual_bruta: float, reduccion_pct: float = 0.6, tipo_marginal: float = 0.19) -> float:
    """
    Estimación simplificada de IRPF sobre ingresos por alquiler.
    - reduccion_pct: porcentaje de reducciones/deducciones aplicadas a la renta bruta.
    - tipo_marginal: tipo efectivo aplicado (simplificado).
    """
    base_imponible = max(0.0, renta_anual_bruta * (1 - reduccion_pct))
    impuesto = base_imponible * tipo_marginal
    return round(impuesto, 2)

def plusvalia_venta(precio_compra: float, precio_venta: float) -> float:
    """
    Estimación simplificada de impuesto sobre ganancia patrimonial (19%).
    En producción habría que aplicar tramos, exenciones y normativa municipal.
    """
    ganancia = max(0.0, precio_venta - precio_compra)
    tasa = 0.19
    return round(ganancia * tasa, 2)
