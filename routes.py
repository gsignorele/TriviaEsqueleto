# importamos la instancia de Flask (app)
from apptrivia import app

# importamos los modelos a usar
from models.models import Categoria

from flask import render_template

@app.route('/trivia')
def index():
    return "<h2>hola Trivia</h2>"

@app.route('/trivia/categorias')
def mostrarcategorias():
    categorias = Categoria.query.all()
    return render_template('categorias.html', categorias=categorias)

