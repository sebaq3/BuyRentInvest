"""Input schema for financial analysis."""

from pydantic import BaseModel, Field
from typing import Optional


class AnalysisInput(BaseModel):
    """Schema for buy vs. rent analysis input."""
    precio: float = Field(..., gt=0, description="Precio del inmueble")
    entrada_pct: float = Field(0.2, ge=0.0, le=1.0, description="Porcentaje de entrada (20% por defecto)")
    gastos_compra_pct: float = Field(0.08, ge=0.0, le=1.0, description="Gastos de compra como % del precio (8% por defecto)")
    plazo_anos: int = Field(25, gt=0, description="Plazo de hipoteca en años")
    tasa_interes_anual: float = Field(0.03, ge=0.0, description="Tasa de interés anual (3% por defecto)")
    gastos_anuales: float = Field(2400.0, ge=0.0, description="Gastos anuales (mantenimiento, impuestos, etc.)")
    alquiler_mensual: Optional[float] = Field(None, ge=0.0, description="Alquiler mensual (si aplica)")
    rentabilidad_inversion_anual: float = Field(0.05, ge=-1.0, description="Rentabilidad esperada de inversión anual (5% por defecto)")
    revalorizacion_anual: float = Field(0.03, description="Revalorización anual del inmueble (3% por defecto)")
    periodo_anos: int = Field(20, gt=0, description="Período de análisis en años")
    vacancia_pct: float = Field(0.05, ge=0.0, le=1.0, description="Porcentaje de vacancia (5% por defecto)")
