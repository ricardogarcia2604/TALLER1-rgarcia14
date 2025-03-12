from flask import make_response
from flask_restful import Resource
from models.perros import Perros

class PerrosController(Resource):
    def get(self):
        guarderias_list = Perros.query.all()
        for guarderia in guarderias_list:
            print(guarderia.nombre)
        return make_response("Hola Soy perros")