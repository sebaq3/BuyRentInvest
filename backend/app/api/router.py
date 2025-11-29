from fastapi import APIRouter
from app.schemas.input_schema import AnalysisInput
from app.schemas.output_schema import AnalysisResult
from app.services.buy_vs_rent import run_analysis_dict
from app.config.settings import get_settings

router = APIRouter()


@router.post("/analyze", response_model=AnalysisResult)
def analyze(input_data: AnalysisInput):
    """FastAPI endpoint to run the financial analysis."""
    config = get_settings()
    result = run_analysis_dict(input_data.model_dump(), config=config)
    return result
