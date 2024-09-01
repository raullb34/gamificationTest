from flask import Blueprint, request, jsonify

properties_bp = Blueprint('properties', __name__, url_prefix='/properties')

@properties_bp.route('/', methods=['POST'])
def create_properties():
    data = request.get_json()
    # Lógica para crear properties
    return jsonify({'message': 'Properties creado exitosamente'}), 201

@properties_bp.route('/', methods=['GET'])
def get_properties():
    # Lógica para obtener todos los properties
    return jsonify({properties: []}), 200

@properties_bp.route('/<int:properties_id>', methods=['GET'])
def get_properties_by_id(properties_id):
    # Lógica para obtener un properties por ID
    return jsonify({properties: {}}), 200

@properties_bp.route('/<int:properties_id>', methods=['PUT'])
def update_properties(properties_id):
    data = request.get_json()
    # Lógica para actualizar properties
    return jsonify({'message': 'Properties actualizado exitosamente'}), 200

@properties_bp.route('/<int:properties_id>', methods=['DELETE'])
def delete_properties(properties_id):
    # Lógica para eliminar properties
    return jsonify({'message': 'Properties eliminado exitosamente'}), 200

