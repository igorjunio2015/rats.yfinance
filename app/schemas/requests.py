from pydantic import BaseModel
from typing import Optional, List

class TickerRequest(BaseModel):
    symbol: str

class HistoryRequest(BaseModel):
    symbol: str
    period: Optional[str] = "1y"
    interval: Optional[str] = "1d"

class MultiTickerRequest(BaseModel):
    symbols: List[str]
    period: Optional[str] = "1y"