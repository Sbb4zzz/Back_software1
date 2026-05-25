# Mundial 2026 Hub - Backend API

Este repositorio contiene el **backend** del ecosistema **Mundial 2026 Hub**. Es una API REST desarrollada en Python con Flask siguiendo la arquitectura MVC (Model-View-Controller), diseñada para gestionar la persistencia de datos, la seguridad de usuarios y la sincronización de módulos para una aplicación de alto rendimiento.

## Arquitectura MVC

El proyecto está organizado siguiendo el patrón de arquitectura MVC:

```
back_world_sync/
├── app.py                 # Aplicación principal (entry point)
├── config.py             # Configuración centralizada
├── models/               # Capa de Modelos (lógica de datos)
│   ├── user.py          # Modelo de usuarios
│   ├── match.py         # Modelo de partidos
│   ├── poll.py          # Modelo de encuestas
│   ├── album.py         # Modelo de álbum
│   └── ticket.py        # Modelo de entradas
├── controllers/          # Capa de Controladores (lógica de negocio)
│   ├── user_controller.py
│   ├── match_controller.py
│   ├── poll_controller.py
│   ├── album_controller.py
│   └── ticket_controller.py
├── routes/               # Capa de Rutas (endpoints)
│   └── api.py           # Definición de rutas API
├── utils/                # Utilidades compartidas
│   ├── database.py      # Conexión a BD
│   └── logging_utils.py # Utilidades de logging
└── requirements.txt      # Dependencias del proyecto
```

## Stack Tecnológico
* **Framework:** Flask 3.x (Python)
* **Base de Datos:** MySQL (Relacional) - Puerto 3307 (XAMPP)
* **Seguridad:** Hashing de contraseñas con `Werkzeug`, UUID4 para identificadores
* **Middleware:** Flask-CORS habilitado para integración con Angular (Puerto 4200)
* **Logging:** Estructurado para trazabilidad y auditoría
* **Arquitectura:** MVC (Model-View-Controller)

## Instalación y Configuración

### 1. Clonar el repositorio
```bash
git clone https://github.com/yerso/back_world_sync.git
cd back_world_sync
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Configurar Base de Datos
- Asegúrate de tener XAMPP corriendo en puerto 3307
- Ejecuta el script SQL `mundial_2026_hub.sql` en phpMyAdmin
- Ejecuta `python populate.py` para datos de ejemplo

### 4. Ejecutar la aplicación
```bash
python app.py
```
La API estará disponible en `http://localhost:5001`

## API Endpoints

Todos los endpoints están bajo el prefijo `/api/`.

### Gestión de Usuarios

#### POST /api/login
Autentica un usuario
```json
{
  "email": "juan@example.com",
  "password": "password123"
}
```

#### POST /api/register
Registra un nuevo usuario
```json
{
  "nombre": "Juan Pérez",
  "email": "juan@example.com",
  "password": "password123",
  "rol": "aficionado"
}
```

#### GET /api/profile
Obtiene el perfil del usuario actual

### Agenda de Partidos

#### GET /api/matches
Obtiene todos los partidos disponibles

### Módulo de Pollas

#### GET /api/polls/groups
Lista todos los grupos de pollas disponibles

#### POST /api/polls/groups
Crea un nuevo grupo de polla
```json
{
  "nombre_grupo": "Grupo Amigos",
  "creador_id": "uuid-del-usuario"
}
```

#### GET /polls/groups/{id}/rankings
Obtiene el ranking de puntos de un grupo específico

#### POST /polls/predictions
Registra un pronóstico
```json
{
  "usuario_id": "uuid-del-usuario",
  "partido_id": 1,
  "grupo_id": 1,
  "goles_a": 2,
  "goles_b": 1
}
```

### Álbum Digital

#### POST /album/buy-pack
Compra y abre un paquete de láminas

#### GET /album/collection
Obtiene la colección completa del usuario

### Gestión de Entradas

#### GET /tickets/available
Obtiene entradas disponibles para un partido

#### POST /tickets/{id}/reserve
Reserva una entrada específica

#### POST /tickets/{id}/pay
Confirma el pago de una entrada reservada

#### GET /tickets/my-tickets
Obtiene las entradas del usuario actual

#### POST /album/abrir-paquete/{usuario_id}
Abrir un paquete de 5 láminas aleatorias

#### GET /album/coleccion/{usuario_id}
Obtener colección completa del usuario

#### POST /album/intercambiar
Realizar intercambio de láminas entre usuarios
```json
{
  "usuario_origen": "uuid-origen",
  "usuario_destino": "uuid-destino",
  "lamina_origen": 1,
  "lamina_destino": 2
}
```

### Gestión de Entradas

#### GET /entradas/disponibles/{partido_id}
Obtener entradas disponibles para un partido

#### POST /entradas/reservar
Reservar una entrada (TTL: 15 minutos)
```json
{
  "entrada_id": "ENT-1-001",
  "usuario_id": "uuid-del-usuario"
}
```

#### POST /entradas/pagar
Confirmar pago de entrada reservada
```json
{
  "entrada_id": "ENT-1-001",
  "usuario_id": "uuid-del-usuario",
  "hash_auditoria": "uuid-hash"
}
```

#### GET /entradas/mis-entradas/{usuario_id}
Obtener entradas del usuario

#### POST /entradas/procesar-expiradas
Procesar reservas expiradas (para ejecutar periódicamente)

### Endpoints Adicionales

#### GET /partidos
Obtener todos los partidos

#### GET /auditoria/logs
Obtener logs de auditoría (requiere rol soporte)

#### PUT /partidos/{partido_id}/estado
Actualizar estado de partido (requiere rol operador)
```json
{
  "estado": "finalizado",
  "resultado_a": 2,
  "resultado_b": 1
}
```

## Funcionalidades Implementadas

✅ **RF-01:** Gestión de Usuarios (Registro, Login, Roles)
✅ **RF-02:** Agenda Personal
✅ **RF-03:** Módulo de Pollas (Grupos, Pronósticos, Ranking)
✅ **RF-04:** Álbum Digital (Paquetes, Colección, Intercambios)
✅ **RF-05:** Trazabilidad (Logs de auditoría completos)
✅ **RF-06:** Gestión de Entradas (Ciclo de vida con TTL)

## Requerimientos No Funcionales

✅ **Seguridad:** Hashing de contraseñas con Werkzeug
✅ **Disponibilidad:** Arquitectura preparada para graceful degradation
✅ **Observabilidad:** Logs estructurados para ELK/Splunk
✅ **Escalabilidad:** Arquitectura desacoplada Frontend/Backend

## Testing

Ejecuta las pruebas con:
```bash
python test_api.py
```

## Base de Datos

El esquema incluye las siguientes tablas principales:
- `usuarios`: Gestión de usuarios y roles
- `partidos`: Información de partidos
- `entradas`: Ciclo de vida de boletos
- `pollas_grupos`: Grupos de predicciones
- `pronosticos`: Pronósticos de usuarios
- `laminas`: Catálogo de láminas
- `coleccion_usuario`: Colección de láminas por usuario
- `eventos_log`: Auditoría completa de eventos

## Próximos Pasos

- Integración con APIs externas de datos deportivos
- Implementación de simulador de pagos (Stripe/Wiremock)
- Sistema de notificaciones push
- Optimización de rendimiento y caching

##  Gestión del Entorno (Virtual Environment)

### ¿Qué es el `venv`?
El **Virtual Environment (venv)** es una herramienta que crea un entorno aislado para el proyecto. Esto garantiza que las librerías instaladas (como Flask o mysql-connector) no entren en conflicto con otras versiones de Python instaladas en tu sistema. 

**Es una práctica estándar en ingeniería para asegurar que el proyecto sea reproducible en cualquier máquina.**

---

##  Guía de Instalación y Ejecución

Sigue estos pasos en tu terminal (CMD o PowerShell) dentro de la carpeta del proyecto:

### 1. Preparar el Entorno Virtual
Crea el entorno y actívalo para empezar a trabajar de forma aislada:
En la terminal o cmd 
# Crear el entorno virtual con flask (python)
python -m venv venv

# Activar el entorno (En Windows)
.\venv\Scripts\activate
