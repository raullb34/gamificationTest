
from flask import current_app

class AchievementProperty:
    """Modelo de AchievementProperty para manejar operaciones CRUD con PostgreSQL usando psycopg2."""

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.achievement_id = kwargs.get('achievement_id', None)
        self.property_key = kwargs.get('property_key', None)
        self.value = kwargs.get('value', None)

    @staticmethod
    def create_table():
        """Crea la tabla de AchievementProperty en la base de datos si no existe."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS achievementproperty (
                id SERIAL PRIMARY KEY,
                achievement_id INTEGER,
                property_key VARCHAR(50),
                value TEXT
            );
            """)
            connection.commit()
            print("Tabla 'achievementproperty' creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla 'achievementproperty': {e}")
            connection.rollback()
        finally:
            cursor.close()

    def save(self):
        """Guarda la instancia actual de AchievementProperty en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO achievementproperty (achievement_id, property_key, value) VALUES (%s, %s, %s) RETURNING id;", (self.achievement_id, self.property_key, self.value))
            self.id = cursor.fetchone()[0]
            connection.commit()
            print(f"AchievementProperty guardado exitosamente con ID: {self.id}.")
        except Exception as e:
            print(f"Error al guardar AchievementProperty: {e}")
            connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def get_all():
        """Obtiene todos los registros de achievementproperty de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM achievementproperty;")
            results = cursor.fetchall()
            return [AchievementProperty(**dict(zip(['id', 'achievement_id', 'property_key', 'value'], row))) for row in results]
        except Exception as e:
            print(f"Error al obtener AchievementProperty: {e}")
            return []
        finally:
            cursor.close()

    @staticmethod
    def find_by_id(item_id):
        """Encuentra un AchievementProperty por su ID."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM achievementproperty WHERE id = %s;", (item_id,))
            row = cursor.fetchone()
            if row:
                return AchievementProperty(**dict(zip(['id', 'achievement_id', 'property_key', 'value'], row)))
            return None
        except Exception as e:
            print(f"Error al buscar AchievementProperty por ID: {e}")
            return None
        finally:
            cursor.close()

    def update(self):
        """Actualiza la instancia actual de AchievementProperty en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE achievementproperty SET achievement_id = %s, property_key = %s, value = %s WHERE id = %s;", (self.achievement_id, self.property_key, self.value, self.id))
            connection.commit()
            print(f"AchievementProperty con ID {self.id} actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar AchievementProperty: {e}")
            connection.rollback()
        finally:
            cursor.close()

    def delete(self):
        """Elimina la instancia actual de AchievementProperty de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM achievementproperty WHERE id = %s;", (self.id,))
            connection.commit()
            print(f"AchievementProperty con ID {self.id} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar AchievementProperty: {e}")
            connection.rollback()
        finally:
            cursor.close()
