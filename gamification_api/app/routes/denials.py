from flask import Blueprint, request, jsonify

denials_bp = Blueprint('denials', __name__, url_prefix='/denials')

@denials_bp.route('/', methods=['POST'])
def create_denials():
    data = request.get_json()
    # Lógica para crear denials
    return jsonify({'message': 'Denials creado exitosamente'}), 201

@denials_bp.route('/', methods=['GET'])
def get_denials():
    # Lógica para obtener todos los denials
    return jsonify({denials: []}), 200

@denials_bp.route('/<int:denials_id>', methods=['GET'])
def get_denials_by_id(denials_id):
    # Lógica para obtener un denials por ID
    return jsonify({denials: {}}), 200

@denials_bp.route('/<int:denials_id>', methods=['PUT'])
def update_denials(denials_id):
    data = request.get_json()
    # Lógica para actualizar denials
    return jsonify({'message': 'Denials actualizado exitosamente'}), 200

@denials_bp.route('/<int:denials_id>', methods=['DELETE'])
def delete_denials(denials_id):
    # Lógica para eliminar denials
    return jsonify({'message': 'Denials eliminado exitosamente'}), 200

