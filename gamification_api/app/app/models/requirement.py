
from flask import current_app

class Requirement:
    """Modelo de Requirement para manejar operaciones CRUD con PostgreSQL usando psycopg2."""

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.requirement_name = kwargs.get('requirement_name', None)
        self.description = kwargs.get('description', None)

    @staticmethod
    def create_table():
        """Crea la tabla de Requirement en la base de datos si no existe."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS requirement (
                id SERIAL PRIMARY KEY,
                requirement_name VARCHAR(100),
                description TEXT
            );
            """)
            connection.commit()
            print("Tabla 'requirement' creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla 'requirement': {e}")
            connection.rollback()
        finally:
            cursor.close()

    def save(self):
        """Guarda la instancia actual de Requirement en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO requirement (requirement_name, description) VALUES (%s, %s) RETURNING id;", (self.requirement_name, self.description))
            self.id = cursor.fetchone()[0]
            connection.commit()
            print(f"Requirement guardado exitosamente con ID: {self.id}.")
        except Exception as e:
            print(f"Error al guardar Requirement: {e}")
            connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def get_all():
        """Obtiene todos los registros de requirement de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM requirement;")
            results = cursor.fetchall()
            return [Requirement(**dict(zip(['id', 'requirement_name', 'description'], row))) for row in results]
        except Exception as e:
            print(f"Error al obtener Requirement: {e}")
            return []
        finally:
            cursor.close()

    @staticmethod
    def find_by_id(item_id):
        """Encuentra un Requirement por su ID."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM requirement WHERE id = %s;", (item_id,))
            row = cursor.fetchone()
            if row:
                return Requirement(**dict(zip(['id', 'requirement_name', 'description'], row)))
            return None
        except Exception as e:
            print(f"Error al buscar Requirement por ID: {e}")
            return None
        finally:
            cursor.close()

    def update(self):
        """Actualiza la instancia actual de Requirement en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE requirement SET requirement_name = %s, description = %s WHERE id = %s;", (self.requirement_name, self.description, self.id))
            connection.commit()
            print(f"Requirement con ID {self.id} actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar Requirement: {e}")
            connection.rollback()
        finally:
            cursor.close()

    def delete(self):
        """Elimina la instancia actual de Requirement de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM requirement WHERE id = %s;", (self.id,))
            connection.commit()
            print(f"Requirement con ID {self.id} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar Requirement: {e}")
            connection.rollback()
        finally:
            cursor.close()
