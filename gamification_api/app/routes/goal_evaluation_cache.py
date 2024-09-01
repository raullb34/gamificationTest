from flask import Blueprint, request, jsonify

goal_evaluation_cache_bp = Blueprint('goal_evaluation_cache', __name__, url_prefix='/goal_evaluation_cache')

@goal_evaluation_cache_bp.route('/update-cache', methods=['POST'])
def update_cache():
    # Lógica para actualizar la caché de evaluación de objetivos
    return jsonify({'message': 'Caché de evaluación actualizada'}), 200

