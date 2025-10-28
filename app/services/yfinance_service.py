import yfinance as yf
from typing import Dict, Any, List
import pandas as pd

class YFinanceService:
    
    @staticmethod
    def get_ticker_info(symbol: str) -> Dict[str, Any]:
        ticker = yf.Ticker(symbol)
        info = ticker.info
        if not info or len(info) == 0:
            raise ValueError(f"Symbol {symbol} not found or no data available")
        return info
    
    @staticmethod
    def get_fast_info(symbol: str) -> Dict[str, Any]:
        ticker = yf.Ticker(symbol)
        fast_info = ticker.fast_info
        
        try:
            return {
                "currency": getattr(fast_info, 'currency', None),
                "dayHigh": getattr(fast_info, 'dayHigh', None),
                "dayLow": getattr(fast_info, 'dayLow', None),
                "exchange": getattr(fast_info, 'exchange', None),
                "fiftyDayAverage": getattr(fast_info, 'fiftyDayAverage', None),
                "lastPrice": getattr(fast_info, 'lastPrice', None),
                "lastVolume": getattr(fast_info, 'lastVolume', None),
                "marketCap": getattr(fast_info, 'marketCap', None),
                "open": getattr(fast_info, 'open', None),
                "previousClose": getattr(fast_info, 'previousClose', None),
                "quoteType": getattr(fast_info, 'quoteType', None),
                "regularMarketPreviousClose": getattr(fast_info, 'regularMarketPreviousClose', None),
                "shares": getattr(fast_info, 'shares', None),
                "tenDayAverageVolume": getattr(fast_info, 'tenDayAverageVolume', None),
                "threeMonthAverageVolume": getattr(fast_info, 'threeMonthAverageVolume', None),
                "timezone": getattr(fast_info, 'timezone', None),
                "twoHundredDayAverage": getattr(fast_info, 'twoHundredDayAverage', None),
                "yearChange": getattr(fast_info, 'yearChange', None),
                "yearHigh": getattr(fast_info, 'yearHigh', None),
                "yearLow": getattr(fast_info, 'yearLow', None)
            }
        except Exception:
            raise ValueError(f"Unable to get fast info for symbol {symbol}")
    
    @staticmethod
    def get_history(symbol: str, period: str = "1y", interval: str = "1d") -> Dict:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period=period, interval=interval)
        if data.empty:
            raise ValueError(f"No historical data found for symbol {symbol}")
        return data.to_dict('index')
    
    @staticmethod
    def get_recommendations(symbol: str) -> List[Dict]:
        ticker = yf.Ticker(symbol)
        recommendations = ticker.recommendations
        return recommendations.to_dict('records') if not recommendations.empty else []
    
    @staticmethod
    def get_news(symbol: str) -> List[Dict]:
        ticker = yf.Ticker(symbol)
        news = ticker.news
        return news if news else []
    
    @staticmethod
    def get_earnings(symbol: str) -> Dict:
        ticker = yf.Ticker(symbol)
        earnings = ticker.earnings
        return earnings.to_dict('index') if not earnings.empty else {}
    
    @staticmethod
    def get_financials(symbol: str) -> Dict:
        ticker = yf.Ticker(symbol)
        financials = ticker.financials
        return financials.to_dict('index') if not financials.empty else {}
    
    @staticmethod
    def get_balance_sheet(symbol: str) -> Dict:
        ticker = yf.Ticker(symbol)
        balance_sheet = ticker.balance_sheet
        return balance_sheet.to_dict('index') if not balance_sheet.empty else {}
    
    @staticmethod
    def get_cashflow(symbol: str) -> Dict:
        ticker = yf.Ticker(symbol)
        cashflow = ticker.cashflow
        return cashflow.to_dict('index') if not cashflow.empty else {}
    
    @staticmethod
    def get_dividends(symbol: str) -> Dict:
        ticker = yf.Ticker(symbol)
        dividends = ticker.dividends
        return dividends.to_dict() if not dividends.empty else {}
    
    @staticmethod
    def get_splits(symbol: str) -> Dict:
        ticker = yf.Ticker(symbol)
        splits = ticker.splits
        return splits.to_dict() if not splits.empty else {}
    
    @staticmethod
    def get_actions(symbol: str) -> Dict:
        ticker = yf.Ticker(symbol)
        actions = ticker.actions
        return actions.to_dict('index') if not actions.empty else {}
    
    @staticmethod
    def download_data(symbols: List[str], period: str = "1y") -> Dict:
        data = yf.download(symbols, period=period)
        if data.empty:
            raise ValueError(f"No data found for symbols: {', '.join(symbols)}")
        return data.to_dict('index')
    
    @staticmethod
    def search_tickers(query: str) -> List[Dict]:
        try:
            from yfinance.search import Search
            search = Search()
            return search.query(query)
        except Exception:
            return []