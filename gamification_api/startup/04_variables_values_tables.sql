-- Tabla variables
CREATE TABLE IF NOT EXISTS variables (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255),
    name_translation_id INTEGER,
    is_reward BOOLEAN,
    FOREIGN KEY (name_translation_id) REFERENCES translations(id)
);

-- Tabla values
CREATE TABLE IF NOT EXISTS values (
    user_id BIGINT,
    datetime TIMESTAMP WITH TIME ZONE,
    variable_id INTEGER,
    value INTEGER,
    key VARCHAR(100),
    PRIMARY KEY (user_id, datetime, variable_id, key),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (variable_id) REFERENCES variables(id)
);
