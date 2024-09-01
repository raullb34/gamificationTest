
from flask import current_app

class AuthRolePermission:
    """Modelo de AuthRolePermission para manejar operaciones CRUD con PostgreSQL usando psycopg2."""

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.role_id = kwargs.get('role_id', None)
        self.permission = kwargs.get('permission', None)

    @staticmethod
    def create_table():
        """Crea la tabla de AuthRolePermission en la base de datos si no existe."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS authrolepermission (
                id SERIAL PRIMARY KEY,
                role_id INTEGER,
                permission VARCHAR(100)
            );
            """)
            connection.commit()
            print("Tabla 'authrolepermission' creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla 'authrolepermission': {e}")
            connection.rollback()
        finally:
            cursor.close()

    def save(self):
        """Guarda la instancia actual de AuthRolePermission en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO authrolepermission (role_id, permission) VALUES (%s, %s) RETURNING id;", (self.role_id, self.permission))
            self.id = cursor.fetchone()[0]
            connection.commit()
            print(f"AuthRolePermission guardado exitosamente con ID: {self.id}.")
        except Exception as e:
            print(f"Error al guardar AuthRolePermission: {e}")
            connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def get_all():
        """Obtiene todos los registros de authrolepermission de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM authrolepermission;")
            results = cursor.fetchall()
            return [AuthRolePermission(**dict(zip(['id', 'role_id', 'permission'], row))) for row in results]
        except Exception as e:
            print(f"Error al obtener AuthRolePermission: {e}")
            return []
        finally:
            cursor.close()

    @staticmethod
    def find_by_id(item_id):
        """Encuentra un AuthRolePermission por su ID."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM authrolepermission WHERE id = %s;", (item_id,))
            row = cursor.fetchone()
            if row:
                return AuthRolePermission(**dict(zip(['id', 'role_id', 'permission'], row)))
            return None
        except Exception as e:
            print(f"Error al buscar AuthRolePermission por ID: {e}")
            return None
        finally:
            cursor.close()

    def update(self):
        """Actualiza la instancia actual de AuthRolePermission en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE authrolepermission SET role_id = %s, permission = %s WHERE id = %s;", (self.role_id, self.permission, self.id))
            connection.commit()
            print(f"AuthRolePermission con ID {self.id} actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar AuthRolePermission: {e}")
            connection.rollback()
        finally:
            cursor.close()

    def delete(self):
        """Elimina la instancia actual de AuthRolePermission de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM authrolepermission WHERE id = %s;", (self.id,))
            connection.commit()
            print(f"AuthRolePermission con ID {self.id} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar AuthRolePermission: {e}")
            connection.rollback()
        finally:
            cursor.close()
