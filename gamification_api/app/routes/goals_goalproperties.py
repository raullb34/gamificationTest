from flask import Blueprint, request, jsonify

goals_goalproperties_bp = Blueprint('goals_goalproperties', __name__, url_prefix='/goals_goalproperties')

@goals_goalproperties_bp.route('/', methods=['POST'])
def create_goals_goalproperties():
    data = request.get_json()
    # Lógica para crear goals_goalproperties
    return jsonify({'message': 'Goals_goalproperties creado exitosamente'}), 201

@goals_goalproperties_bp.route('/', methods=['GET'])
def get_goals_goalproperties():
    # Lógica para obtener todos los goals_goalproperties
    return jsonify({goals_goalproperties: []}), 200

@goals_goalproperties_bp.route('/<int:goals_goalproperties_id>', methods=['GET'])
def get_goals_goalproperties_by_id(goals_goalproperties_id):
    # Lógica para obtener un goals_goalproperties por ID
    return jsonify({goals_goalproperties: {}}), 200

@goals_goalproperties_bp.route('/<int:goals_goalproperties_id>', methods=['PUT'])
def update_goals_goalproperties(goals_goalproperties_id):
    data = request.get_json()
    # Lógica para actualizar goals_goalproperties
    return jsonify({'message': 'Goals_goalproperties actualizado exitosamente'}), 200

@goals_goalproperties_bp.route('/<int:goals_goalproperties_id>', methods=['DELETE'])
def delete_goals_goalproperties(goals_goalproperties_id):
    # Lógica para eliminar goals_goalproperties
    return jsonify({'message': 'Goals_goalproperties eliminado exitosamente'}), 200

