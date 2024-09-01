
from flask import current_app

class AuthUser:
    """Modelo de AuthUser para manejar operaciones CRUD con PostgreSQL usando psycopg2."""

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.username = kwargs.get('username', None)
        self.password_hash = kwargs.get('password_hash', None)

    @staticmethod
    def create_table():
        """Crea la tabla de AuthUser en la base de datos si no existe."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS authuser (
                id SERIAL PRIMARY KEY,
                username VARCHAR(100),
                password_hash TEXT
            );
            """)
            connection.commit()
            print("Tabla 'authuser' creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla 'authuser': {e}")
            connection.rollback()
        finally:
            cursor.close()

    def save(self):
        """Guarda la instancia actual de AuthUser en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO authuser (username, password_hash) VALUES (%s, %s) RETURNING id;", (self.username, self.password_hash))
            self.id = cursor.fetchone()[0]
            connection.commit()
            print(f"AuthUser guardado exitosamente con ID: {self.id}.")
        except Exception as e:
            print(f"Error al guardar AuthUser: {e}")
            connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def get_all():
        """Obtiene todos los registros de authuser de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM authuser;")
            results = cursor.fetchall()
            return [AuthUser(**dict(zip(['id', 'username', 'password_hash'], row))) for row in results]
        except Exception as e:
            print(f"Error al obtener AuthUser: {e}")
            return []
        finally:
            cursor.close()

    @staticmethod
    def find_by_id(item_id):
        """Encuentra un AuthUser por su ID."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM authuser WHERE id = %s;", (item_id,))
            row = cursor.fetchone()
            if row:
                return AuthUser(**dict(zip(['id', 'username', 'password_hash'], row)))
            return None
        except Exception as e:
            print(f"Error al buscar AuthUser por ID: {e}")
            return None
        finally:
            cursor.close()

    def update(self):
        """Actualiza la instancia actual de AuthUser en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE authuser SET username = %s, password_hash = %s WHERE id = %s;", (self.username, self.password_hash, self.id))
            connection.commit()
            print(f"AuthUser con ID {self.id} actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar AuthUser: {e}")
            connection.rollback()
        finally:
            cursor.close()

    def delete(self):
        """Elimina la instancia actual de AuthUser de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM authuser WHERE id = %s;", (self.id,))
            connection.commit()
            print(f"AuthUser con ID {self.id} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar AuthUser: {e}")
            connection.rollback()
        finally:
            cursor.close()
