
from flask import current_app

class Value:
    """Modelo de Value para manejar operaciones CRUD con PostgreSQL usando psycopg2."""

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.variable_id = kwargs.get('variable_id', None)
        self.user_id = kwargs.get('user_id', None)
        self.value = kwargs.get('value', None)

    @staticmethod
    def create_table():
        """Crea la tabla de Value en la base de datos si no existe."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS value (
                id SERIAL PRIMARY KEY,
                variable_id INTEGER,
                user_id INTEGER,
                value DOUBLE PRECISION
            );
            """)
            connection.commit()
            print("Tabla 'value' creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla 'value': {e}")
            connection.rollback()
        finally:
            cursor.close()

    def save(self):
        """Guarda la instancia actual de Value en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO value (variable_id, user_id, value) VALUES (%s, %s, %s) RETURNING id;", (self.variable_id, self.user_id, self.value))
            self.id = cursor.fetchone()[0]
            connection.commit()
            print(f"Value guardado exitosamente con ID: {self.id}.")
        except Exception as e:
            print(f"Error al guardar Value: {e}")
            connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def get_all():
        """Obtiene todos los registros de value de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM value;")
            results = cursor.fetchall()
            return [Value(**dict(zip(['id', 'variable_id', 'user_id', 'value'], row))) for row in results]
        except Exception as e:
            print(f"Error al obtener Value: {e}")
            return []
        finally:
            cursor.close()

    @staticmethod
    def find_by_id(item_id):
        """Encuentra un Value por su ID."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM value WHERE id = %s;", (item_id,))
            row = cursor.fetchone()
            if row:
                return Value(**dict(zip(['id', 'variable_id', 'user_id', 'value'], row)))
            return None
        except Exception as e:
            print(f"Error al buscar Value por ID: {e}")
            return None
        finally:
            cursor.close()

    def update(self):
        """Actualiza la instancia actual de Value en la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE value SET variable_id = %s, user_id = %s, value = %s WHERE id = %s;", (self.variable_id, self.user_id, self.value, self.id))
            connection.commit()
            print(f"Value con ID {self.id} actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar Value: {e}")
            connection.rollback()
        finally:
            cursor.close()

    def delete(self):
        """Elimina la instancia actual de Value de la base de datos."""
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM value WHERE id = %s;", (self.id,))
            connection.commit()
            print(f"Value con ID {self.id} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar Value: {e}")
            connection.rollback()
        finally:
            cursor.close()
