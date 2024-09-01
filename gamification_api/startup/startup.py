import sys
import os
import psycopg2


# Agregar el directorio raíz al PYTHONPATH para poder importar config correctamente
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Obtener el directorio actual donde está ubicado el archivo startup.py
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

from config import Config  # Importa la configuración después de ajustar el PYTHONPATH


def execute_sql_file(connection, cursor, file_path):
    """Lee un archivo SQL y ejecuta sus comandos en la base de datos."""
    try:
        with open(file_path, 'r') as file:
            sql_commands = file.read()
            cursor.execute(sql_commands)
            connection.commit()
            print(f"Ejecutado con éxito: {file_path}")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error al ejecutar {file_path}: {error}")
        connection.rollback()

def create_tables():
    """Ejecuta todos los archivos SQL en el orden correcto para crear las tablas."""
    # Archivos SQL en orden de ejecución
    sql_files = [
        '01_base_tables.sql',
        '02_translation_properties_tables.sql',
        '03_achievements_goals_tables.sql',
        '04_variables_values_tables.sql',
        '05_auth_roles_tables.sql',
        '06_miscellaneous_tables.sql'
    ]

    # Inicializar variables de conexión
    connection = None
    cursor = None

    # Conectar a la base de datos PostgreSQL
    try:
        connection = psycopg2.connect(Config.get_db_uri())
        cursor = connection.cursor()

        # Ejecutar cada archivo SQL en secuencia
        for sql_file in sql_files:
            # Construir la ruta completa del archivo SQL
            file_path = os.path.join(CURRENT_DIR, sql_file)
            execute_sql_file(connection, cursor, file_path)

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error en la conexión a la base de datos: {error}")
    finally:
        # Cerrar cursor y conexión si se establecieron correctamente
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
            print("Conexión cerrada.")

if __name__ == "__main__":
    create_tables()

