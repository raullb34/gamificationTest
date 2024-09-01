
from flask import current_app

class Variable:
    """Modelo de Variable para manejar operaciones CRUD con PostgreSQL usando psycopg2."""

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)

    @staticmethod
    def create_table():
        """Crea la tabla de Variable en la base de datos si no existe."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS variable (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                description TEXT
            );
            """)
            connection.commit()
            print("Tabla 'variable' creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla 'variable': {e}")
            connection.rollback()
        finally:
            cursor.close()

    def save(self):
        """Guarda la instancia actual de Variable en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO variable (name, description) VALUES (%s, %s) RETURNING id;", (self.name, self.description))
            self.id = cursor.fetchone()[0]
            connection.commit()
            print(f"Variable guardado exitosamente con ID: {self.id}.")
        except Exception as e:
            print(f"Error al guardar Variable: {e}")
            connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def get_all():
        """Obtiene todos los registros de variable de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM variable;")
            results = cursor.fetchall()
            return [Variable(**dict(zip(['id', 'name', 'description'], row))) for row in results]
        except Exception as e:
            print(f"Error al obtener Variable: {e}")
            return []
        finally:
            cursor.close()

    @staticmethod
    def find_by_id(item_id):
        """Encuentra un Variable por su ID."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM variable WHERE id = %s;", (item_id,))
            row = cursor.fetchone()
            if row:
                return Variable(**dict(zip(['id', 'name', 'description'], row)))
            return None
        except Exception as e:
            print(f"Error al buscar Variable por ID: {e}")
            return None
        finally:
            cursor.close()

    def update(self):
        """Actualiza la instancia actual de Variable en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE variable SET name = %s, description = %s WHERE id = %s;", (self.name, self.description, self.id))
            connection.commit()
            print(f"Variable con ID {self.id} actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar Variable: {e}")
            connection.rollback()
        finally:
            cursor.close()

    def delete(self):
        """Elimina la instancia actual de Variable de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM variable WHERE id = %s;", (self.id,))
            connection.commit()
            print(f"Variable con ID {self.id} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar Variable: {e}")
            connection.rollback()
        finally:
            cursor.close()
