
from flask import current_app

class GoalGoalProperty:
    """Modelo de GoalGoalProperty para manejar operaciones CRUD con PostgreSQL usando psycopg2."""

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.goal_id = kwargs.get('goal_id', None)
        self.property_id = kwargs.get('property_id', None)

    @staticmethod
    def create_table():
        """Crea la tabla de GoalGoalProperty en la base de datos si no existe."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS goalgoalproperty (
                id SERIAL PRIMARY KEY,
                goal_id INTEGER,
                property_id INTEGER
            );
            """)
            connection.commit()
            print("Tabla 'goalgoalproperty' creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla 'goalgoalproperty': {e}")
            connection.rollback()
        finally:
            cursor.close()

    def save(self):
        """Guarda la instancia actual de GoalGoalProperty en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO goalgoalproperty (goal_id, property_id) VALUES (%s, %s) RETURNING id;", (self.goal_id, self.property_id))
            self.id = cursor.fetchone()[0]
            connection.commit()
            print(f"GoalGoalProperty guardado exitosamente con ID: {self.id}.")
        except Exception as e:
            print(f"Error al guardar GoalGoalProperty: {e}")
            connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def get_all():
        """Obtiene todos los registros de goalgoalproperty de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM goalgoalproperty;")
            results = cursor.fetchall()
            return [GoalGoalProperty(**dict(zip(['id', 'goal_id', 'property_id'], row))) for row in results]
        except Exception as e:
            print(f"Error al obtener GoalGoalProperty: {e}")
            return []
        finally:
            cursor.close()

    @staticmethod
    def find_by_id(item_id):
        """Encuentra un GoalGoalProperty por su ID."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM goalgoalproperty WHERE id = %s;", (item_id,))
            row = cursor.fetchone()
            if row:
                return GoalGoalProperty(**dict(zip(['id', 'goal_id', 'property_id'], row)))
            return None
        except Exception as e:
            print(f"Error al buscar GoalGoalProperty por ID: {e}")
            return None
        finally:
            cursor.close()

    def update(self):
        """Actualiza la instancia actual de GoalGoalProperty en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE goalgoalproperty SET goal_id = %s, property_id = %s WHERE id = %s;", (self.goal_id, self.property_id, self.id))
            connection.commit()
            print(f"GoalGoalProperty con ID {self.id} actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar GoalGoalProperty: {e}")
            connection.rollback()
        finally:
            cursor.close()

    def delete(self):
        """Elimina la instancia actual de GoalGoalProperty de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM goalgoalproperty WHERE id = %s;", (self.id,))
            connection.commit()
            print(f"GoalGoalProperty con ID {self.id} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar GoalGoalProperty: {e}")
            connection.rollback()
        finally:
            cursor.close()
