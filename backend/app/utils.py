from math import pow
from typing import Union

def cuota_mensual(monto: float, tasa_anual: float, plazo_anos: int) -> float:
    """
    Amortización francesa (cuota fija).
    Fórmula: C = P * r * (1+r)^n / ((1+r)^n - 1)
    Donde r = tasa periódica (mensual) y n = número de períodos (meses).
    """
    if monto <= 0 or plazo_anos <= 0:
        return 0.0
    r = tasa_anual / 12.0
    n = plazo_anos * 12
    if r == 0:
        return monto / n
    return monto * r * pow(1 + r, n) / (pow(1 + r, n) - 1)


def valor_futuro(precio: float, tasa: float, años: int) -> float:
    """Capitalización compuesta simple: VF = PV * (1 + i)^t"""
    return precio * pow(1 + tasa, años)
