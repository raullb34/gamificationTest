
from flask import current_app

class AuthRole:
    """Modelo de AuthRole para manejar operaciones CRUD con PostgreSQL usando psycopg2."""

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.role_name = kwargs.get('role_name', None)
        self.description = kwargs.get('description', None)

    @staticmethod
    def create_table():
        """Crea la tabla de AuthRole en la base de datos si no existe."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS authrole (
                id SERIAL PRIMARY KEY,
                role_name VARCHAR(50),
                description TEXT
            );
            """)
            connection.commit()
            print("Tabla 'authrole' creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla 'authrole': {e}")
            connection.rollback()
        finally:
            cursor.close()

    def save(self):
        """Guarda la instancia actual de AuthRole en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO authrole (role_name, description) VALUES (%s, %s) RETURNING id;", (self.role_name, self.description))
            self.id = cursor.fetchone()[0]
            connection.commit()
            print(f"AuthRole guardado exitosamente con ID: {self.id}.")
        except Exception as e:
            print(f"Error al guardar AuthRole: {e}")
            connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def get_all():
        """Obtiene todos los registros de authrole de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM authrole;")
            results = cursor.fetchall()
            return [AuthRole(**dict(zip(['id', 'role_name', 'description'], row))) for row in results]
        except Exception as e:
            print(f"Error al obtener AuthRole: {e}")
            return []
        finally:
            cursor.close()

    @staticmethod
    def find_by_id(item_id):
        """Encuentra un AuthRole por su ID."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM authrole WHERE id = %s;", (item_id,))
            row = cursor.fetchone()
            if row:
                return AuthRole(**dict(zip(['id', 'role_name', 'description'], row)))
            return None
        except Exception as e:
            print(f"Error al buscar AuthRole por ID: {e}")
            return None
        finally:
            cursor.close()

    def update(self):
        """Actualiza la instancia actual de AuthRole en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE authrole SET role_name = %s, description = %s WHERE id = %s;", (self.role_name, self.description, self.id))
            connection.commit()
            print(f"AuthRole con ID {self.id} actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar AuthRole: {e}")
            connection.rollback()
        finally:
            cursor.close()

    def delete(self):
        """Elimina la instancia actual de AuthRole de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM authrole WHERE id = %s;", (self.id,))
            connection.commit()
            print(f"AuthRole con ID {self.id} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar AuthRole: {e}")
            connection.rollback()
        finally:
            cursor.close()
