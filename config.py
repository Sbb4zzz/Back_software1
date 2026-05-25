import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    DEBUG = True
    JWT_EXPIRATION_SECONDS = 3600
    FOOTBALL_API_KEY = "79375fc47630435d931e43d20e082bf2"

    # Database configuration
    DB_CONFIG = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'mundial_2026_hub',
        'port': 3306
    }

    # Logging configuration
    LOGGING_CONFIG = {
        'level': 'INFO',
        'format': '%(asctime)s - %(levelname)s - %(message)s',
        'handlers': ['file', 'console']
    }

