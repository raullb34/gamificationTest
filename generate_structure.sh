#!/bin/bash

# Crear la estructura de directorios
mkdir -p gamification_api/app
mkdir -p gamification_api/migrations
mkdir -p gamification_api/tests

# Crear los archivos de Python
cat <<EOL > gamification_api/run.py
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
EOL

cat <<EOL > gamification_api/app/__init__.py
from flask import Flask
from .extensions import db, migrate
from .routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar rutas
    register_routes(app)

    return app
EOL

cat <<EOL > gamification_api/app/routes.py
from flask import Blueprint, request, jsonify
from .models import User, Variable, Goal, Achievement, db

main = Blueprint('main', __name__)

@main.route('/add_or_update_subject/<int:subjectId>', methods=['POST'])
def add_or_update_subject(subjectId):
    data = request.form
    user = User.query.get(subjectId)
    if not user:
        user = User(id=subjectId)
    
    user.lat = data.get("lat")
    user.lon = data.get("lon")
    user.country = data.get("country")
    user.city = data.get("city")
    user.region = data.get("region")
    user.friends = data.get("friends", "").split(",")
    user.groups = data.get("groups", "").split(",")
    user.language = data.get("language")
    user.additional_public_data = data.get("additional_public_data")
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify({"status": "success", "subjectId": subjectId})

@main.route('/delete_user/<int:userId>', methods=['DELETE'])
def delete_user(userId):
    user = User.query.get(userId)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "error", "message": "User not found"}), 404

@main.route('/increase_value/<string:variable_name>/<int:userId>/<string:key>', methods=['POST'])
def increase_value(variable_name, userId, key):
    data = request.form
    value = float(data.get("value"))
    
    user = User.query.get(userId)
    if not user:
        return jsonify({"status": "error", "message": "User not registered"}), 404

    variable = Variable.query.filter_by(name=variable_name, user_id=userId, key=key).first()
    if not variable:
        variable = Variable(name=variable_name, user_id=userId, key=key, value=0)
    
    variable.value += value
    db.session.add(variable)
    db.session.commit()
    
    new_achievements = evaluate_goals(userId, variable_name)
    return jsonify({"status": "success", "new_achievements": new_achievements})

@main.route('/increase_multi_values', methods=['POST'])
def increase_multi_values():
    data = request.get_json()
    new_achievements = []

    for userId, variables_data in data.items():
        for variable_name, entries in variables_data.items():
            for entry in entries:
                key = entry.get("key")
                value = entry.get("value")
                increase_value(variable_name, int(userId), key)
                new_achievements += evaluate_goals(int(userId), variable_name)
    
    return jsonify({"status": "success", "new_achievements": new_achievements})

def evaluate_goals(userId, variable_name):
    achieved = []
    goals = Goal.query.filter_by(variable=variable_name).all()
    for goal in goals:
        # Lógica para evaluar si el usuario ha alcanzado la meta
        pass
    return achieved

@main.route('/progress/<int:userId>', methods=['GET'])
def get_progress(userId):
    user = User.query.get(userId)
    if not user:
        return jsonify({"status": "error", "message": "User not found"}), 404
    
    # Lógica para recuperar el progreso del usuario
    progress = {}  # Implementar la lógica
    return jsonify({"progress": progress})

@main.route('/achievement/<int:achievement_id>/level/<int:level>', methods=['GET'])
def get_achievement_level(achievement_id, level):
    achievement = Achievement.query.get(achievement_id)
    if not achievement:
        return jsonify({"status": "error", "message": "Achievement not found"}), 404
    
    # Lógica para recuperar la información del nivel de logro
    level_info = {}  # Implementar la lógica
    return jsonify({"achievement": level_info})

@main.route('/auth/login', methods=['POST'])
def auth_login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    # Aquí iría la lógica de autenticación
    return jsonify({"token": "foobar...."})

@main.route('/register_device/<int:user_id>', methods=['POST'])
def register_device(user_id):
    data = request.get_json()
    device_id = data.get('device_id')
    push_id = data.get('push_id')
    device_os = data.get('device_os')
    app_version = data.get('app_version')
    # Aquí iría la lógica para registrar el dispositivo
    return jsonify({"status": "ok"})

@main.route('/messages/<int:user_id>', methods=['GET'])
def get_messages(user_id):
    offset = request.args.get('offset', 0)
    # Aquí iría la lógica para recuperar mensajes
    messages = []  # Implementar la lógica
    return jsonify({"messages": messages})

@main.route('/read_messages/<int:user_id>', methods=['POST'])
def read_messages(user_id):
    data = request.get_json()
    message_id = data.get('message_id')
    # Aquí iría la lógica para marcar los mensajes como leídos
    return jsonify({"status": "ok"})

def register_routes(app):
    app.register_blueprint(main)
EOL

cat <<EOL > gamification_api/app/models.py
from .extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    country = db.Column(db.String(100))
    city = db.Column(db.String(100))
    region = db.Column(db.String(100))
    friends = db.Column(db.PickleType)  # Para guardar listas
    groups = db.Column(db.PickleType)   # Para guardar listas
    language = db.Column(db.String(100))
    additional_public_data = db.Column(db.JSON)

class Variable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    key = db.Column(db.String(100))
    value = db.Column(db.Float)
    user = db.relationship('User', backref=db.backref('variables', lazy=True))

class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    variable = db.Column(db.String(100))
    goal = db.Column(db.Float)
    operator = db.Column(db.String(10))
    condition = db.Column(db.JSON)

class Achievement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    maxlevel = db.Column(db.Integer)
    valid_start = db.Column(db.DateTime)
    valid_end = db.Column(db.DateTime)
    hidden = db.Column(db.Boolean)
    priority = db.Column(db.Integer)
EOL

cat <<EOL > gamification_api/app/extensions.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
EOL

cat <<EOL > gamification_api/config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
EOL

# Crear archivos de configuración y requerimientos
cat <<EOL > gamification_api/.env
DATABASE_URL=sqlite:///db.sqlite3
SECRET_KEY=your_secret_key
EOL

cat <<EOL > gamification_api/.flaskenv
FLASK_APP=run.py
FLASK_ENV=development
EOL

cat <<EOL > gamification_api/requirements.txt
Flask
Flask-SQLAlchemy
Flask-Migrate
EOL

# Crear archivo de pruebas unitarias
cat <<EOL > gamification_api/tests/test_routes.py
import unittest
from app import create_app, db

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.app_context().push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_or_update_subject(self):
        response = self.client.post('/add_or_update_subject/1', data={
            'lat': 10.0,
            'lon': 20.0,
            'country': 'Country',
            'city': 'City',
            'region': 'Region',
            'language': 'English'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'success', response.data)

if __name__ == '__main__':
    unittest.main()
EOL

# Mensaje de finalización
echo "Estructura de la API Flask generada con éxito en el directorio gamification_api/"

