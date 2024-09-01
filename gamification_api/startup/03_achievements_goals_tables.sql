-- Tabla achievements
CREATE TABLE IF NOT EXISTS achievements (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255),
    maxlevel INTEGER,
    valid_start DATE,
    valid_end DATE,
    hidden BOOLEAN,
    relevance VARCHAR(50),
    evaluation_timezone VARCHAR(50),
    view_permission VARCHAR(50)
);

-- Tabla achievements_rewards
CREATE TABLE IF NOT EXISTS achievements_rewards (
    id INTEGER PRIMARY KEY,
    achievement_id INTEGER,
    reward_id INTEGER,
    value VARCHAR(255),
    value_translation_id INTEGER,
    from_level INTEGER,
    FOREIGN KEY (achievement_id) REFERENCES achievements(id),
    FOREIGN KEY (reward_id) REFERENCES rewards(id),
    FOREIGN KEY (value_translation_id) REFERENCES translations(id)
);

-- Tabla achievements_users
CREATE TABLE IF NOT EXISTS achievements_users (
    user_id BIGINT,
    achievement_id INTEGER,
    level INTEGER,
    updated_at TIMESTAMP WITHOUT TIME ZONE,
    PRIMARY KEY (user_id, achievement_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (achievement_id) REFERENCES achievements(id)
);

-- Tabla goals
CREATE TABLE IF NOT EXISTS goals (
    id INTEGER PRIMARY KEY,
    name_translation_id INTEGER,
    condition VARCHAR(255),
    evaluation VARCHAR(255),
    timestamp INTEGER,
    group_by_key BOOLEAN,
    group_by_dateformat VARCHAR(255),
    goal DOUBLE PRECISION,
    operator VARCHAR(10),
    maxmin VARCHAR(10),
    achievement_id INTEGER,
    priority INTEGER,
    FOREIGN KEY (name_translation_id) REFERENCES translations(id),
    FOREIGN KEY (achievement_id) REFERENCES achievements(id)
);

-- Tabla goals_goalproperties
CREATE TABLE IF NOT EXISTS goals_goalproperties (
    id INTEGER PRIMARY KEY,
    goal_id INTEGER,
    property_id INTEGER,
    value_translation_id INTEGER,
    from_level INTEGER,
    FOREIGN KEY (goal_id) REFERENCES goals(id),
    FOREIGN KEY (property_id) REFERENCES properties(id),
    FOREIGN KEY (value_translation_id) REFERENCES translations(id)
);

-- Tabla goals_properties
CREATE TABLE IF NOT EXISTS goals_properties (
    id INTEGER PRIMARY KEY,
    goal_id INTEGER,
    property_id INTEGER,
    value_translation_id INTEGER,
    from_level INTEGER,
    FOREIGN KEY (goal_id) REFERENCES goals(id),
    FOREIGN KEY (property_id) REFERENCES properties(id),
    FOREIGN KEY (value_translation_id) REFERENCES translations(id)
);

-- Tabla goal_triggers
CREATE TABLE IF NOT EXISTS goal_triggers (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    goal_id INTEGER,
    is_active BOOLEAN,
    FOREIGN KEY (goal_id) REFERENCES goals(id)
);

-- Tabla goal_trigger_steps
CREATE TABLE IF NOT EXISTS goal_trigger_steps (
    id INTEGER PRIMARY KEY,
    goal_trigger_id INTEGER,
    step_order INTEGER,
    condition_expression VARCHAR(255),
    FOREIGN KEY (goal_trigger_id) REFERENCES goal_triggers(id)
);

-- Tabla goal_trigger_executions
CREATE TABLE IF NOT EXISTS goal_trigger_executions (
    id BIGINT PRIMARY KEY,
    user_id BIGINT,
    trigger_id INTEGER,
    execution_date TIMESTAMP WITHOUT TIME ZONE,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (trigger_id) REFERENCES goal_triggers(id)
);
