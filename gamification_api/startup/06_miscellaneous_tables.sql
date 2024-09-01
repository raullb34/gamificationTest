-- Tabla user_devices
CREATE TABLE IF NOT EXISTS user_devices (
    user_id BIGINT,
    device_id VARCHAR(255),
    push_id VARCHAR(255),
    device_os VARCHAR(50),
    app_version VARCHAR(50),
    PRIMARY KEY (user_id, device_id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Tabla user_messages
CREATE TABLE IF NOT EXISTS user_messages (
    user_id BIGINT,
    message_id BIGINT,
    is_read BOOLEAN,
    PRIMARY KEY (user_id, message_id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Tabla goal_evaluation_cache
CREATE TABLE IF NOT EXISTS goal_evaluation_cache (
    goal_id INTEGER,
    user_id BIGINT,
    achieved BOOLEAN,
    value DOUBLE PRECISION,
    PRIMARY KEY (goal_id, user_id),
    FOREIGN KEY (goal_id) REFERENCES goals(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Tabla denials
CREATE TABLE IF NOT EXISTS denials (
    from_id INTEGER,
    to_id INTEGER,
    FOREIGN KEY (from_id) REFERENCES users(id),
    FOREIGN KEY (to_id) REFERENCES users(id)
);

-- Tabla requirements
CREATE TABLE IF NOT EXISTS requirements (
    from_id INTEGER,
    to_id INTEGER,
    FOREIGN KEY (from_id) REFERENCES users(id),
    FOREIGN KEY (to_id) REFERENCES users(id)
);
