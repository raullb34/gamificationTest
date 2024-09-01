
from flask import current_app

class UserMessage:
    """Modelo de UserMessage para manejar operaciones CRUD con PostgreSQL usando psycopg2."""

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.user_id = kwargs.get('user_id', None)
        self.message = kwargs.get('message', None)
        self.is_read = kwargs.get('is_read', None)

    @staticmethod
    def create_table():
        """Crea la tabla de UserMessage en la base de datos si no existe."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS usermessage (
                id SERIAL PRIMARY KEY,
                user_id INTEGER,
                message TEXT,
                is_read BOOLEAN
            );
            """)
            connection.commit()
            print("Tabla 'usermessage' creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla 'usermessage': {e}")
            connection.rollback()
        finally:
            cursor.close()

    def save(self):
        """Guarda la instancia actual de UserMessage en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO usermessage (user_id, message, is_read) VALUES (%s, %s, %s) RETURNING id;", (self.user_id, self.message, self.is_read))
            self.id = cursor.fetchone()[0]
            connection.commit()
            print(f"UserMessage guardado exitosamente con ID: {self.id}.")
        except Exception as e:
            print(f"Error al guardar UserMessage: {e}")
            connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def get_all():
        """Obtiene todos los registros de usermessage de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM usermessage;")
            results = cursor.fetchall()
            return [UserMessage(**dict(zip(['id', 'user_id', 'message', 'is_read'], row))) for row in results]
        except Exception as e:
            print(f"Error al obtener UserMessage: {e}")
            return []
        finally:
            cursor.close()

    @staticmethod
    def find_by_id(item_id):
        """Encuentra un UserMessage por su ID."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM usermessage WHERE id = %s;", (item_id,))
            row = cursor.fetchone()
            if row:
                return UserMessage(**dict(zip(['id', 'user_id', 'message', 'is_read'], row)))
            return None
        except Exception as e:
            print(f"Error al buscar UserMessage por ID: {e}")
            return None
        finally:
            cursor.close()

    def update(self):
        """Actualiza la instancia actual de UserMessage en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE usermessage SET user_id = %s, message = %s, is_read = %s WHERE id = %s;", (self.user_id, self.message, self.is_read, self.id))
            connection.commit()
            print(f"UserMessage con ID {self.id} actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar UserMessage: {e}")
            connection.rollback()
        finally:
            cursor.close()

    def delete(self):
        """Elimina la instancia actual de UserMessage de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM usermessage WHERE id = %s;", (self.id,))
            connection.commit()
            print(f"UserMessage con ID {self.id} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar UserMessage: {e}")
            connection.rollback()
        finally:
            cursor.close()
