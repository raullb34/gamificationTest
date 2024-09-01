from flask import current_app

from .users import Users
from .reward import Reward
from .language import Language
from .translationvariable import TranslationVariable
from .translation import Translation
from .usergroup import UserGroup
from .property import Property
from .achievementproperty import AchievementProperty
from .goalproperty import GoalProperty
from .achievement import Achievement
from .achievementreward import AchievementReward
from .achievementuser import AchievementUser
from .goal import Goal
from .goalsgoalproperty import GoalsGoalProperty
from .goaltrigger import GoalTrigger
from .goaltriggerstep import GoalTriggerStep
from .goaltriggerexecution import GoalTriggerExecution
from .variable import Variable
from .value import Value
from .authuser import AuthUser
from .authrole import AuthRole
from .authrolepermission import AuthRolePermission
from .authtoken import AuthToken
from .authuserrole import AuthUserRole
from .userdevice import UserDevice
from .usermessage import UserMessage
from .goalevaluationcache import GoalEvaluationCache
from .denial import Denial
from .requirement import Requirement

def init_app(app):
    if not app.db_connection:
        print('No hay conexión a la base de datos.')
        return

    # Crear tablas
    Users.create_table()
    Reward.create_table()
    Language.create_table()
    TranslationVariable.create_table()
    Translation.create_table()
    UserGroup.create_table()
    Property.create_table()
    AchievementProperty.create_table()
    GoalProperty.create_table()
    Achievement.create_table()
    AchievementReward.create_table()
    AchievementUser.create_table()
    Goal.create_table()
    GoalsGoalProperty.create_table()
    GoalTrigger.create_table()
    GoalTriggerStep.create_table()
    GoalTriggerExecution.create_table()
    Variable.create_table()
    Value.create_table()
    AuthUser.create_table()
    AuthRole.create_table()
    AuthRolePermission.create_table()
    AuthToken.create_table()
    AuthUserRole.create_table()
    UserDevice.create_table()
    UserMessage.create_table()
    GoalEvaluationCache.create_table()
    Denial.create_table()
    Requirement.create_table()
