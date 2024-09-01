
from flask import current_app

class GoalProperty:
    """Modelo de GoalProperty para manejar operaciones CRUD con PostgreSQL usando psycopg2."""

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.goal_id = kwargs.get('goal_id', None)
        self.property_key = kwargs.get('property_key', None)
        self.value = kwargs.get('value', None)

    @staticmethod
    def create_table():
        """Crea la tabla de GoalProperty en la base de datos si no existe."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS goalproperty (
                id SERIAL PRIMARY KEY,
                goal_id INTEGER,
                property_key VARCHAR(50),
                value TEXT
            );
            """)
            connection.commit()
            print("Tabla 'goalproperty' creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla 'goalproperty': {e}")
            connection.rollback()
        finally:
            cursor.close()

    def save(self):
        """Guarda la instancia actual de GoalProperty en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO goalproperty (goal_id, property_key, value) VALUES (%s, %s, %s) RETURNING id;", (self.goal_id, self.property_key, self.value))
            self.id = cursor.fetchone()[0]
            connection.commit()
            print(f"GoalProperty guardado exitosamente con ID: {self.id}.")
        except Exception as e:
            print(f"Error al guardar GoalProperty: {e}")
            connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def get_all():
        """Obtiene todos los registros de goalproperty de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM goalproperty;")
            results = cursor.fetchall()
            return [GoalProperty(**dict(zip(['id', 'goal_id', 'property_key', 'value'], row))) for row in results]
        except Exception as e:
            print(f"Error al obtener GoalProperty: {e}")
            return []
        finally:
            cursor.close()

    @staticmethod
    def find_by_id(item_id):
        """Encuentra un GoalProperty por su ID."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM goalproperty WHERE id = %s;", (item_id,))
            row = cursor.fetchone()
            if row:
                return GoalProperty(**dict(zip(['id', 'goal_id', 'property_key', 'value'], row)))
            return None
        except Exception as e:
            print(f"Error al buscar GoalProperty por ID: {e}")
            return None
        finally:
            cursor.close()

    def update(self):
        """Actualiza la instancia actual de GoalProperty en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE goalproperty SET goal_id = %s, property_key = %s, value = %s WHERE id = %s;", (self.goal_id, self.property_key, self.value, self.id))
            connection.commit()
            print(f"GoalProperty con ID {self.id} actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar GoalProperty: {e}")
            connection.rollback()
        finally:
            cursor.close()

    def delete(self):
        """Elimina la instancia actual de GoalProperty de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM goalproperty WHERE id = %s;", (self.id,))
            connection.commit()
            print(f"GoalProperty con ID {self.id} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar GoalProperty: {e}")
            connection.rollback()
        finally:
            cursor.close()
