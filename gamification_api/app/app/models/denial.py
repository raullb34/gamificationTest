
from flask import current_app

class Denial:
    """Modelo de Denial para manejar operaciones CRUD con PostgreSQL usando psycopg2."""

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.user_id = kwargs.get('user_id', None)
        self.reason = kwargs.get('reason', None)

    @staticmethod
    def create_table():
        """Crea la tabla de Denial en la base de datos si no existe."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS denial (
                id SERIAL PRIMARY KEY,
                user_id INTEGER,
                reason TEXT
            );
            """)
            connection.commit()
            print("Tabla 'denial' creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla 'denial': {e}")
            connection.rollback()
        finally:
            cursor.close()

    def save(self):
        """Guarda la instancia actual de Denial en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO denial (user_id, reason) VALUES (%s, %s) RETURNING id;", (self.user_id, self.reason))
            self.id = cursor.fetchone()[0]
            connection.commit()
            print(f"Denial guardado exitosamente con ID: {self.id}.")
        except Exception as e:
            print(f"Error al guardar Denial: {e}")
            connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def get_all():
        """Obtiene todos los registros de denial de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM denial;")
            results = cursor.fetchall()
            return [Denial(**dict(zip(['id', 'user_id', 'reason'], row))) for row in results]
        except Exception as e:
            print(f"Error al obtener Denial: {e}")
            return []
        finally:
            cursor.close()

    @staticmethod
    def find_by_id(item_id):
        """Encuentra un Denial por su ID."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM denial WHERE id = %s;", (item_id,))
            row = cursor.fetchone()
            if row:
                return Denial(**dict(zip(['id', 'user_id', 'reason'], row)))
            return None
        except Exception as e:
            print(f"Error al buscar Denial por ID: {e}")
            return None
        finally:
            cursor.close()

    def update(self):
        """Actualiza la instancia actual de Denial en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE denial SET user_id = %s, reason = %s WHERE id = %s;", (self.user_id, self.reason, self.id))
            connection.commit()
            print(f"Denial con ID {self.id} actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar Denial: {e}")
            connection.rollback()
        finally:
            cursor.close()

    def delete(self):
        """Elimina la instancia actual de Denial de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM denial WHERE id = %s;", (self.id,))
            connection.commit()
            print(f"Denial con ID {self.id} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar Denial: {e}")
            connection.rollback()
        finally:
            cursor.close()
