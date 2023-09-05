from pydantic_settings import BaseSettings

class Settings(BaseSettings):

        # Config para MongoDB
        user_mongo: str = "root"
        password_mongo: str = "root"
        address_mongo: str = "localhost"
        port_mongo: int = 27017
        URI_MONGO: str = f"mongodb://{user_mongo}:{password_mongo}@{address_mongo}:{port_mongo}/?authMechanism=DEFAULT"


settings = Settings()