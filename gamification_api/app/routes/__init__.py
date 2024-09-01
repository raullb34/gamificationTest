from flask import Blueprint

# Crear un blueprint para la API
api = Blueprint('api', __name__)

# Importar y registrar cada archivo de rutas
from .users import users_bp
from .rewards import rewards_bp
from .languages import languages_bp
from .translationvariables import translationvariables_bp
from .translations import translations_bp
from .user_groups import user_groups_bp
from .properties import properties_bp
from .achievementproperties import achievementproperties_bp
from .goalproperties import goalproperties_bp
from .achievements import achievements_bp
from .achievements_rewards import achievements_rewards_bp
from .achievements_users import achievements_users_bp
from .goals import goals_bp
from .goal_triggers import goal_triggers_bp
from .goal_trigger_steps import goal_trigger_steps_bp
from .goal_trigger_executions import goal_trigger_executions_bp
from .variables import variables_bp
from .values import values_bp
from .auth_users import auth_users_bp
from .auth_roles import auth_roles_bp
from .auth_role_permissions import auth_role_permissions_bp
from .auth_tokens import auth_tokens_bp
from .auth_users_roles import auth_users_roles_bp
from .user_devices import user_devices_bp
from .user_messages import user_messages_bp
from .goal_evaluation_cache import goal_evaluation_cache_bp
from .denials import denials_bp
from .requirements import requirements_bp
from .goals_goalproperties import goals_goalproperties_bp

# Registrar los blueprints de cada archivo de rutas
def register_routes(app):
    app.register_blueprint(users_bp)
    app.register_blueprint(rewards_bp)
    app.register_blueprint(languages_bp)
    app.register_blueprint(translationvariables_bp)
    app.register_blueprint(translations_bp)
    app.register_blueprint(user_groups_bp)
    app.register_blueprint(properties_bp)
    app.register_blueprint(achievementproperties_bp)
    app.register_blueprint(goalproperties_bp)
    app.register_blueprint(achievements_bp)
    app.register_blueprint(achievements_rewards_bp)
    app.register_blueprint(achievements_users_bp)
    app.register_blueprint(goals_bp)
    app.register_blueprint(goal_triggers_bp)
    app.register_blueprint(goal_trigger_steps_bp)
    app.register_blueprint(goal_trigger_executions_bp)
    app.register_blueprint(variables_bp)
    app.register_blueprint(values_bp)
    app.register_blueprint(auth_users_bp)
    app.register_blueprint(auth_roles_bp)
    app.register_blueprint(auth_role_permissions_bp)
    app.register_blueprint(auth_tokens_bp)
    app.register_blueprint(auth_users_roles_bp)
    app.register_blueprint(user_devices_bp)
    app.register_blueprint(user_messages_bp)
    app.register_blueprint(goal_evaluation_cache_bp)
    app.register_blueprint(denials_bp)
    app.register_blueprint(requirements_bp)
    app.register_blueprint(goals_goalproperties_bp)
