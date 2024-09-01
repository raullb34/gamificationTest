import os

# Directorio donde se crearán los archivos de modelos
MODELS_DIR = 'app/models'

# Diccionario de nombres de clases para los modelos y sus atributos
model_classes = {
    'Users': {'name': 'VARCHAR(100)', 'email': 'VARCHAR(100) UNIQUE'},
    'Reward': {'name': 'VARCHAR(100)', 'points': 'INTEGER'},
    'Language': {'code': 'VARCHAR(5)', 'name': 'VARCHAR(50)'},
    'TranslationVariable': {'key': 'VARCHAR(50)', 'description': 'TEXT'},
    'Translation': {'variable_id': 'INTEGER', 'language_code': 'VARCHAR(5)', 'text': 'TEXT'},
    'UserGroup': {'name': 'VARCHAR(100)', 'description': 'TEXT'},
    'Property': {'key': 'VARCHAR(50)', 'value': 'TEXT'},
    'AchievementProperty': {'achievement_id': 'INTEGER', 'property_key': 'VARCHAR(50)', 'value': 'TEXT'},
    'GoalProperty': {'goal_id': 'INTEGER', 'property_key': 'VARCHAR(50)', 'value': 'TEXT'},
    'Achievement': {'name': 'VARCHAR(100)', 'description': 'TEXT'},
    'AchievementReward': {'achievement_id': 'INTEGER', 'reward_id': 'INTEGER'},
    'AchievementUser': {'achievement_id': 'INTEGER', 'user_id': 'INTEGER'},
    'Goal': {'name': 'VARCHAR(100)', 'condition': 'TEXT'},
    'GoalsGoalProperty': {'goal_id': 'INTEGER', 'property_id': 'INTEGER'},
    'GoalTrigger': {'goal_id': 'INTEGER', 'trigger_condition': 'TEXT'},
    'GoalTriggerStep': {'trigger_id': 'INTEGER', 'step_order': 'INTEGER', 'action': 'TEXT'},
    'GoalTriggerExecution': {'trigger_id': 'INTEGER', 'execution_time': 'TIMESTAMP'},
    'Variable': {'name': 'VARCHAR(100)', 'description': 'TEXT'},
    'Value': {'variable_id': 'INTEGER', 'user_id': 'INTEGER', 'value': 'DOUBLE PRECISION'},
    'AuthUser': {'username': 'VARCHAR(100)', 'password_hash': 'TEXT'},
    'AuthRole': {'role_name': 'VARCHAR(50)', 'description': 'TEXT'},
    'AuthRolePermission': {'role_id': 'INTEGER', 'permission': 'VARCHAR(100)'},
    'AuthToken': {'user_id': 'INTEGER', 'token': 'TEXT'},
    'AuthUserRole': {'user_id': 'INTEGER', 'role_id': 'INTEGER'},
    'UserDevice': {'user_id': 'INTEGER', 'device_id': 'VARCHAR(100)', 'push_id': 'VARCHAR(100)'},
    'UserMessage': {'user_id': 'INTEGER', 'message': 'TEXT', 'is_read': 'BOOLEAN'},
    'GoalEvaluationCache': {'goal_id': 'INTEGER', 'user_id': 'INTEGER', 'last_evaluation': 'TIMESTAMP'},
    'Denial': {'user_id': 'INTEGER', 'reason': 'TEXT'},
    'Requirement': {'requirement_name': 'VARCHAR(100)', 'description': 'TEXT'},
}

# Clase base para los modelos
model_template = """
from flask import current_app

class {class_name}:
    \"\"\"Modelo de {class_name} para manejar operaciones CRUD con PostgreSQL usando psycopg2.\"\"\"

    def __init__(self, **kwargs):
        {init_params}

    @staticmethod
    def create_table():
        \"\"\"Crea la tabla de {class_name} en la base de datos si no existe.\"\"\"
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute(\"\"\"
            CREATE TABLE IF NOT EXISTS {table_name} (
                id SERIAL PRIMARY KEY,
                {columns}
            );
            \"\"\")
            connection.commit()
            print("Tabla '{table_name}' creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla '{table_name}': {{e}}")
            connection.rollback()
        finally:
            cursor.close()

    def save(self):
        \"\"\"Guarda la instancia actual de {class_name} en la base de datos.\"\"\"
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO {table_name} ({fields}) VALUES ({placeholders}) RETURNING id;", ({values}))
            self.id = cursor.fetchone()[0]
            connection.commit()
            print(f"{class_name} guardado exitosamente con ID: {{self.id}}.")
        except Exception as e:
            print(f"Error al guardar {class_name}: {{e}}")
            connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def get_all():
        \"\"\"Obtiene todos los registros de {table_name} de la base de datos.\"\"\"
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM {table_name};")
            results = cursor.fetchall()
            return [{class_name}(**dict(zip(['id', {fields_list}], row))) for row in results]
        except Exception as e:
            print(f"Error al obtener {class_name}: {{e}}")
            return []
        finally:
            cursor.close()

    @staticmethod
    def find_by_id(item_id):
        \"\"\"Encuentra un {class_name} por su ID.\"\"\"
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM {table_name} WHERE id = %s;", (item_id,))
            row = cursor.fetchone()
            if row:
                return {class_name}(**dict(zip(['id', {fields_list}], row)))
            return None
        except Exception as e:
            print(f"Error al buscar {class_name} por ID: {{e}}")
            return None
        finally:
            cursor.close()

    def update(self):
        \"\"\"Actualiza la instancia actual de {class_name} en la base de datos.\"\"\"
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("UPDATE {table_name} SET {update_fields} WHERE id = %s;", ({values}, self.id))
            connection.commit()
            print(f"{class_name} con ID {{self.id}} actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar {class_name}: {{e}}")
            connection.rollback()
        finally:
            cursor.close()

    def delete(self):
        \"\"\"Elimina la instancia actual de {class_name} de la base de datos.\"\"\"
        connection = current_app.db_connection
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM {table_name} WHERE id = %s;", (self.id,))
            connection.commit()
            print(f"{class_name} con ID {{self.id}} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar {class_name}: {{e}}")
            connection.rollback()
        finally:
            cursor.close()
"""

# Función para eliminar el directorio de modelos y todos sus archivos
def clear_models_directory():
    if os.path.exists(MODELS_DIR):
        for file in os.listdir(MODELS_DIR):
            file_path = os.path.join(MODELS_DIR, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print(f"Todos los archivos en '{MODELS_DIR}' han sido eliminados.")
    else:
        os.makedirs(MODELS_DIR)
        print(f"Directorio '{MODELS_DIR}' creado.")

# Función para crear archivos de modelos con la estructura deseada
def generate_model_files():
    for class_name, attributes in model_classes.items():
        file_path = os.path.join(MODELS_DIR, f"{class_name.lower()}.py")
        columns = ",\n                ".join([f"{name} {type_}" for name, type_ in attributes.items()])
        fields = ", ".join(attributes.keys())
        placeholders = ", ".join(["%s"] * len(attributes))
        fields_list = ", ".join([f"'{name}'" for name in attributes.keys()])
        update_fields = ", ".join([f"{name} = %s" for name in attributes.keys()])
        init_params = "\n        ".join(f"self.{attr} = kwargs.get('{attr}', None)" for attr in ['id'] + list(attributes.keys()))
        with open(file_path, 'w', encoding='utf-8') as f:
            # Reemplaza {class_name} y {table_name} en el template
            f.write(model_template.format(
                class_name=class_name,
                table_name=class_name.lower(),
                columns=columns,
                fields=fields,
                placeholders=placeholders,
                values=", ".join([f"self.{field}" for field in attributes.keys()]),
                fields_list=fields_list,
                update_fields=update_fields,
                init_params=init_params
            ))
        print(f"Modelo '{class_name}' creado en '{file_path}'.")

# Función para generar el archivo __init__.py para importar todos los modelos
def generate_init_file():
    init_file_path = os.path.join(MODELS_DIR, '__init__.py')
    with open(init_file_path, 'w', encoding='utf-8') as f:
        f.write("from flask import current_app\n\n")
        imports = "\n".join([f"from .{class_name.lower()} import {class_name}" for class_name in model_classes.keys()])
        f.write(f"{imports}\n\n")
        f.write("def init_app(app):\n")
        f.write("    if not app.db_connection:\n")
        f.write("        print('No hay conexión a la base de datos.')\n")
        f.write("        return\n\n")
        f.write("    # Crear tablas\n")
        for class_name in model_classes.keys():
            f.write(f"    {class_name}.create_table()\n")
        print(f"Archivo '__init__.py' generado en '{init_file_path}'.")

if __name__ == "__main__":
    clear_models_directory()
    generate_model_files()
    generate_init_file()
    print("Todos los modelos han sido generados y registrados correctamente.")
