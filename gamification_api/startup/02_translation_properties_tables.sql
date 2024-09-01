-- Tabla translations
CREATE TABLE IF NOT EXISTS translations (
    id INTEGER PRIMARY KEY,
    translationvariable_id INTEGER,
    language_id INTEGER,
    text VARCHAR(255),
    FOREIGN KEY (translationvariable_id) REFERENCES translationvariables(id),
    FOREIGN KEY (language_id) REFERENCES languages(id)
);

-- Tabla properties
CREATE TABLE IF NOT EXISTS properties (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255),
    is_variable BOOLEAN
);

-- Tabla achievementproperties
CREATE TABLE IF NOT EXISTS achievementproperties (
    id INTEGER PRIMARY KEY,
    achievement_id INTEGER,
    property_id INTEGER,
    FOREIGN KEY (achievement_id) REFERENCES achievements(id),
    FOREIGN KEY (property_id) REFERENCES properties(id)
);

-- Tabla goalproperties
CREATE TABLE IF NOT EXISTS goalproperties (
    id INTEGER PRIMARY KEY,
    goal_id INTEGER,
    property_id INTEGER,
    FOREIGN KEY (goal_id) REFERENCES goals(id),
    FOREIGN KEY (property_id) REFERENCES properties(id)
);
