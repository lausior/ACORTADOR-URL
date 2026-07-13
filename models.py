##IMPORTACIÓN LIBRERÍAS

# Importa la librería psycopg, que permite que Python se comunique con una base de datos PostgreSQL.
import psycopg 
# Importa el decorador @dataclass (Una dataclass es una forma sencilla de crear clases cuyos atributos solo almacenan datos)
from dataclasses import dataclass
# Importa la clase datetime, que sirve para trabajar con fechas y horas.
from datetime import datetime




#------------------------------------------------------------#

#CREACIÓN DE LA CONEXIÓN A LA DB
# Importa los datos de configuración necesarios para conectarse a la base de datos.
from config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER

# Función que establece una conexión con la base de datos PostgreSQL.
def get_db_connection():
        return psycopg.connect(f"host={DB_HOST} port={DB_PORT} dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD}")


#------------------------------------------------------------#

#CLASES Y QUERYS

# El decorador @dataclass genera automáticamente el constructor (__init__)

# CLASE PERFILES
@dataclass
class Perfiles:
    id: str # PK
    fecha_creacion: datetime
    ultimo_acceso: datetime

#INSERTAR DATOS EN LA DB
    def save(self): # self-> representa el objeto actual 
        with get_db_connection() as conn: # abre la conexión
            with conn.cursor() as cur: #crea el cursor para ejecutar las consultas
                 cur.execute("INSERT INTO perfiles (id, fecha_creacion, ultimo_acceso) VALUES (%s, %s, %s)", #ejecutamos la consulta SQL para insertar los datos de la nota en la tabla "notas"
                        (self.id, self.fecha_creacion, self.ultimo_acceso)) #sustituimos los valores de la nota



# CLASE REDIRECCIONES
# Creación clase
@dataclass
class Redirecciones:
    url: str 
    codigo: str # PK

#Insercción datos en la DB
    def save(self): # self-> representa el objeto actual 
        with get_db_connection() as conn: # abre la conexión
            with conn.cursor() as cur: # crea el cursor para ejecutar las consultas
                 cur.execute("INSERT INTO redirecciones (url, codigo) VALUES (%s, %s)", # ejecutamos la consulta SQL para insertar los datos de la nota en la tabla "notas"
                        (self.url, self.codigo)) # sustituimos los valores de la nota


    #Hace un select filtrando por el código de la url
    @staticmethod
    def get(codigo): # codigo-> busca una url utilizando su código 
        conn = get_db_connection() # abre la conexión
        with conn.cursor() as cur: #crea el cursor para ejecutar las consultas
            cur.execute("SELECT * FROM redirecciones WHERE codigo = %s", (codigo,))
            resultado = cur.fetchone() # devuelve la primera fila del resultado de la consulta
            if resultado is None:
                return None
            else:
                return resultado[0]



# CLASE VISITAS
# Creación clase
@dataclass
class Visitas:
    id: str # PK
    id_perfil: str  # FK
    codigo_redireccion: str # FK
    marca_temporal: datetime



#------------------------------------------------------------#








