from pydantic import BaseModel, Field
from typing import Optional

class AnalysisInput(BaseModel):
    precio: float = Field(..., gt=0)
    entrada_pct: float = Field(0.2, ge=0.0, le=1.0)
    gastos_compra_pct: float = Field(0.08, ge=0.0, le=1.0)
    plazo_anos: int = Field(25, gt=0)
    tasa_interes_anual: float = Field(0.03, ge=0.0)
    gastos_anuales: float = Field(2400.0, ge=0.0)
    alquiler_mensual: Optional[float] = Field(None, ge=0.0)
    rentabilidad_inversion_anual: float = Field(0.05, ge=-1.0)
    revalorizacion_anual: float = Field(0.03)
    periodo_anos: int = Field(20, gt=0)
    vacancia_pct: float = Field(0.05, ge=0.0, le=1.0)

class SimpleResult(BaseModel):
    vf_inmueble: float
    deuda_final: float
    capital_pagado: float
    cashflow_acumulado: float
    capital_total: float

class RentResult(BaseModel):
    vf_inversion: float
    cashflow_acumulado: float
    capital_total: float

class AnalysisResult(BaseModel):
    buy: SimpleResult
    rent: RentResult
    buy_to_rent: SimpleResult
