from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
	POSTGRES: PostgresDsn = 'postgresql://postgres:postgres@db:5432/postgres'


settings = Settings()
