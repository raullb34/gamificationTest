
from flask import current_app

class Property:
    """Modelo de Property para manejar operaciones CRUD con PostgreSQL usando psycopg2."""

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.key = kwargs.get('key', None)
        self.value = kwargs.get('value', None)

    @staticmethod
    def create_table():
        """Crea la tabla de Property en la base de datos si no existe."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS property (
                id SERIAL PRIMARY KEY,
                key VARCHAR(50),
                value TEXT
            );
            """)
            connection.commit()
            print("Tabla 'property' creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla 'property': {e}")
            connection.rollback()
        finally:
            cursor.close()

    def save(self):
        """Guarda la instancia actual de Property en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO property (key, value) VALUES (%s, %s) RETURNING id;", (self.key, self.value))
            self.id = cursor.fetchone()[0]
            connection.commit()
            print(f"Property guardado exitosamente con ID: {self.id}.")
        except Exception as e:
            print(f"Error al guardar Property: {e}")
            connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def get_all():
        """Obtiene todos los registros de property de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM property;")
            results = cursor.fetchall()
            return [Property(**dict(zip(['id', 'key', 'value'], row))) for row in results]
        except Exception as e:
            print(f"Error al obtener Property: {e}")
            return []
        finally:
            cursor.close()

    @staticmethod
    def find_by_id(item_id):
        """Encuentra un Property por su ID."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM property WHERE id = %s;", (item_id,))
            row = cursor.fetchone()
            if row:
                return Property(**dict(zip(['id', 'key', 'value'], row)))
            return None
        except Exception as e:
            print(f"Error al buscar Property por ID: {e}")
            return None
        finally:
            cursor.close()

    def update(self):
        """Actualiza la instancia actual de Property en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE property SET key = %s, value = %s WHERE id = %s;", (self.key, self.value, self.id))
            connection.commit()
            print(f"Property con ID {self.id} actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar Property: {e}")
            connection.rollback()
        finally:
            cursor.close()

    def delete(self):
        """Elimina la instancia actual de Property de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM property WHERE id = %s;", (self.id,))
            connection.commit()
            print(f"Property con ID {self.id} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar Property: {e}")
            connection.rollback()
        finally:
            cursor.close()
