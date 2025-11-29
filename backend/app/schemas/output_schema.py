"""Output schemas for financial analysis results."""

from pydantic import BaseModel


class SimpleResult(BaseModel):
    """Result schema for simple scenarios (buy or buy & rent)."""
    vf_inmueble: float
    deuda_final: float
    capital_pagado: float
    cashflow_acumulado: float
    capital_total: float


class RentResult(BaseModel):
    """Result schema for renting scenario."""
    vf_inversion: float
    cashflow_acumulado: float
    capital_total: float


class AnalysisResult(BaseModel):
    """Complete analysis result with buy, rent, and buy_to_rent scenarios."""
    buy: SimpleResult
    rent: RentResult
    buy_to_rent: SimpleResult
