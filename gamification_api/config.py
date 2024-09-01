import os

class Config:
    DB_NAME = os.getenv('DB_NAME', 'gamification_db')
    DB_USER = os.getenv('DB_USER', 'postgres')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
    DB_HOST = os.getenv('DB_HOST', 'db')  # 'db' es el nombre del servicio en docker-compose.yml
    DB_PORT = os.getenv('DB_PORT', '5432')
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')

    @staticmethod
    def get_db_uri():
        return f"dbname={Config.DB_NAME} user={Config.DB_USER} password={Config.DB_PASSWORD} host={Config.DB_HOST} port={Config.DB_PORT}"
