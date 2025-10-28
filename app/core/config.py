from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "YFinance Microservice"
    version: str = "1.0.0"
    host: str = "0.0.0.0"
    port: int = 8000
    
    class Config:
        env_file = ".env"

settings = Settings()