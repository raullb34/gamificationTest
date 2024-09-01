from flask import Blueprint, request, jsonify, current_app

main = Blueprint('main', __name__)

@main.route('/add_or_update_subject/<int:subjectId>', methods=['POST'])
def add_or_update_subject(subjectId):
    data = request.form
    connection = current_app.db_connection
    cursor = connection.cursor()
    
    # Verificar si el usuario existe
    cursor.execute("SELECT id FROM users WHERE id = %s;", (subjectId,))
    user = cursor.fetchone()

    if user:
        cursor.execute("""
            UPDATE users 
            SET lat = %s, lon = %s, country = %s, city = %s, region = %s, friends = %s, groups = %s, language = %s, additional_public_data = %s 
            WHERE id = %s;
        """, (
            data.get("lat"), data.get("lon"), data.get("country"), 
            data.get("city"), data.get("region"), data.get("friends"), 
            data.get("groups"), data.get("language"), data.get("additional_public_data"), 
            subjectId
        ))
    else:
        cursor.execute("""
            INSERT INTO users (id, lat, lon, country, city, region, friends, groups, language, additional_public_data)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """, (
            subjectId, data.get("lat"), data.get("lon"), data.get("country"), 
            data.get("city"), data.get("region"), data.get("friends"), 
            data.get("groups"), data.get("language"), data.get("additional_public_data")
        ))

    connection.commit()
    cursor.close()
    
    return jsonify({"status": "success", "subjectId": subjectId})

@main.route('/delete_user/<int:userId>', methods=['DELETE'])
def delete_user(userId):
    connection = current_app.db_connection
    cursor = connection.cursor()

    cursor.execute("DELETE FROM users WHERE id = %s;", (userId,))
    connection.commit()

    if cursor.rowcount > 0:
        response = {"status": "success"}
    else:
        response = {"status": "error", "message": "User not found"}
        return jsonify(response), 404

    cursor.close()
    return jsonify(response)

@main.route('/increase_value/<string:variable_name>/<int:userId>/<string:key>', methods=['POST'])
def increase_value(variable_name, userId, key):
    data = request.form
    value = float(data.get("value"))

    connection = current_app.db_connection
    cursor = connection.cursor()

    # Actualizar el valor de la variable
    cursor.execute("""
        INSERT INTO variables (name, user_id, key, value)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (name, user_id, key) 
        DO UPDATE SET value = variables.value + EXCLUDED.value;
    """, (variable_name, userId, key, value))
    
    connection.commit()
    cursor.close()

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
    # Evaluación de metas usando SQL nativo
    achieved = []
    connection = current_app.db_connection
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, goal, operator, condition FROM goals WHERE variable = %s;
    """, (variable_name,))
    
    goals = cursor.fetchall()
    for goal in goals:
        # Lógica para evaluar si el usuario ha alcanzado la meta usando SQL
        pass
    
    cursor.close()
    return achieved

@main.route('/progress/<int:userId>', methods=['GET'])
def get_progress(userId):
    connection = current_app.db_connection
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM achievements WHERE user_id = %s;", (userId,))
    progress = cursor.fetchall()

    cursor.close()
    return jsonify({"progress": progress})

@main.route('/achievement/<int:achievement_id>/level/<int:level>', methods=['GET'])
def get_achievement_level(achievement_id, level):
    connection = current_app.db_connection
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM achievements WHERE id = %s AND level = %s;
    """, (achievement_id, level))
    
    achievement = cursor.fetchone()
    cursor.close()

    if achievement:
        return jsonify({"achievement": achievement})
    else:
        return jsonify({"status": "error", "message": "Achievement not found"}), 404

@main.route('/auth/login', methods=['POST'])
def auth_login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    # Lógica de autenticación usando SQL nativo
    return jsonify({"token": "foobar...."})

@main.route('/register_device/<int:user_id>', methods=['POST'])
def register_device(user_id):
    data = request.get_json()
    connection = current_app.db_connection
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO devices (user_id, device_id, push_id, device_os, app_version)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (user_id, device_id)
        DO UPDATE SET push_id = EXCLUDED.push_id, device_os = EXCLUDED.device_os, app_version = EXCLUDED.app_version;
    """, (user_id, data.get('device_id'), data.get('push_id'), data.get('device_os'), data.get('app_version')))
    
    connection.commit()
    cursor.close()

    return jsonify({"status": "ok"})

@main.route('/messages/<int:user_id>', methods=['GET'])
def get_messages(user_id):
    connection = current_app.db_connection
    cursor = connection.cursor()

    offset = request.args.get('offset', 0)
    cursor.execute("SELECT * FROM messages WHERE user_id = %s LIMIT 100 OFFSET %s;", (user_id, offset))
    
    messages = cursor.fetchall()
    cursor.close()

    return jsonify({"messages": messages})

@main.route('/read_messages/<int:user_id>', methods=['POST'])
def read_messages(user_id):
    data = request.get_json()
    message_id = data.get('message_id')

    connection = current_app.db_connection
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE messages SET is_read = true 
        WHERE user_id = %s AND id <= %s;
    """, (user_id, message_id))
    
    connection.commit()
    cursor.close()

    return jsonify({"status": "ok"})

def register_routes(app):
    app.register_blueprint(main)
