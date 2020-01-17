from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# instancia Flask
app = Flask(__name__)

# lee la config desde el archivo config.py
app.config.from_pyfile('config.py')

# inicializa la base de datos con la config leida
db = SQLAlchemy(app)

# rutas disponibles
from routes import *

# subimos el server (solo cuando se llama directamente a este archivo)
if __name__ == '__main__':
    app.run()