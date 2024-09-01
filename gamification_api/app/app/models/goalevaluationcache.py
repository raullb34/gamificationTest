
from flask import current_app

class GoalEvaluationCache:
    """Modelo de GoalEvaluationCache para manejar operaciones CRUD con PostgreSQL usando psycopg2."""

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.goal_id = kwargs.get('goal_id', None)
        self.user_id = kwargs.get('user_id', None)
        self.last_evaluation = kwargs.get('last_evaluation', None)

    @staticmethod
    def create_table():
        """Crea la tabla de GoalEvaluationCache en la base de datos si no existe."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS goalevaluationcache (
                id SERIAL PRIMARY KEY,
                goal_id INTEGER,
                user_id INTEGER,
                last_evaluation TIMESTAMP
            );
            """)
            connection.commit()
            print("Tabla 'goalevaluationcache' creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla 'goalevaluationcache': {e}")
            connection.rollback()
        finally:
            cursor.close()

    def save(self):
        """Guarda la instancia actual de GoalEvaluationCache en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO goalevaluationcache (goal_id, user_id, last_evaluation) VALUES (%s, %s, %s) RETURNING id;", (self.goal_id, self.user_id, self.last_evaluation))
            self.id = cursor.fetchone()[0]
            connection.commit()
            print(f"GoalEvaluationCache guardado exitosamente con ID: {self.id}.")
        except Exception as e:
            print(f"Error al guardar GoalEvaluationCache: {e}")
            connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def get_all():
        """Obtiene todos los registros de goalevaluationcache de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM goalevaluationcache;")
            results = cursor.fetchall()
            return [GoalEvaluationCache(**dict(zip(['id', 'goal_id', 'user_id', 'last_evaluation'], row))) for row in results]
        except Exception as e:
            print(f"Error al obtener GoalEvaluationCache: {e}")
            return []
        finally:
            cursor.close()

    @staticmethod
    def find_by_id(item_id):
        """Encuentra un GoalEvaluationCache por su ID."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM goalevaluationcache WHERE id = %s;", (item_id,))
            row = cursor.fetchone()
            if row:
                return GoalEvaluationCache(**dict(zip(['id', 'goal_id', 'user_id', 'last_evaluation'], row)))
            return None
        except Exception as e:
            print(f"Error al buscar GoalEvaluationCache por ID: {e}")
            return None
        finally:
            cursor.close()

    def update(self):
        """Actualiza la instancia actual de GoalEvaluationCache en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE goalevaluationcache SET goal_id = %s, user_id = %s, last_evaluation = %s WHERE id = %s;", (self.goal_id, self.user_id, self.last_evaluation, self.id))
            connection.commit()
            print(f"GoalEvaluationCache con ID {self.id} actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar GoalEvaluationCache: {e}")
            connection.rollback()
        finally:
            cursor.close()

    def delete(self):
        """Elimina la instancia actual de GoalEvaluationCache de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM goalevaluationcache WHERE id = %s;", (self.id,))
            connection.commit()
            print(f"GoalEvaluationCache con ID {self.id} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar GoalEvaluationCache: {e}")
            connection.rollback()
        finally:
            cursor.close()
