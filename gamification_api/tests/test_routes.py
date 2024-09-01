import unittest
import psycopg2
from app import create_app
from config import Config

class APITestCase(unittest.TestCase):
    def setUp(self):
        # Crear la aplicación Flask
        self.app = create_app()
        self.client = self.app.test_client()

        # Conectar a la base de datos
        self.connection = self.app.db_connection
        self.cursor = self.connection.cursor()

        # Crear las tablas necesarias
        self.create_tables()

    def tearDown(self):
        # Eliminar las tablas en el orden correcto con CASCADE
        self.drop_tables()

        # Cerrar la conexión a la base de datos
        self.cursor.close()
        self.connection.commit()

    def create_tables(self):
        """Crea las tablas necesarias para las pruebas."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                lat FLOAT,
                lon FLOAT,
                country VARCHAR(100),
                city VARCHAR(100),
                region VARCHAR(100),
                friends TEXT[],
                groups TEXT[],
                language VARCHAR(100),
                additional_public_data JSONB
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS variables (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                user_id INT,
                key VARCHAR(100),
                value FLOAT,
                FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS goals (
                id SERIAL PRIMARY KEY,
                variable VARCHAR(100),
                goal FLOAT,
                operator VARCHAR(10),
                condition JSONB
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS achievements (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                maxlevel INT,
                valid_start TIMESTAMP,
                valid_end TIMESTAMP,
                hidden BOOLEAN,
                priority INT
            );
        """)
        self.connection.commit()

    def drop_tables(self):
        """Elimina todas las tablas en el orden correcto usando CASCADE."""
        # Eliminar las tablas dependientes primero
        self.cursor.execute("DROP TABLE IF EXISTS variables CASCADE;")
        self.cursor.execute("DROP TABLE IF EXISTS goals CASCADE;")
        self.cursor.execute("DROP TABLE IF EXISTS achievements CASCADE;")
        # Eliminar la tabla principal
        self.cursor.execute("DROP TABLE IF EXISTS users CASCADE;")
        self.connection.commit()

    def test_add_or_update_subject(self):
        """Prueba para añadir o actualizar un sujeto."""
        response = self.client.post('/add_or_update_subject/1', data={
            'lat': 10.0,
            'lon': 20.0,
            'country': 'Country',
            'city': 'City',
            'region': 'Region',
            'language': 'English'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'success', response.data)

if __name__ == '__main__':
    unittest.main()
