
from fastapi import FastAPI

app = FastAPI(
    title="SureBet API",
    description="API para obtener cuotas y calcular oportunidades de arbitraje.",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "SureBet API funcionando",
        "status": "ok",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }
