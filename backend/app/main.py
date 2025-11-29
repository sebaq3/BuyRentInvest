from fastapi import FastAPI
from app.api.router import router
import logging


def create_app() -> FastAPI:
    app = FastAPI(title="BuyRentInvest API")
    # logging básico — en producción usar structlog o configuración más completa
    logging.basicConfig(level=logging.INFO)
    app.include_router(router, prefix="/api/v1")
    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
