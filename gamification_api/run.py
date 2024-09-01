from app import create_app
import logging
from app.models import init_app as init_models
from app.routes import register_routes as register_routes


# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = create_app()

init_models(app)  # Inicializar los modelos y crear las tablas
register_routes(app)  # Registrar todas las rutas en la aplicación

if __name__ == '__main__':
    # Definir el puerto en el que la aplicación correrá
    port = 5000
    
    # Mensaje de log que indica que la aplicación está en ejecución
    logger.info(f"Starting API on http://127.0.0.1:{port}")
    
    app.run(host='0.0.0.0', port=port)
