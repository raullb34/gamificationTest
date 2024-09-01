
from flask import current_app

class Translation:
    """Modelo de Translation para manejar operaciones CRUD con PostgreSQL usando psycopg2."""

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.variable_id = kwargs.get('variable_id', None)
        self.language_code = kwargs.get('language_code', None)
        self.text = kwargs.get('text', None)

    @staticmethod
    def create_table():
        """Crea la tabla de Translation en la base de datos si no existe."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS translation (
                id SERIAL PRIMARY KEY,
                variable_id INTEGER,
                language_code VARCHAR(5),
                text TEXT
            );
            """)
            connection.commit()
            print("Tabla 'translation' creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla 'translation': {e}")
            connection.rollback()
        finally:
            cursor.close()

    def save(self):
        """Guarda la instancia actual de Translation en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO translation (variable_id, language_code, text) VALUES (%s, %s, %s) RETURNING id;", (self.variable_id, self.language_code, self.text))
            self.id = cursor.fetchone()[0]
            connection.commit()
            print(f"Translation guardado exitosamente con ID: {self.id}.")
        except Exception as e:
            print(f"Error al guardar Translation: {e}")
            connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def get_all():
        """Obtiene todos los registros de translation de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM translation;")
            results = cursor.fetchall()
            return [Translation(**dict(zip(['id', 'variable_id', 'language_code', 'text'], row))) for row in results]
        except Exception as e:
            print(f"Error al obtener Translation: {e}")
            return []
        finally:
            cursor.close()

    @staticmethod
    def find_by_id(item_id):
        """Encuentra un Translation por su ID."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM translation WHERE id = %s;", (item_id,))
            row = cursor.fetchone()
            if row:
                return Translation(**dict(zip(['id', 'variable_id', 'language_code', 'text'], row)))
            return None
        except Exception as e:
            print(f"Error al buscar Translation por ID: {e}")
            return None
        finally:
            cursor.close()

    def update(self):
        """Actualiza la instancia actual de Translation en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE translation SET variable_id = %s, language_code = %s, text = %s WHERE id = %s;", (self.variable_id, self.language_code, self.text, self.id))
            connection.commit()
            print(f"Translation con ID {self.id} actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar Translation: {e}")
            connection.rollback()
        finally:
            cursor.close()

    def delete(self):
        """Elimina la instancia actual de Translation de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM translation WHERE id = %s;", (self.id,))
            connection.commit()
            print(f"Translation con ID {self.id} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar Translation: {e}")
            connection.rollback()
        finally:
            cursor.close()
