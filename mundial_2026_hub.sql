
CREATE DATABASE IF NOT EXISTS mundial_2026_hub;
USE mundial_2026_hub;

-- 2. TABLA DE USUARIOS

CREATE TABLE usuarios (
    usuario_id VARCHAR(36) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    puntos_totales INT DEFAULT 0,
    saldo DECIMAL(12, 2) DEFAULT 0.00,
    rol ENUM('aficionado', 'operador', 'soporte') DEFAULT 'aficionado',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. TABLA DE PARTIDOS
CREATE TABLE partidos (
    partido_id INT AUTO_INCREMENT PRIMARY KEY,
    equipo_a VARCHAR(50) NOT NULL,
    equipo_b VARCHAR(50) NOT NULL,
    fecha_hora DATETIME NOT NULL,
    estadio VARCHAR(100) NOT NULL,
    ciudad VARCHAR(50) NOT NULL,
    fase VARCHAR(50), 
    estado ENUM('programado', 'en juego', 'finalizado') DEFAULT 'programado',
    resultado_a INT DEFAULT 0,
    resultado_b INT DEFAULT 0
);

-- 4. GESTIÓN DE ENTRADAS
CREATE TABLE entradas (
    entrada_id VARCHAR(36) PRIMARY KEY,
    partido_id INT,
    usuario_id VARCHAR(36),
    estado ENUM('Disponible', 'Reservada', 'Pagada', 'Transferida', 'Reembolsada', 'Expirada') DEFAULT 'Disponible',
    precio DECIMAL(10,2),
    reserva_expira_at DATETIME,
    hash_auditoria TEXT,
    FOREIGN KEY (partido_id) REFERENCES partidos(partido_id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id)
);

-- 5. MÓDULO DE POLLAS
CREATE TABLE pollas_grupos (
    grupo_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_grupo VARCHAR(100) NOT NULL,
    codigo_invitacion VARCHAR(10) UNIQUE NOT NULL,
    creador_id VARCHAR(36),
    FOREIGN KEY (creador_id) REFERENCES usuarios(usuario_id)
);

CREATE TABLE pronosticos (
    pronostico_id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id VARCHAR(36),
    partido_id INT,
    grupo_id INT,
    goles_a INT NOT NULL,
    goles_b INT NOT NULL,
    puntos_obtenidos INT DEFAULT 0,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY pronostico_unico (usuario_id, partido_id, grupo_id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id),
    FOREIGN KEY (partido_id) REFERENCES partidos(partido_id),
    FOREIGN KEY (grupo_id) REFERENCES pollas_grupos(grupo_id)
);

-- 6. MÓDULO DE ÁLBUM DIGITAL
CREATE TABLE laminas (
    lamina_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_jugador VARCHAR(255),
    seleccion VARCHAR(255),
    posicion VARCHAR(100),
    especial BOOLEAN DEFAULT FALSE,
    imagen_url TEXT
);

CREATE TABLE control_sobres (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT UNIQUE,
    sobres_abiertos INT DEFAULT 0,
    ultima_apertura DATE
);

CREATE TABLE coleccion_usuario (
    usuario_id VARCHAR(36),
    lamina_id INT,
    cantidad INT DEFAULT 1,
    PRIMARY KEY (usuario_id, lamina_id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id),
    FOREIGN KEY (lamina_id) REFERENCES laminas(lamina_id)
);

--  EVENTOS Y AUDITORÍA ANALITICA
CREATE TABLE eventos_log (
    evento_id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id VARCHAR(36),
    tipo_evento VARCHAR(50),
    descripcion TEXT,
    id_correlacion VARCHAR(36),
    metadata JSON,
    fecha_evento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id)
);
