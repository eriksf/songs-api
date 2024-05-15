from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_user: str
    db_password: str
    db_server: str
    db_port: int
    db_name: str
    db_protocol: str = "postgresql+asyncpg"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
