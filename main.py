from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from app.core.config import settings
from app.routers import ticker, market

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    description="Microserviço performático para dados financeiros usando yfinance"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Redireciona para a documentação Swagger"""
    return RedirectResponse(url="/docs")

@app.get("/health", tags=["Health"])
async def health():
    """Endpoint para verificar a saúde do serviço"""
    return {"status": "ok", "service": "finance-api", "version": settings.version}

app.include_router(ticker.router)
app.include_router(market.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.host, port=settings.port)