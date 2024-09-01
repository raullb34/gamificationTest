# Gamification API

Esta API de Gamificación permite gestionar usuarios, logros, objetivos, variables, dispositivos, y mucho más. Está diseñada para integrarse en sistemas que requieren características de gamificación, como recompensas, niveles, seguimiento de objetivos, etc. A continuación se detallan las entidades de la base de datos y su funcionalidad dentro de la API.

## Índice
- [Entidades Principales](#entidades-principales)
- [Entidades de Traducción y Propiedades](#entidades-de-traducción-y-propiedades)
- [Entidades de Logros y Objetivos](#entidades-de-logros-y-objetivos)
- [Entidades de Variables y Valores](#entidades-de-variables-y-valores)
- [Entidades de Autenticación y Roles](#entidades-de-autenticación-y-roles)
- [Entidades Misceláneas](#entidades-misceláneas)
- [Cómo Usar la API](#cómo-usar-la-api)

## Entidades Principales

### 1. users
- **Descripción:** Almacena información sobre los usuarios.
- **Campos:** id, lat, lon, timezone, country, region, city, additional_public_data, created_at
- **Funcionalidad en la API:**
  - **Crear/Actualizar Usuario:** Permite añadir o actualizar un usuario con su información de localización y datos adicionales.
  - **Consultar Usuario:** Recupera la información del usuario, incluyendo su progreso en logros y variables.

### 2. rewards
- **Descripción:** Define los diferentes tipos de recompensas que se pueden otorgar a los usuarios.
- **Campos:** id, name
- **Funcionalidad en la API:**
  - **Consultar Recompensas:** Permite listar las recompensas disponibles.

### 3. languages
- **Descripción:** Almacena los idiomas disponibles para las traducciones.
- **Campos:** id, name
- **Funcionalidad en la API:**
  - **Gestión de Idiomas:** Listar los idiomas disponibles para las traducciones.

### 4. translationvariables
- **Descripción:** Representa las variables que pueden ser traducidas a diferentes idiomas.
- **Campos:** id, name
- **Funcionalidad en la API:**
  - **Consultar Variables de Traducción:** Listar las variables que tienen traducciones disponibles.

### 5. user_groups
- **Descripción:** Define grupos de usuarios.
- **Campos:** id, name
- **Funcionalidad en la API:**
  - **Gestión de Grupos de Usuarios:** Crear, actualizar y eliminar grupos de usuarios.

## Entidades de Traducción y Propiedades

### 6. translations
- **Descripción:** Contiene las traducciones de diferentes variables en varios idiomas.
- **Campos:** id, translationvariable_id, language_id, text
- **Funcionalidad en la API:**
  - **Gestión de Traducciones:** Añadir o actualizar traducciones para diferentes variables.

### 7. properties
- **Descripción:** Define propiedades que pueden estar asociadas a logros y objetivos.
- **Campos:** id, name, is_variable
- **Funcionalidad en la API:**
  - **Gestión de Propiedades:** Listar y gestionar propiedades para logros y objetivos.

### 8. achievementproperties
- **Descripción:** Asocia propiedades con logros.
- **Campos:** id, achievement_id, property_id
- **Funcionalidad en la API:**
  - **Gestión de Propiedades de Logros:** Consultar las propiedades asociadas a un logro específico.

### 9. goalproperties
- **Descripción:** Asocia propiedades con objetivos.
- **Campos:** id, goal_id, property_id
- **Funcionalidad en la API:**
  - **Gestión de Propiedades de Objetivos:** Consultar las propiedades asociadas a un objetivo específico.

## Entidades de Logros y Objetivos

### 10. achievements
- **Descripción:** Almacena información sobre los logros disponibles en la plataforma.
- **Campos:** id, name, maxlevel, valid_start, valid_end, hidden, relevance, evaluation_timezone, view_permission
- **Funcionalidad en la API:**
  - **Gestión de Logros:** Crear, actualizar y consultar logros.

### 11. achievements_rewards
- **Descripción:** Relaciona logros con recompensas específicas.
- **Campos:** id, achievement_id, reward_id, value, value_translation_id, from_level
- **Funcionalidad en la API:**
  - **Asignación de Recompensas a Logros:** Definir qué recompensas se otorgan por alcanzar un logro.

### 12. achievements_users
- **Descripción:** Almacena los logros alcanzados por los usuarios.
- **Campos:** user_id, achievement_id, level, updated_at
- **Funcionalidad en la API:**
  - **Gestión de Logros de Usuarios:** Consultar y actualizar el progreso de los logros de los usuarios.

### 13. goals
- **Descripción:** Define objetivos que los usuarios deben alcanzar para conseguir logros.
- **Campos:** id, name_translation_id, condition, evaluation, timestamp, group_by_key, group_by_dateformat, goal, operator, maxmin, achievement_id, priority
- **Funcionalidad en la API:**
  - **Gestión de Objetivos:** Crear, actualizar y consultar objetivos.

### 14. goals_goalproperties
- **Descripción:** Relaciona propiedades con objetivos específicos.
- **Campos:** id, goal_id, property_id, value_translation_id, from_level
- **Funcionalidad en la API:**
  - **Gestión de Propiedades de Objetivos:** Consultar propiedades relacionadas con objetivos.

### 15. goals_properties
- **Descripción:** Asocia propiedades con objetivos.
- **Campos:** id, goal_id, property_id, value_translation_id, from_level
- **Funcionalidad en la API:**
  - **Gestión de Propiedades de Objetivos:** Listar propiedades relacionadas con objetivos.

### 16. goal_triggers
- **Descripción:** Define los disparadores de objetivos.
- **Campos:** id, name, goal_id, is_active
- **Funcionalidad en la API:**
  - **Gestión de Disparadores de Objetivos:** Crear y gestionar disparadores de objetivos.

### 17. goal_trigger_steps
- **Descripción:** Define los pasos para los disparadores de objetivos.
- **Campos:** id, goal_trigger_id, step_order, condition_expression
- **Funcionalidad en la API:**
  - **Gestión de Pasos de Disparadores de Objetivos:** Crear y gestionar los pasos de los disparadores.

### 18. goal_trigger_executions
- **Descripción:** Registra las ejecuciones de los disparadores de objetivos.
- **Campos:** id, user_id, trigger_id, execution_date
- **Funcionalidad en la API:**
  - **Registro de Ejecuciones de Disparadores:** Registrar cuando un disparador es ejecutado.

## Entidades de Variables y Valores

### 19. variables
- **Descripción:** Define variables que pueden ser utilizadas para medir el progreso de los usuarios.
- **Campos:** id, name, name_translation_id, is_reward
- **Funcionalidad en la API:**
  - **Gestión de Variables:** Crear, actualizar y consultar variables.

### 20. values
- **Descripción:** Almacena valores de las variables para los usuarios.
- **Campos:** user_id, datetime, variable_id, value, key
- **Funcionalidad en la API:**
  - **Gestión de Valores de Variables:** Crear, actualizar y consultar valores de variables para usuarios.

## Entidades de Autenticación y Roles

### 21. auth_users
- **Descripción:** Contiene la información de autenticación de los usuarios.
- **Campos:** id, username, email, password
- **Funcionalidad en la API:**
  - **Gestión de Usuarios:** Crear, actualizar y autenticar usuarios.

### 22. auth_roles
- **Descripción:** Define roles que pueden ser asignados a usuarios.
- **Campos:** id, name
- **Funcionalidad en la API:**
  - **Gestión de Roles:** Crear, actualizar y consultar roles.

### 23. auth_role_permissions
- **Descripción:** Define permisos para los roles.
- **Campos:** id, role_id, permission
- **Funcionalidad en la API:**
  - **Gestión de Permisos de Roles:** Asignar y gestionar permisos para roles.

### 24. auth_tokens
- **Descripción:** Almacena los tokens de autenticación de los usuarios.
- **Campos:** id, user_id, token, expires_at
- **Funcionalidad en la API:**
  - **Gestión de Tokens de Autenticación:** Crear, actualizar y consultar tokens de autenticación.

### 25. auth_users_roles
- **Descripción:** Relaciona usuarios con roles.
- **Campos:** user_id, role_id
- **Funcionalidad en la API:**
  - **Asignación de Roles a Usuarios:** Asignar y gestionar roles para usuarios.

## Entidades Misceláneas

### 26. user_devices
- **Descripción:** Almacena información sobre los dispositivos de los usuarios.
- **Campos:** user_id, device_id, push_id, device_os, app_version
- **Funcionalidad en la API:**
  - **Gestión de Dispositivos de Usuarios:** Registrar y gestionar los dispositivos asociados a los usuarios.

### 27. user_messages
- **Descripción:** Almacena los mensajes de los usuarios.
- **Campos:** user_id, message_id, is_read
- **Funcionalidad en la API:**
  - **Gestión de Mensajes de Usuarios:** Consultar y marcar mensajes como leídos.

### 28. goal_evaluation_cache
- **Descripción:** Almacena caché de las evaluaciones de objetivos para los usuarios.
- **Campos:** goal_id, user_id, achieved, value
- **Funcionalidad en la API:**
  - **Gestión de Caché de Evaluación de Objetivos:** Optimizar el rendimiento de las evaluaciones de objetivos.

### 29. denials
- **Descripción:** Almacena relaciones de denegación entre entidades.
- **Campos:** from_id, to_id
- **Funcionalidad en la API:**
  - **Gestión de Denegaciones:** Definir y consultar relaciones de denegación.

### 30. requirements
- **Descripción:** Almacena relaciones de requisitos entre entidades.
- **Campos:** from_id, to_id
- **Funcionalidad en la API:**
  - **Gestión de Requisitos:** Definir y consultar relaciones de requisitos.

### 31. auth_users_roles
- **Descripción:** Asocia usuarios con roles específicos.
- **Campos:** user_id, role_id
- **Funcionalidad en la API:**
  - **Asignación de Roles:** Definir qué roles tienen los usuarios.

## Cómo Usar la API

La API proporciona un conjunto de endpoints que permiten gestionar todas estas entidades. Puedes interactuar con la API utilizando herramientas como Postman o cURL para probar los endpoints.

- **Crear Usuario:** `POST /add_or_update_subject/{user_id}`
- **Consultar Logros de Usuario:** `GET /progress/{user_id}`
- **Autenticación de Usuario:** `POST /auth/login`
- **Registrar Dispositivo:** `POST /register_device/{user_id}`
- **Gestión de Roles y Permisos:** `POST /auth/roles`

Cada entidad y su endpoint correspondiente están diseñados para facilitar la integración de gamificación en aplicaciones y sistemas de gestión de usuarios.
