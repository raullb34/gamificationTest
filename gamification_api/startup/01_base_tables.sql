-- Tabla users
CREATE TABLE IF NOT EXISTS users (
    id BIGINT PRIMARY KEY,
    lat DOUBLE PRECISION,
    lon DOUBLE PRECISION,
    timezone VARCHAR(50),
    country VARCHAR,
    region VARCHAR,
    city VARCHAR,
    additional_public_data JSON,
    created_at TIMESTAMP WITHOUT TIME ZONE
);

-- Tabla rewards
CREATE TABLE IF NOT EXISTS rewards (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255)
);

-- Tabla languages
CREATE TABLE IF NOT EXISTS languages (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255)
);

-- Tabla translationvariables
CREATE TABLE IF NOT EXISTS translationvariables (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255)
);

-- Tabla user_groups
CREATE TABLE IF NOT EXISTS user_groups (
    id BIGINT PRIMARY KEY,
    name VARCHAR(255)
);
