
from flask import current_app

class AuthUserRole:
    """Modelo de AuthUserRole para manejar operaciones CRUD con PostgreSQL usando psycopg2."""

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.user_id = kwargs.get('user_id', None)
        self.role_id = kwargs.get('role_id', None)

    @staticmethod
    def create_table():
        """Crea la tabla de AuthUserRole en la base de datos si no existe."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS authuserrole (
                id SERIAL PRIMARY KEY,
                user_id INTEGER,
                role_id INTEGER
            );
            """)
            connection.commit()
            print("Tabla 'authuserrole' creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla 'authuserrole': {e}")
            connection.rollback()
        finally:
            cursor.close()

    def save(self):
        """Guarda la instancia actual de AuthUserRole en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO authuserrole (user_id, role_id) VALUES (%s, %s) RETURNING id;", (self.user_id, self.role_id))
            self.id = cursor.fetchone()[0]
            connection.commit()
            print(f"AuthUserRole guardado exitosamente con ID: {self.id}.")
        except Exception as e:
            print(f"Error al guardar AuthUserRole: {e}")
            connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def get_all():
        """Obtiene todos los registros de authuserrole de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM authuserrole;")
            results = cursor.fetchall()
            return [AuthUserRole(**dict(zip(['id', 'user_id', 'role_id'], row))) for row in results]
        except Exception as e:
            print(f"Error al obtener AuthUserRole: {e}")
            return []
        finally:
            cursor.close()

    @staticmethod
    def find_by_id(item_id):
        """Encuentra un AuthUserRole por su ID."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM authuserrole WHERE id = %s;", (item_id,))
            row = cursor.fetchone()
            if row:
                return AuthUserRole(**dict(zip(['id', 'user_id', 'role_id'], row)))
            return None
        except Exception as e:
            print(f"Error al buscar AuthUserRole por ID: {e}")
            return None
        finally:
            cursor.close()

    def update(self):
        """Actualiza la instancia actual de AuthUserRole en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE authuserrole SET user_id = %s, role_id = %s WHERE id = %s;", (self.user_id, self.role_id, self.id))
            connection.commit()
            print(f"AuthUserRole con ID {self.id} actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar AuthUserRole: {e}")
            connection.rollback()
        finally:
            cursor.close()

    def delete(self):
        """Elimina la instancia actual de AuthUserRole de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM authuserrole WHERE id = %s;", (self.id,))
            connection.commit()
            print(f"AuthUserRole con ID {self.id} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar AuthUserRole: {e}")
            connection.rollback()
        finally:
            cursor.close()
