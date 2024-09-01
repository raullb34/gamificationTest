
from flask import current_app

class GoalTrigger:
    """Modelo de GoalTrigger para manejar operaciones CRUD con PostgreSQL usando psycopg2."""

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.goal_id = kwargs.get('goal_id', None)
        self.trigger_condition = kwargs.get('trigger_condition', None)

    @staticmethod
    def create_table():
        """Crea la tabla de GoalTrigger en la base de datos si no existe."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS goaltrigger (
                id SERIAL PRIMARY KEY,
                goal_id INTEGER,
                trigger_condition TEXT
            );
            """)
            connection.commit()
            print("Tabla 'goaltrigger' creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla 'goaltrigger': {e}")
            connection.rollback()
        finally:
            cursor.close()

    def save(self):
        """Guarda la instancia actual de GoalTrigger en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO goaltrigger (goal_id, trigger_condition) VALUES (%s, %s) RETURNING id;", (self.goal_id, self.trigger_condition))
            self.id = cursor.fetchone()[0]
            connection.commit()
            print(f"GoalTrigger guardado exitosamente con ID: {self.id}.")
        except Exception as e:
            print(f"Error al guardar GoalTrigger: {e}")
            connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def get_all():
        """Obtiene todos los registros de goaltrigger de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM goaltrigger;")
            results = cursor.fetchall()
            return [GoalTrigger(**dict(zip(['id', 'goal_id', 'trigger_condition'], row))) for row in results]
        except Exception as e:
            print(f"Error al obtener GoalTrigger: {e}")
            return []
        finally:
            cursor.close()

    @staticmethod
    def find_by_id(item_id):
        """Encuentra un GoalTrigger por su ID."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM goaltrigger WHERE id = %s;", (item_id,))
            row = cursor.fetchone()
            if row:
                return GoalTrigger(**dict(zip(['id', 'goal_id', 'trigger_condition'], row)))
            return None
        except Exception as e:
            print(f"Error al buscar GoalTrigger por ID: {e}")
            return None
        finally:
            cursor.close()

    def update(self):
        """Actualiza la instancia actual de GoalTrigger en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE goaltrigger SET goal_id = %s, trigger_condition = %s WHERE id = %s;", (self.goal_id, self.trigger_condition, self.id))
            connection.commit()
            print(f"GoalTrigger con ID {self.id} actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar GoalTrigger: {e}")
            connection.rollback()
        finally:
            cursor.close()

    def delete(self):
        """Elimina la instancia actual de GoalTrigger de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM goaltrigger WHERE id = %s;", (self.id,))
            connection.commit()
            print(f"GoalTrigger con ID {self.id} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar GoalTrigger: {e}")
            connection.rollback()
        finally:
            cursor.close()
