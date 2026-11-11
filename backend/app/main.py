from fastapi import FastAPI
from app.api.tenders import router as tenders_router

app = FastAPI()


@app.get("/api/v1/health")
def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "bidflow-api"
    }


app.include_router(tenders_router)
