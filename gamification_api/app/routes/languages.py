from flask import Blueprint, request, jsonify

languages_bp = Blueprint('languages', __name__, url_prefix='/languages')

@languages_bp.route('/', methods=['GET'])
def get_languages():
    # Lógica para obtener todos los languages
    return jsonify({languages: []}), 200

