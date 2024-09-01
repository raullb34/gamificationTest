
from flask import current_app

class AuthToken:
    """Modelo de AuthToken para manejar operaciones CRUD con PostgreSQL usando psycopg2."""

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.user_id = kwargs.get('user_id', None)
        self.token = kwargs.get('token', None)

    @staticmethod
    def create_table():
        """Crea la tabla de AuthToken en la base de datos si no existe."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS authtoken (
                id SERIAL PRIMARY KEY,
                user_id INTEGER,
                token TEXT
            );
            """)
            connection.commit()
            print("Tabla 'authtoken' creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla 'authtoken': {e}")
            connection.rollback()
        finally:
            cursor.close()

    def save(self):
        """Guarda la instancia actual de AuthToken en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO authtoken (user_id, token) VALUES (%s, %s) RETURNING id;", (self.user_id, self.token))
            self.id = cursor.fetchone()[0]
            connection.commit()
            print(f"AuthToken guardado exitosamente con ID: {self.id}.")
        except Exception as e:
            print(f"Error al guardar AuthToken: {e}")
            connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def get_all():
        """Obtiene todos los registros de authtoken de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM authtoken;")
            results = cursor.fetchall()
            return [AuthToken(**dict(zip(['id', 'user_id', 'token'], row))) for row in results]
        except Exception as e:
            print(f"Error al obtener AuthToken: {e}")
            return []
        finally:
            cursor.close()

    @staticmethod
    def find_by_id(item_id):
        """Encuentra un AuthToken por su ID."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM authtoken WHERE id = %s;", (item_id,))
            row = cursor.fetchone()
            if row:
                return AuthToken(**dict(zip(['id', 'user_id', 'token'], row)))
            return None
        except Exception as e:
            print(f"Error al buscar AuthToken por ID: {e}")
            return None
        finally:
            cursor.close()

    def update(self):
        """Actualiza la instancia actual de AuthToken en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE authtoken SET user_id = %s, token = %s WHERE id = %s;", (self.user_id, self.token, self.id))
            connection.commit()
            print(f"AuthToken con ID {self.id} actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar AuthToken: {e}")
            connection.rollback()
        finally:
            cursor.close()

    def delete(self):
        """Elimina la instancia actual de AuthToken de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM authtoken WHERE id = %s;", (self.id,))
            connection.commit()
            print(f"AuthToken con ID {self.id} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar AuthToken: {e}")
            connection.rollback()
        finally:
            cursor.close()
