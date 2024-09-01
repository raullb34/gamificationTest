
from flask import current_app

class TranslationVariable:
    """Modelo de TranslationVariable para manejar operaciones CRUD con PostgreSQL usando psycopg2."""

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.key = kwargs.get('key', None)
        self.description = kwargs.get('description', None)

    @staticmethod
    def create_table():
        """Crea la tabla de TranslationVariable en la base de datos si no existe."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS translationvariable (
                id SERIAL PRIMARY KEY,
                key VARCHAR(50),
                description TEXT
            );
            """)
            connection.commit()
            print("Tabla 'translationvariable' creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla 'translationvariable': {e}")
            connection.rollback()
        finally:
            cursor.close()

    def save(self):
        """Guarda la instancia actual de TranslationVariable en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO translationvariable (key, description) VALUES (%s, %s) RETURNING id;", (self.key, self.description))
            self.id = cursor.fetchone()[0]
            connection.commit()
            print(f"TranslationVariable guardado exitosamente con ID: {self.id}.")
        except Exception as e:
            print(f"Error al guardar TranslationVariable: {e}")
            connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def get_all():
        """Obtiene todos los registros de translationvariable de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM translationvariable;")
            results = cursor.fetchall()
            return [TranslationVariable(**dict(zip(['id', 'key', 'description'], row))) for row in results]
        except Exception as e:
            print(f"Error al obtener TranslationVariable: {e}")
            return []
        finally:
            cursor.close()

    @staticmethod
    def find_by_id(item_id):
        """Encuentra un TranslationVariable por su ID."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM translationvariable WHERE id = %s;", (item_id,))
            row = cursor.fetchone()
            if row:
                return TranslationVariable(**dict(zip(['id', 'key', 'description'], row)))
            return None
        except Exception as e:
            print(f"Error al buscar TranslationVariable por ID: {e}")
            return None
        finally:
            cursor.close()

    def update(self):
        """Actualiza la instancia actual de TranslationVariable en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE translationvariable SET key = %s, description = %s WHERE id = %s;", (self.key, self.description, self.id))
            connection.commit()
            print(f"TranslationVariable con ID {self.id} actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar TranslationVariable: {e}")
            connection.rollback()
        finally:
            cursor.close()

    def delete(self):
        """Elimina la instancia actual de TranslationVariable de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM translationvariable WHERE id = %s;", (self.id,))
            connection.commit()
            print(f"TranslationVariable con ID {self.id} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar TranslationVariable: {e}")
            connection.rollback()
        finally:
            cursor.close()
