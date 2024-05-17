from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_user: str
    db_password: str
    db_server: str
    db_port: int
    db_name: str
    db_protocol: str = "postgresql+asyncpg"
    root_path: str = ""
    log_level: str = "INFO"
    project_name: str = "Songs API"
    project_version: str = "0.1.0"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
