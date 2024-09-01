
from flask import current_app

class GoalTriggerStep:
    """Modelo de GoalTriggerStep para manejar operaciones CRUD con PostgreSQL usando psycopg2."""

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.trigger_id = kwargs.get('trigger_id', None)
        self.step_order = kwargs.get('step_order', None)
        self.action = kwargs.get('action', None)

    @staticmethod
    def create_table():
        """Crea la tabla de GoalTriggerStep en la base de datos si no existe."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS goaltriggerstep (
                id SERIAL PRIMARY KEY,
                trigger_id INTEGER,
                step_order INTEGER,
                action TEXT
            );
            """)
            connection.commit()
            print("Tabla 'goaltriggerstep' creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla 'goaltriggerstep': {e}")
            connection.rollback()
        finally:
            cursor.close()

    def save(self):
        """Guarda la instancia actual de GoalTriggerStep en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO goaltriggerstep (trigger_id, step_order, action) VALUES (%s, %s, %s) RETURNING id;", (self.trigger_id, self.step_order, self.action))
            self.id = cursor.fetchone()[0]
            connection.commit()
            print(f"GoalTriggerStep guardado exitosamente con ID: {self.id}.")
        except Exception as e:
            print(f"Error al guardar GoalTriggerStep: {e}")
            connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def get_all():
        """Obtiene todos los registros de goaltriggerstep de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM goaltriggerstep;")
            results = cursor.fetchall()
            return [GoalTriggerStep(**dict(zip(['id', 'trigger_id', 'step_order', 'action'], row))) for row in results]
        except Exception as e:
            print(f"Error al obtener GoalTriggerStep: {e}")
            return []
        finally:
            cursor.close()

    @staticmethod
    def find_by_id(item_id):
        """Encuentra un GoalTriggerStep por su ID."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM goaltriggerstep WHERE id = %s;", (item_id,))
            row = cursor.fetchone()
            if row:
                return GoalTriggerStep(**dict(zip(['id', 'trigger_id', 'step_order', 'action'], row)))
            return None
        except Exception as e:
            print(f"Error al buscar GoalTriggerStep por ID: {e}")
            return None
        finally:
            cursor.close()

    def update(self):
        """Actualiza la instancia actual de GoalTriggerStep en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE goaltriggerstep SET trigger_id = %s, step_order = %s, action = %s WHERE id = %s;", (self.trigger_id, self.step_order, self.action, self.id))
            connection.commit()
            print(f"GoalTriggerStep con ID {self.id} actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar GoalTriggerStep: {e}")
            connection.rollback()
        finally:
            cursor.close()

    def delete(self):
        """Elimina la instancia actual de GoalTriggerStep de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM goaltriggerstep WHERE id = %s;", (self.id,))
            connection.commit()
            print(f"GoalTriggerStep con ID {self.id} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar GoalTriggerStep: {e}")
            connection.rollback()
        finally:
            cursor.close()
