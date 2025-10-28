from fastapi import APIRouter, HTTPException
from app.schemas.requests import TickerRequest, HistoryRequest
from app.services.yfinance_service import YFinanceService

router = APIRouter(prefix="/ticker", tags=["ticker"])

@router.post("/info")
async def get_ticker_info(request: TickerRequest):
    try:
        return YFinanceService.get_ticker_info(request.symbol)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.post("/fast-info")
async def get_fast_info(request: TickerRequest):
    try:
        return YFinanceService.get_fast_info(request.symbol)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.post("/history")
async def get_history(request: HistoryRequest):
    try:
        return YFinanceService.get_history(
            request.symbol, 
            request.period or "1y", 
            request.interval or "1d"
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.post("/recommendations")
async def get_recommendations(request: TickerRequest):
    try:
        return YFinanceService.get_recommendations(request.symbol)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.post("/news")
async def get_news(request: TickerRequest):
    try:
        return YFinanceService.get_news(request.symbol)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.post("/earnings")
async def get_earnings(request: TickerRequest):
    try:
        return YFinanceService.get_earnings(request.symbol)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.post("/financials")
async def get_financials(request: TickerRequest):
    try:
        return YFinanceService.get_financials(request.symbol)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.post("/balance-sheet")
async def get_balance_sheet(request: TickerRequest):
    try:
        return YFinanceService.get_balance_sheet(request.symbol)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.post("/cashflow")
async def get_cashflow(request: TickerRequest):
    try:
        return YFinanceService.get_cashflow(request.symbol)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.post("/dividends")
async def get_dividends(request: TickerRequest):
    try:
        return YFinanceService.get_dividends(request.symbol)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.post("/splits")
async def get_splits(request: TickerRequest):
    try:
        return YFinanceService.get_splits(request.symbol)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.post("/actions")
async def get_actions(request: TickerRequest):
    try:
        return YFinanceService.get_actions(request.symbol)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")