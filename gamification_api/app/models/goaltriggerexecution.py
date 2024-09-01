
from flask import current_app

class GoalTriggerExecution:
    """Modelo de GoalTriggerExecution para manejar operaciones CRUD con PostgreSQL usando psycopg2."""

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.trigger_id = kwargs.get('trigger_id', None)
        self.execution_time = kwargs.get('execution_time', None)

    @staticmethod
    def create_table():
        """Crea la tabla de GoalTriggerExecution en la base de datos si no existe."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS goaltriggerexecution (
                id SERIAL PRIMARY KEY,
                trigger_id INTEGER,
                execution_time TIMESTAMP
            );
            """)
            connection.commit()
            print("Tabla 'goaltriggerexecution' creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla 'goaltriggerexecution': {e}")
            connection.rollback()
        finally:
            cursor.close()

    def save(self):
        """Guarda la instancia actual de GoalTriggerExecution en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO goaltriggerexecution (trigger_id, execution_time) VALUES (%s, %s) RETURNING id;", (self.trigger_id, self.execution_time))
            self.id = cursor.fetchone()[0]
            connection.commit()
            print(f"GoalTriggerExecution guardado exitosamente con ID: {self.id}.")
        except Exception as e:
            print(f"Error al guardar GoalTriggerExecution: {e}")
            connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def get_all():
        """Obtiene todos los registros de goaltriggerexecution de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM goaltriggerexecution;")
            results = cursor.fetchall()
            return [GoalTriggerExecution(**dict(zip(['id', 'trigger_id', 'execution_time'], row))) for row in results]
        except Exception as e:
            print(f"Error al obtener GoalTriggerExecution: {e}")
            return []
        finally:
            cursor.close()

    @staticmethod
    def find_by_id(item_id):
        """Encuentra un GoalTriggerExecution por su ID."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM goaltriggerexecution WHERE id = %s;", (item_id,))
            row = cursor.fetchone()
            if row:
                return GoalTriggerExecution(**dict(zip(['id', 'trigger_id', 'execution_time'], row)))
            return None
        except Exception as e:
            print(f"Error al buscar GoalTriggerExecution por ID: {e}")
            return None
        finally:
            cursor.close()

    def update(self):
        """Actualiza la instancia actual de GoalTriggerExecution en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE goaltriggerexecution SET trigger_id = %s, execution_time = %s WHERE id = %s;", (self.trigger_id, self.execution_time, self.id))
            connection.commit()
            print(f"GoalTriggerExecution con ID {self.id} actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar GoalTriggerExecution: {e}")
            connection.rollback()
        finally:
            cursor.close()

    def delete(self):
        """Elimina la instancia actual de GoalTriggerExecution de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM goaltriggerexecution WHERE id = %s;", (self.id,))
            connection.commit()
            print(f"GoalTriggerExecution con ID {self.id} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar GoalTriggerExecution: {e}")
            connection.rollback()
        finally:
            cursor.close()
