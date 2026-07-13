--TABLA PERFILES
CREATE TABLE IF NOT EXISTS perfiles(
    id VARCHAR(255) PRIMARY KEY, --PK
    fecha_creacion TIMESTAMP,
    ultimo_acceso TIMESTAMP
);

--TABLA REDIRECCIONES
CREATE TABLE IF NOT EXISTS redirecciones(
    url_origen VARCHAR(255),
    codigo VARCHAR(255) PRIMARY KEY--PK
);

--TABLA VISITAS
CREATE TABLE IF NOT EXISTS visitas(
    id VARCHAR(255) PRIMARY KEY, --PK
    id_perfil VARCHAR(255), --FK
    codigo_redireccion VARCHAR(255), --FK
    marca_temporal TIMESTAMP,
    CONSTRAINT fk_id_perfil FOREIGN KEY(id_perfil) REFERENCES perfiles(id),
    CONSTRAINT fk_codigo_temporal FOREIGN KEY(codigo_redireccion) REFERENCES redirecciones(codigo)
);