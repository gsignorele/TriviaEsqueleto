#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apptrivia import db
from models.models import Categoria

db.drop_all()
db.create_all()
#categorias
c_geogra = Categoria(descripcion="Geografía")
c_deporte = Categoria(descripcion="Deportes")
db.session.add(c_geogra)
db.session.add(c_deporte)
db.session.commit()

