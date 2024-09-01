
from flask import current_app

class UserDevice:
    """Modelo de UserDevice para manejar operaciones CRUD con PostgreSQL usando psycopg2."""

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.user_id = kwargs.get('user_id', None)
        self.device_id = kwargs.get('device_id', None)
        self.push_id = kwargs.get('push_id', None)

    @staticmethod
    def create_table():
        """Crea la tabla de UserDevice en la base de datos si no existe."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS userdevice (
                id SERIAL PRIMARY KEY,
                user_id INTEGER,
                device_id VARCHAR(100),
                push_id VARCHAR(100)
            );
            """)
            connection.commit()
            print("Tabla 'userdevice' creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla 'userdevice': {e}")
            connection.rollback()
        finally:
            cursor.close()

    def save(self):
        """Guarda la instancia actual de UserDevice en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO userdevice (user_id, device_id, push_id) VALUES (%s, %s, %s) RETURNING id;", (self.user_id, self.device_id, self.push_id))
            self.id = cursor.fetchone()[0]
            connection.commit()
            print(f"UserDevice guardado exitosamente con ID: {self.id}.")
        except Exception as e:
            print(f"Error al guardar UserDevice: {e}")
            connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def get_all():
        """Obtiene todos los registros de userdevice de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM userdevice;")
            results = cursor.fetchall()
            return [UserDevice(**dict(zip(['id', 'user_id', 'device_id', 'push_id'], row))) for row in results]
        except Exception as e:
            print(f"Error al obtener UserDevice: {e}")
            return []
        finally:
            cursor.close()

    @staticmethod
    def find_by_id(item_id):
        """Encuentra un UserDevice por su ID."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM userdevice WHERE id = %s;", (item_id,))
            row = cursor.fetchone()
            if row:
                return UserDevice(**dict(zip(['id', 'user_id', 'device_id', 'push_id'], row)))
            return None
        except Exception as e:
            print(f"Error al buscar UserDevice por ID: {e}")
            return None
        finally:
            cursor.close()

    def update(self):
        """Actualiza la instancia actual de UserDevice en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE userdevice SET user_id = %s, device_id = %s, push_id = %s WHERE id = %s;", (self.user_id, self.device_id, self.push_id, self.id))
            connection.commit()
            print(f"UserDevice con ID {self.id} actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar UserDevice: {e}")
            connection.rollback()
        finally:
            cursor.close()

    def delete(self):
        """Elimina la instancia actual de UserDevice de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM userdevice WHERE id = %s;", (self.id,))
            connection.commit()
            print(f"UserDevice con ID {self.id} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar UserDevice: {e}")
            connection.rollback()
        finally:
            cursor.close()
