from flask import Blueprint, request, jsonify

values_bp = Blueprint('values', __name__, url_prefix='/values')

@values_bp.route('/', methods=['POST'])
def create_values():
    data = request.get_json()
    # Lógica para crear values
    return jsonify({'message': 'Values creado exitosamente'}), 201

@values_bp.route('/', methods=['GET'])
def get_values():
    # Lógica para obtener todos los values
    return jsonify({values: []}), 200

@values_bp.route('/<int:values_id>', methods=['GET'])
def get_values_by_id(values_id):
    # Lógica para obtener un values por ID
    return jsonify({values: {}}), 200

@values_bp.route('/<int:values_id>', methods=['PUT'])
def update_values(values_id):
    data = request.get_json()
    # Lógica para actualizar values
    return jsonify({'message': 'Values actualizado exitosamente'}), 200

@values_bp.route('/<int:values_id>', methods=['DELETE'])
def delete_values(values_id):
    # Lógica para eliminar values
    return jsonify({'message': 'Values eliminado exitosamente'}), 200

