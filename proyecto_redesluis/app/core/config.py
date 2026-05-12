from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    DATABASE_URL = "sqlite:///./escuela.db"

settings = Settings()