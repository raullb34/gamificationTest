from flask import Blueprint, request, jsonify

# Crear el blueprint para goals_goalproperties
goals_goalproperties_bp = Blueprint('goals_goalproperties', __name__, url_prefix='/goals_goalproperties')

# Define las rutas para goals_goalproperties
@goals_goalproperties_bp.route('/', methods=['GET'])
def get_goal_properties():
    # Lógica para manejar la solicitud GET
    return jsonify({'message': 'Propiedades de objetivos obtenidas con éxito'}), 200
