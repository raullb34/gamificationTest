-- Tabla auth_users
CREATE TABLE IF NOT EXISTS auth_users (
    id BIGINT PRIMARY KEY,
    username VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(255)
);

-- Tabla auth_roles
CREATE TABLE IF NOT EXISTS auth_roles (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100)
);

-- Tabla auth_role_permissions
CREATE TABLE IF NOT EXISTS auth_role_permissions (
    id INTEGER PRIMARY KEY,
    role_id INTEGER,
    permission VARCHAR(100),
    FOREIGN KEY (role_id) REFERENCES auth_roles(id)
);

-- Tabla auth_tokens
CREATE TABLE IF NOT EXISTS auth_tokens (
    id BIGINT PRIMARY KEY,
    user_id BIGINT,
    token VARCHAR(255),
    expires_at TIMESTAMP WITHOUT TIME ZONE,
    FOREIGN KEY (user_id) REFERENCES auth_users(id)
);

-- Tabla auth_users_roles
CREATE TABLE IF NOT EXISTS auth_users_roles (
    user_id BIGINT,
    role_id INTEGER,
    PRIMARY KEY (user_id, role_id),
    FOREIGN KEY (user_id) REFERENCES auth_users(id),
    FOREIGN KEY (role_id) REFERENCES auth_roles(id)
);
