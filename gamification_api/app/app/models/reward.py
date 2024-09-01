
from flask import current_app

class Reward:
    """Modelo de Reward para manejar operaciones CRUD con PostgreSQL usando psycopg2."""

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.points = kwargs.get('points', None)

    @staticmethod
    def create_table():
        """Crea la tabla de Reward en la base de datos si no existe."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS reward (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                points INTEGER
            );
            """)
            connection.commit()
            print("Tabla 'reward' creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla 'reward': {e}")
            connection.rollback()
        finally:
            cursor.close()

    def save(self):
        """Guarda la instancia actual de Reward en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO reward (name, points) VALUES (%s, %s) RETURNING id;", (self.name, self.points))
            self.id = cursor.fetchone()[0]
            connection.commit()
            print(f"Reward guardado exitosamente con ID: {self.id}.")
        except Exception as e:
            print(f"Error al guardar Reward: {e}")
            connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def get_all():
        """Obtiene todos los registros de reward de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM reward;")
            results = cursor.fetchall()
            return [Reward(**dict(zip(['id', 'name', 'points'], row))) for row in results]
        except Exception as e:
            print(f"Error al obtener Reward: {e}")
            return []
        finally:
            cursor.close()

    @staticmethod
    def find_by_id(item_id):
        """Encuentra un Reward por su ID."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM reward WHERE id = %s;", (item_id,))
            row = cursor.fetchone()
            if row:
                return Reward(**dict(zip(['id', 'name', 'points'], row)))
            return None
        except Exception as e:
            print(f"Error al buscar Reward por ID: {e}")
            return None
        finally:
            cursor.close()

    def update(self):
        """Actualiza la instancia actual de Reward en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE reward SET name = %s, points = %s WHERE id = %s;", (self.name, self.points, self.id))
            connection.commit()
            print(f"Reward con ID {self.id} actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar Reward: {e}")
            connection.rollback()
        finally:
            cursor.close()

    def delete(self):
        """Elimina la instancia actual de Reward de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM reward WHERE id = %s;", (self.id,))
            connection.commit()
            print(f"Reward con ID {self.id} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar Reward: {e}")
            connection.rollback()
        finally:
            cursor.close()
