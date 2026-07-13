#IMPORTACIÓN DE LIBRERÍAS
from flask import Flask # Es la clase principal de Flask. Con ella se crea la aplicación web
from flask import render_template # Permite mostrar páginas HTML que se encuentran dentro de la carpeta templates
from flask import request # Sirve para acceder a los datos que envía un formulario
from flask import abort
from flask import redirect
from models import Redirecciones # Importa la clase Redireccion, definida en models.py
import secrets # Es una librería de Python que genera cadenas aleatorias y seguras
from config import APP_BASE_URL




# Crea la aplicación Flask
app = Flask(__name__)

# Static files
app.static_folder = 'static'
app.static_url_path = '/static'


# 1.EL USUARIO ENTRA EN LA PÁGINA
@app.get('/')# Cuando el usuario visite la dirección / mediante una petición GET, ejecuta la función siguiente.
def index():# Creamos la función que muestra la página principal
    return render_template('crear_shortlink.html', app_base_url=APP_BASE_URL) # devuelve la plantilla


# 2.GUARDAMOS EL URL EN LA DB
@app.post('/') # El formulario se envía por POST
def create_shortlink():
    url = request.form['url']# cogemos la url del formulario
    clave = secrets.token_urlsafe(8) # Genera un código único para cada url
    codigo = f"bifrost/{clave}"
    direccion_url = Redirecciones(url=url, codigo=codigo) # Crea un objeto 'direccion_url' 
    direccion_url.save() # Guarda la url en la base de datos
    return render_template('crear_shortlink.html', direccion_url=direccion_url, app_base_url=APP_BASE_URL) #devuelve la plantilla


# 3. COGEMOS EL CÓDIGO DE LA URL A TRAVÉS DEL MÉTODO GET
@app.get('/bifrost/<codigo>')
def redirect_to_url(codigo):
    url_corta = f"bifrost/{codigo}"
    
    redir = Redirecciones.get(url_corta)
    if redir is None:
        abort(404)
    else:
        return redirect(redir)

        

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404