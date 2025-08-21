from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv


load_dotenv()


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    SECRET_KEY: str

    PAYPAL_CLIENT_ID: str
    PAYPAL_SECRET_KEY: str


    @property
    def DATABASE_URL_asyncpg(self):
        #? postgresql+asyncpg://user:pass@localhost:5432/db_name
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    @property
    def ALEMBIC_DATABASE_URL_asyncpg(self):
        #? "postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
        return f"postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    

    
    model_config=SettingsConfigDict(env_file=".env")


settings = Settings()
    