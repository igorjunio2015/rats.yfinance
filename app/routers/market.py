from fastapi import APIRouter, HTTPException
from app.schemas.requests import MultiTickerRequest
from app.services.yfinance_service import YFinanceService

router = APIRouter(prefix="/market", tags=["market"])

@router.post("/download")
async def download_data(request: MultiTickerRequest):
    try:
        return YFinanceService.download_data(
            request.symbols, 
            request.period or "1y"
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/search/{query}")
async def search_tickers(query: str):
    try:
        return YFinanceService.search_tickers(query)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))