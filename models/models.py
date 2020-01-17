# importamos la instancia de la BD

from apptrivia import db

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(64), index=True, unique=True)
    # preguntas = db.relationship('Pregunta', backref='categoria', lazy='dynamic')

    def __repr__(self):
        return '<Categoria: {}>'.format(self.descripcion)

