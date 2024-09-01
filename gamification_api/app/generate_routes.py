import os

# Directorio donde se crearán los archivos de rutas
ROUTES_DIR = 'routes'

# Lista de clases con detalles de sus métodos
classes = [
    {'name': 'users', 'methods': ['create', 'read_all', 'read_one', 'update', 'delete', 'login']},
    {'name': 'rewards', 'methods': ['create', 'read_all', 'read_one', 'update', 'delete']},
    {'name': 'languages', 'methods': ['read_all']},
    {'name': 'translationvariables', 'methods': ['create', 'read_all', 'read_one', 'update', 'delete']},
    {'name': 'translations', 'methods': ['create', 'read_all', 'read_one', 'update', 'delete']},
    {'name': 'user_groups', 'methods': ['create', 'read_all', 'read_one', 'update', 'delete']},
    {'name': 'properties', 'methods': ['create', 'read_all', 'read_one', 'update', 'delete']},
    {'name': 'achievementproperties', 'methods': ['create', 'read_all', 'read_one', 'update', 'delete']},
    {'name': 'goalproperties', 'methods': ['create', 'read_all', 'read_one', 'update', 'delete']},
    {'name': 'achievements', 'methods': ['create', 'read_all', 'read_one', 'update', 'delete']},
    {'name': 'achievements_rewards', 'methods': ['create', 'read_all', 'read_one', 'update', 'delete']},
    {'name': 'achievements_users', 'methods': ['create', 'read_all', 'read_one', 'update', 'delete']},
    {'name': 'goals', 'methods': ['create', 'read_all', 'read_one', 'update', 'delete']},
    {'name': 'goal_triggers', 'methods': ['create', 'read_all', 'read_one', 'update', 'delete']},
    {'name': 'goal_trigger_steps', 'methods': ['create', 'read_all', 'read_one', 'update', 'delete']},
    {'name': 'goal_trigger_executions', 'methods': ['create', 'read_all', 'read_one', 'update', 'delete']},
    {'name': 'variables', 'methods': ['create', 'read_all', 'read_one', 'update', 'delete']},
    {'name': 'values', 'methods': ['create', 'read_all', 'read_one', 'update', 'delete']},
    {'name': 'auth_users', 'methods': ['create', 'read_all', 'read_one', 'update', 'delete', 'login']},
    {'name': 'auth_roles', 'methods': ['create', 'read_all', 'read_one', 'update', 'delete']},
    {'name': 'auth_role_permissions', 'methods': ['create', 'read_all', 'read_one', 'update', 'delete']},
    {'name': 'auth_tokens', 'methods': ['create', 'read_all', 'read_one', 'update', 'delete', 'validate', 'revoke']},
    {'name': 'auth_users_roles', 'methods': ['create', 'read_all', 'read_one', 'update', 'delete']},
    {'name': 'user_devices', 'methods': ['create', 'read_all', 'read_one', 'update', 'delete']},
    {'name': 'user_messages', 'methods': ['create', 'read_all', 'read_one', 'update', 'delete', 'mark_as_read']},
    {'name': 'goal_evaluation_cache', 'methods': ['update_cache']},
    {'name': 'denials', 'methods': ['create', 'read_all', 'read_one', 'update', 'delete']},
    {'name': 'requirements', 'methods': ['create', 'read_all', 'read_one', 'update', 'delete']}
]

# Función para crear el directorio de rutas
def create_routes_directory():
    if not os.path.exists(ROUTES_DIR):
        os.makedirs(ROUTES_DIR)

# Función para generar las rutas CRUD para una clase
def generate_route_code(class_name, methods):
    code = f"from flask import Blueprint, request, jsonify\n\n{class_name}_bp = Blueprint('{class_name}', __name__, url_prefix='/{class_name}')\n\n"
    
    if 'create' in methods:
        code += f"@{class_name}_bp.route('/', methods=['POST'])\ndef create_{class_name}():\n    data = request.get_json()\n    # Lógica para crear {class_name}\n    return jsonify({{'message': '{class_name.capitalize()} creado exitosamente'}}), 201\n\n"
    
    if 'read_all' in methods:
        code += f"@{class_name}_bp.route('/', methods=['GET'])\ndef get_{class_name}():\n    # Lógica para obtener todos los {class_name}\n    return jsonify({{{class_name}: []}}), 200\n\n"
    
    if 'read_one' in methods:
        code += f"@{class_name}_bp.route('/<int:{class_name}_id>', methods=['GET'])\ndef get_{class_name}_by_id({class_name}_id):\n    # Lógica para obtener un {class_name} por ID\n    return jsonify({{{class_name}: {{}}}}), 200\n\n"
    
    if 'update' in methods:
        code += f"@{class_name}_bp.route('/<int:{class_name}_id>', methods=['PUT'])\ndef update_{class_name}({class_name}_id):\n    data = request.get_json()\n    # Lógica para actualizar {class_name}\n    return jsonify({{'message': '{class_name.capitalize()} actualizado exitosamente'}}), 200\n\n"
    
    if 'delete' in methods:
        code += f"@{class_name}_bp.route('/<int:{class_name}_id>', methods=['DELETE'])\ndef delete_{class_name}({class_name}_id):\n    # Lógica para eliminar {class_name}\n    return jsonify({{'message': '{class_name.capitalize()} eliminado exitosamente'}}), 200\n\n"
    
    # Métodos adicionales
    if 'login' in methods:
        code += f"@{class_name}_bp.route('/auth/login', methods=['POST'])\ndef login():\n    data = request.get_json()\n    # Lógica para autenticación de usuario\n    return jsonify({{'token': 'jwt_token'}}), 200\n\n"
    
    if 'validate' in methods:
        code += f"@{class_name}_bp.route('/validate', methods=['POST'])\ndef validate_token():\n    data = request.get_json()\n    # Lógica para validar token\n    return jsonify({{'message': 'Token válido'}}), 200\n\n"
    
    if 'revoke' in methods:
        code += f"@{class_name}_bp.route('/revoke', methods=['POST'])\ndef revoke_token():\n    data = request.get_json()\n    # Lógica para revocar token\n    return jsonify({{'message': 'Token revocado'}}), 200\n\n"
    
    if 'mark_as_read' in methods:
        code += f"@{class_name}_bp.route('/<int:message_id>/mark-as-read', methods=['PUT'])\ndef mark_as_read(message_id):\n    # Lógica para marcar mensaje como leído\n    return jsonify({{'message': 'Mensaje marcado como leído'}}), 200\n\n"
    
    if 'update_cache' in methods:
        code += f"@{class_name}_bp.route('/update-cache', methods=['POST'])\ndef update_cache():\n    # Lógica para actualizar la caché de evaluación de objetivos\n    return jsonify({{'message': 'Caché de evaluación actualizada'}}), 200\n\n"
    
    return code

# Función para generar todos los archivos de rutas
def generate_route_files():
    create_routes_directory()
    for class_info in classes:
        class_name = class_info['name']
        methods = class_info['methods']
        file_path = os.path.join(ROUTES_DIR, f"{class_name}.py")
        with open(file_path, 'w') as f:
            f.write(generate_route_code(class_name, methods))
        print(f"Archivo generado: {file_path}")

if __name__ == "__main__":
    generate_route_files()
