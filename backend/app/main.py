from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from app.api.tenders import router as tenders_router
from app.core.exceptions import TenderNotFoundError, TenderConflictError

app = FastAPI()


@app.get("/api/v1/health")
def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "bidflow-api"
    }


@app.exception_handler(TenderNotFoundError)
async def tender_not_found_handler(
    request: Request,
    exc: TenderNotFoundError,
) -> JSONResponse:
    return JSONResponse(
        status_code=404,
        content={"detail": "Tender not found"},
    )


@app.exception_handler(TenderConflictError)
async def tender_conflict_handler(
    request: Request,
    exc: TenderConflictError,
) -> JSONResponse:
    return JSONResponse(
        status_code=409,
        content={"detail": "Tender conflict"},
    )


app.include_router(tenders_router)
