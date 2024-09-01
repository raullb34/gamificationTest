
from flask import current_app

class Goal:
    """Modelo de Goal para manejar operaciones CRUD con PostgreSQL usando psycopg2."""

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.condition = kwargs.get('condition', None)

    @staticmethod
    def create_table():
        """Crea la tabla de Goal en la base de datos si no existe."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS goal (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                condition TEXT
            );
            """)
            connection.commit()
            print("Tabla 'goal' creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla 'goal': {e}")
            connection.rollback()
        finally:
            cursor.close()

    def save(self):
        """Guarda la instancia actual de Goal en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO goal (name, condition) VALUES (%s, %s) RETURNING id;", (self.name, self.condition))
            self.id = cursor.fetchone()[0]
            connection.commit()
            print(f"Goal guardado exitosamente con ID: {self.id}.")
        except Exception as e:
            print(f"Error al guardar Goal: {e}")
            connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def get_all():
        """Obtiene todos los registros de goal de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM goal;")
            results = cursor.fetchall()
            return [Goal(**dict(zip(['id', 'name', 'condition'], row))) for row in results]
        except Exception as e:
            print(f"Error al obtener Goal: {e}")
            return []
        finally:
            cursor.close()

    @staticmethod
    def find_by_id(item_id):
        """Encuentra un Goal por su ID."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM goal WHERE id = %s;", (item_id,))
            row = cursor.fetchone()
            if row:
                return Goal(**dict(zip(['id', 'name', 'condition'], row)))
            return None
        except Exception as e:
            print(f"Error al buscar Goal por ID: {e}")
            return None
        finally:
            cursor.close()

    def update(self):
        """Actualiza la instancia actual de Goal en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE goal SET name = %s, condition = %s WHERE id = %s;", (self.name, self.condition, self.id))
            connection.commit()
            print(f"Goal con ID {self.id} actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar Goal: {e}")
            connection.rollback()
        finally:
            cursor.close()

    def delete(self):
        """Elimina la instancia actual de Goal de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM goal WHERE id = %s;", (self.id,))
            connection.commit()
            print(f"Goal con ID {self.id} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar Goal: {e}")
            connection.rollback()
        finally:
            cursor.close()
