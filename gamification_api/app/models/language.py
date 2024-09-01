
from flask import current_app

class Language:
    """Modelo de Language para manejar operaciones CRUD con PostgreSQL usando psycopg2."""

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.code = kwargs.get('code', None)
        self.name = kwargs.get('name', None)

    @staticmethod
    def create_table():
        """Crea la tabla de Language en la base de datos si no existe."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS language (
                id SERIAL PRIMARY KEY,
                code VARCHAR(5),
                name VARCHAR(50)
            );
            """)
            connection.commit()
            print("Tabla 'language' creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla 'language': {e}")
            connection.rollback()
        finally:
            cursor.close()

    def save(self):
        """Guarda la instancia actual de Language en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO language (code, name) VALUES (%s, %s) RETURNING id;", (self.code, self.name))
            self.id = cursor.fetchone()[0]
            connection.commit()
            print(f"Language guardado exitosamente con ID: {self.id}.")
        except Exception as e:
            print(f"Error al guardar Language: {e}")
            connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def get_all():
        """Obtiene todos los registros de language de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM language;")
            results = cursor.fetchall()
            return [Language(**dict(zip(['id', 'code', 'name'], row))) for row in results]
        except Exception as e:
            print(f"Error al obtener Language: {e}")
            return []
        finally:
            cursor.close()

    @staticmethod
    def find_by_id(item_id):
        """Encuentra un Language por su ID."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM language WHERE id = %s;", (item_id,))
            row = cursor.fetchone()
            if row:
                return Language(**dict(zip(['id', 'code', 'name'], row)))
            return None
        except Exception as e:
            print(f"Error al buscar Language por ID: {e}")
            return None
        finally:
            cursor.close()

    def update(self):
        """Actualiza la instancia actual de Language en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE language SET code = %s, name = %s WHERE id = %s;", (self.code, self.name, self.id))
            connection.commit()
            print(f"Language con ID {self.id} actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar Language: {e}")
            connection.rollback()
        finally:
            cursor.close()

    def delete(self):
        """Elimina la instancia actual de Language de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM language WHERE id = %s;", (self.id,))
            connection.commit()
            print(f"Language con ID {self.id} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar Language: {e}")
            connection.rollback()
        finally:
            cursor.close()
