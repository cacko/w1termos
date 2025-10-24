from pydantic import BaseModel
from pydantic_settings import BaseSettings

class W1TermosSettings(BaseModel):
    host: str = '0.0.0.0'
    port: int = 44532
    log_level: str = 'INFO'

class Settings(BaseSettings):
    w1termos: W1TermosSettings

    class Config:
        env_nested_delimiter = "__"


app_config = Settings()  # type: ignore