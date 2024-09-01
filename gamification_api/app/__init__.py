from flask import Flask
import psycopg2
from config import Config

def create_app():
    """Crear y configurar la aplicación Flask."""
    app = Flask(__name__)
    
    # Configurar la aplicación desde el archivo de configuración
    app.config.from_object('config.Config')

    # Establecer la conexión a la base de datos
    app.db_connection = psycopg2.connect(Config.get_db_uri())

    return app
