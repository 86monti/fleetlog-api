from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    project_name: str = "FleetLog API"
    version: str = "0.1.0"
    debug: bool = True

    database_url: str = "postgresql://fleetlog_user:fleetlog_password@localhost:5432/fleetlog_db"

    secret_key: str = "change_this_to_a_long_random_secret_key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


settings = Settings()