
from flask import current_app

class Users:
    """Modelo de Users para manejar operaciones CRUD con PostgreSQL usando psycopg2."""

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.email = kwargs.get('email', None)

    @staticmethod
    def create_table():
        """Crea la tabla de Users en la base de datos si no existe."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                email VARCHAR(100) UNIQUE
            );
            """)
            connection.commit()
            print("Tabla 'users' creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla 'users': {e}")
            connection.rollback()
        finally:
            cursor.close()

    def save(self):
        """Guarda la instancia actual de Users en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id;", (self.name, self.email))
            self.id = cursor.fetchone()[0]
            connection.commit()
            print(f"Users guardado exitosamente con ID: {self.id}.")
        except Exception as e:
            print(f"Error al guardar Users: {e}")
            connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def get_all():
        """Obtiene todos los registros de users de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM users;")
            results = cursor.fetchall()
            return [Users(**dict(zip(['id', 'name', 'email'], row))) for row in results]
        except Exception as e:
            print(f"Error al obtener Users: {e}")
            return []
        finally:
            cursor.close()

    @staticmethod
    def find_by_id(item_id):
        """Encuentra un Users por su ID."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM users WHERE id = %s;", (item_id,))
            row = cursor.fetchone()
            if row:
                return Users(**dict(zip(['id', 'name', 'email'], row)))
            return None
        except Exception as e:
            print(f"Error al buscar Users por ID: {e}")
            return None
        finally:
            cursor.close()

    def update(self):
        """Actualiza la instancia actual de Users en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE users SET name = %s, email = %s WHERE id = %s;", (self.name, self.email, self.id))
            connection.commit()
            print(f"Users con ID {self.id} actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar Users: {e}")
            connection.rollback()
        finally:
            cursor.close()

    def delete(self):
        """Elimina la instancia actual de Users de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM users WHERE id = %s;", (self.id,))
            connection.commit()
            print(f"Users con ID {self.id} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar Users: {e}")
            connection.rollback()
        finally:
            cursor.close()
