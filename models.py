# Importa la librería psycopg, que permite que Python se comunique con una base de datos PostgreSQL.
import psycopg 

# Importa el decorador @dataclass (Una dataclass es una forma sencilla de crear clases cuyos atributos solo almacenan datos)
from dataclasses import dataclass

# Importa la clase datetime, que sirve para trabajar con fechas y horas.
from datetime import datetime

# Importa los datos de configuración necesarios para conectarse a la base de datos.
from config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER

# Función que establece una conexión con la base de datos PostgreSQL.
def get_db_connection():
        return psycopg.connect(f"host={DB_HOST} port={DB_PORT} dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD}")

# El decorador @dataclass genera automáticamente el constructor (__init__)
# Clase Perfiles
@dataclass
class Perfiles:
    id: str # PK
    fecha_creacion: str
    fecha_ultimo_acceso: datetime

# Clase Redirecciones
@dataclass
class Redirecciones:
    url_origen: str 
    codigo: str # PK

# Clase Visitas
@dataclass
class Visitas:
    id: str # PK
    id_perfil: str  # FK
    codigo_redireccion: str # FK
    marca_temporal: datetime





