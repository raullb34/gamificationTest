
from flask import current_app

class AchievementReward:
    """Modelo de AchievementReward para manejar operaciones CRUD con PostgreSQL usando psycopg2."""

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.achievement_id = kwargs.get('achievement_id', None)
        self.reward_id = kwargs.get('reward_id', None)

    @staticmethod
    def create_table():
        """Crea la tabla de AchievementReward en la base de datos si no existe."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS achievementreward (
                id SERIAL PRIMARY KEY,
                achievement_id INTEGER,
                reward_id INTEGER
            );
            """)
            connection.commit()
            print("Tabla 'achievementreward' creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla 'achievementreward': {e}")
            connection.rollback()
        finally:
            cursor.close()

    def save(self):
        """Guarda la instancia actual de AchievementReward en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO achievementreward (achievement_id, reward_id) VALUES (%s, %s) RETURNING id;", (self.achievement_id, self.reward_id))
            self.id = cursor.fetchone()[0]
            connection.commit()
            print(f"AchievementReward guardado exitosamente con ID: {self.id}.")
        except Exception as e:
            print(f"Error al guardar AchievementReward: {e}")
            connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def get_all():
        """Obtiene todos los registros de achievementreward de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM achievementreward;")
            results = cursor.fetchall()
            return [AchievementReward(**dict(zip(['id', 'achievement_id', 'reward_id'], row))) for row in results]
        except Exception as e:
            print(f"Error al obtener AchievementReward: {e}")
            return []
        finally:
            cursor.close()

    @staticmethod
    def find_by_id(item_id):
        """Encuentra un AchievementReward por su ID."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM achievementreward WHERE id = %s;", (item_id,))
            row = cursor.fetchone()
            if row:
                return AchievementReward(**dict(zip(['id', 'achievement_id', 'reward_id'], row)))
            return None
        except Exception as e:
            print(f"Error al buscar AchievementReward por ID: {e}")
            return None
        finally:
            cursor.close()

    def update(self):
        """Actualiza la instancia actual de AchievementReward en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE achievementreward SET achievement_id = %s, reward_id = %s WHERE id = %s;", (self.achievement_id, self.reward_id, self.id))
            connection.commit()
            print(f"AchievementReward con ID {self.id} actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar AchievementReward: {e}")
            connection.rollback()
        finally:
            cursor.close()

    def delete(self):
        """Elimina la instancia actual de AchievementReward de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM achievementreward WHERE id = %s;", (self.id,))
            connection.commit()
            print(f"AchievementReward con ID {self.id} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar AchievementReward: {e}")
            connection.rollback()
        finally:
            cursor.close()
