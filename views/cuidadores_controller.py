from flask import make_response
from flask_restful import Resource
from models.cuidadores import Cuidadores

class CuidadoresController(Resource):
    def get(self):
        guarderias_list = Cuidadores.query.all()
        for guarderia in guarderias_list:
            print(guarderia.nombre)
        return make_response("Hola cuidadores")