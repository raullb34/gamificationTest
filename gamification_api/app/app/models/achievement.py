
from flask import current_app

class Achievement:
    """Modelo de Achievement para manejar operaciones CRUD con PostgreSQL usando psycopg2."""

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)

    @staticmethod
    def create_table():
        """Crea la tabla de Achievement en la base de datos si no existe."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS achievement (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                description TEXT
            );
            """)
            connection.commit()
            print("Tabla 'achievement' creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla 'achievement': {e}")
            connection.rollback()
        finally:
            cursor.close()

    def save(self):
        """Guarda la instancia actual de Achievement en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO achievement (name, description) VALUES (%s, %s) RETURNING id;", (self.name, self.description))
            self.id = cursor.fetchone()[0]
            connection.commit()
            print(f"Achievement guardado exitosamente con ID: {self.id}.")
        except Exception as e:
            print(f"Error al guardar Achievement: {e}")
            connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def get_all():
        """Obtiene todos los registros de achievement de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM achievement;")
            results = cursor.fetchall()
            return [Achievement(**dict(zip(['id', 'name', 'description'], row))) for row in results]
        except Exception as e:
            print(f"Error al obtener Achievement: {e}")
            return []
        finally:
            cursor.close()

    @staticmethod
    def find_by_id(item_id):
        """Encuentra un Achievement por su ID."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM achievement WHERE id = %s;", (item_id,))
            row = cursor.fetchone()
            if row:
                return Achievement(**dict(zip(['id', 'name', 'description'], row)))
            return None
        except Exception as e:
            print(f"Error al buscar Achievement por ID: {e}")
            return None
        finally:
            cursor.close()

    def update(self):
        """Actualiza la instancia actual de Achievement en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE achievement SET name = %s, description = %s WHERE id = %s;", (self.name, self.description, self.id))
            connection.commit()
            print(f"Achievement con ID {self.id} actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar Achievement: {e}")
            connection.rollback()
        finally:
            cursor.close()

    def delete(self):
        """Elimina la instancia actual de Achievement de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM achievement WHERE id = %s;", (self.id,))
            connection.commit()
            print(f"Achievement con ID {self.id} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar Achievement: {e}")
            connection.rollback()
        finally:
            cursor.close()
