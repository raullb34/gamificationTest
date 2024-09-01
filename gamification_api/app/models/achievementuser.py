
from flask import current_app

class AchievementUser:
    """Modelo de AchievementUser para manejar operaciones CRUD con PostgreSQL usando psycopg2."""

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.achievement_id = kwargs.get('achievement_id', None)
        self.user_id = kwargs.get('user_id', None)

    @staticmethod
    def create_table():
        """Crea la tabla de AchievementUser en la base de datos si no existe."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS achievementuser (
                id SERIAL PRIMARY KEY,
                achievement_id INTEGER,
                user_id INTEGER
            );
            """)
            connection.commit()
            print("Tabla 'achievementuser' creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla 'achievementuser': {e}")
            connection.rollback()
        finally:
            cursor.close()

    def save(self):
        """Guarda la instancia actual de AchievementUser en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO achievementuser (achievement_id, user_id) VALUES (%s, %s) RETURNING id;", (self.achievement_id, self.user_id))
            self.id = cursor.fetchone()[0]
            connection.commit()
            print(f"AchievementUser guardado exitosamente con ID: {self.id}.")
        except Exception as e:
            print(f"Error al guardar AchievementUser: {e}")
            connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def get_all():
        """Obtiene todos los registros de achievementuser de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM achievementuser;")
            results = cursor.fetchall()
            return [AchievementUser(**dict(zip(['id', 'achievement_id', 'user_id'], row))) for row in results]
        except Exception as e:
            print(f"Error al obtener AchievementUser: {e}")
            return []
        finally:
            cursor.close()

    @staticmethod
    def find_by_id(item_id):
        """Encuentra un AchievementUser por su ID."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM achievementuser WHERE id = %s;", (item_id,))
            row = cursor.fetchone()
            if row:
                return AchievementUser(**dict(zip(['id', 'achievement_id', 'user_id'], row)))
            return None
        except Exception as e:
            print(f"Error al buscar AchievementUser por ID: {e}")
            return None
        finally:
            cursor.close()

    def update(self):
        """Actualiza la instancia actual de AchievementUser en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE achievementuser SET achievement_id = %s, user_id = %s WHERE id = %s;", (self.achievement_id, self.user_id, self.id))
            connection.commit()
            print(f"AchievementUser con ID {self.id} actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar AchievementUser: {e}")
            connection.rollback()
        finally:
            cursor.close()

    def delete(self):
        """Elimina la instancia actual de AchievementUser de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM achievementuser WHERE id = %s;", (self.id,))
            connection.commit()
            print(f"AchievementUser con ID {self.id} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar AchievementUser: {e}")
            connection.rollback()
        finally:
            cursor.close()
