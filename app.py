from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import insert, select
from flask_restful import Api
from config.config import Config
from config.db import db
from config.auth import login_manager
from views.cuidadores_controller import CuidadoresController
from views.perros_controller import PerrosController
from models.cuidadores import Cuidadores
from models.perros import Perros
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from models.usuario import Usuario



app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
api = Api(app)
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

@app.route("/Login")
def Login():
    return render_template('Login.html')

@app.route("/auth")
def auth():
    username = request.args.get("username")
    password = request.args.get("password")
    user = Usuario.query.filter_by(username =username, password = password).first()
    if user:
        login_user(user)
        if current_user.es_admin:
            count = db.session.query(Perros).filter(Perros.nombre == "Lassie").count()

            return f"Hay {count} perros llamados Lassie"
        else:
            return render_template("ingreso.html")

@app.route("/auth/profile")
@login_required
def auth_profile():
    return f'datos : {current_user.username}'


@app.route("/Logout")
def logout():
    logout_user()
    return render_template("logout.html")


@app.route("/")
def home():
    count = db.session.query(Perros).filter(Perros.nombre == "Lassie").count()

    return f"Hay {count} perros llamados Lassie"

api.add_resource(CuidadoresController,'/Cuidadores')

api.add_resource(PerrosController,'/perros')


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        if not Cuidadores.query.first():
            insert_cuidadores = insert(Cuidadores).values([
                {"id" : 1 ,"nombre": "Juan Perez", "telefono": "555-1112233"},
                {"id" : 2 ,"nombre": "Ana Gomez", "telefono": "555-2223344"},
                {"id" : 3 ,"nombre": "Pedro Rodriguez", "telefono": "555-3334455"},
                {"id" : 4 ,"nombre": "Lucia Martinez", "telefono": "555-4445566"},
                {"id" : 5 ,"nombre": "Maria Lopez", "telefono": "555-5556677"},
                {"id" : 6 ,"nombre": "Antonio Ruiz", "telefono": "555-6667788"},
                {"id" : 7 ,"nombre": "Sofia Diaz", "telefono": "555-7778899"},
                {"id" : 8 ,"nombre": "Raul Garcia", "telefono": "555-8889900"},
                {"id" : 9 ,"nombre": "Carlos Fernandez", "telefono": "555-9990011"},
                {"id" : 10 ,"nombre": "Elena Sanchez", "telefono": "555-1011122"},
                {"id" : 11 ,"nombre": "Alba Navarro", "telefono": "555-2122233"},
                {"id" : 12 ,"nombre": "David Torres", "telefono": "555-3233344"},
                {"id" : 13 ,"nombre": "Ines Lopez", "telefono": "555-4344455"},
                {"id" : 14 ,"nombre": "Jose Gomez", "telefono": "555-5455566"},
                {"id" : 15 ,"nombre": "Patricia Jimenez", "telefono": "555-6566677"},
                {"id" : 16 ,"nombre": "Mario Lopez", "telefono": "555-6566679"}
                ])
            db.session.execute(insert_cuidadores)
            db.session.commit() 
            print("Cuidadores insertados correctamente")
        
        if not Usuario.query.first():
            insert_Usuario = insert(Usuario).values([
                {"id" : 1007671455 ,"username": "Rick", "password": "1111", "es_admin" : True},
                {"id" : 2 ,"username": "Ana Gomez", "password": "5552", "es_admin" : False},
                {"id" : 3 ,"username": "Pedro Rodriguez", "password": "5553", "es_admin" : False},
                {"id" : 4 ,"username": "Lucia Martinez", "password": "5554", "es_admin" : False},
                    ])
            db.session.execute(insert_Usuario )
            db.session.commit() 
            print("Cuidadores insertados correctamente")


        if not Perros.query.first():
            insert_perros = insert(Perros).values([
                {"nombre": "Rex", "raza": "Labrador", "edad": 2, "peso": 35, "id_cuidador": 12},
                {"nombre": "Simba", "raza": "Golden Retriever", "edad": 9, "peso": 20, "id_cuidador": 11},
                {"nombre": "Nina", "raza": "Bulldog", "edad": 7, "peso": 10, "id_cuidador": 14},
                {"nombre": "Bruno", "raza": "Pastor Alemán", "edad": 3, "peso": 15, "id_cuidador": 12},
                {"nombre": "Lola", "raza": "Golden Retriever", "edad": 6, "peso": 5, "id_cuidador": 9},
                {"nombre": "Milo", "raza": "Pastor Alemán", "edad": 8, "peso": 35, "id_cuidador": 4},
                {"nombre": "Chispa", "raza": "Poodle", "edad": 3, "peso": 35, "id_cuidador": 3},
                {"nombre": "Teo", "raza": "Labrador", "edad": 6, "peso": 5, "id_cuidador": 15},
                {"nombre": "Maxi", "raza": "Bulldog", "edad": 7, "peso": 15, "id_cuidador": 12},
                {"nombre": "Fiona", "raza": "Golden Retriever", "edad": 6, "peso": 1, "id_cuidador": 16},
                {"nombre": "Bobby", "raza": "Pastor Alemán", "edad": 4, "peso": 15, "id_cuidador": 8},
                {"nombre": "Lassie", "raza": "Pastor Alemán", "edad": 6, "peso": 30, "id_cuidador": 8},
                {"nombre": "Toby", "raza": "Poodle", "edad": 6, "peso": 25, "id_cuidador": 2},
                {"nombre": "Luky", "raza": "Golden Retriever", "edad": 3, "peso": 5, "id_cuidador": 6},
                {"nombre": "Chester", "raza": "Bulldog", "edad": 5, "peso": 15, "id_cuidador": 2},
                {"nombre": "Sasha", "raza": "Golden Retriever", "edad": 3, "peso": 10, "id_cuidador": 5},
                {"nombre": "Lassie", "raza": "Poodle", "edad": 2, "peso": 25, "id_cuidador": 3},
                {"nombre": "Tommy", "raza": "Pastor Alemán", "edad": 7, "peso": 10, "id_cuidador": 5},
                {"nombre": "Oso", "raza": "Pastor Alemán", "edad": 5, "peso": 15, "id_cuidador": 3},
                {"nombre": "Luna", "raza": "Poodle", "edad": 6, "peso": 35, "id_cuidador": 9},
                {"nombre": "Balto", "raza": "Beagle", "edad": 4, "peso": 30, "id_cuidador": 14},
                {"nombre": "Nala", "raza": "Golden Retriever", "edad": 3, "peso": 2, "id_cuidador": 16},
                {"nombre": "Rocky", "raza": "Poodle", "edad": 8, "peso": 15, "id_cuidador": 6},
                {"nombre": "Kira", "raza": "Pastor Alemán", "edad": 9, "peso": 30, "id_cuidador": 12},
                {"nombre": "Sam", "raza": "Bulldog", "edad": 10, "peso": 30, "id_cuidador": 15},
                {"nombre": "Maya", "raza": "Golden Retriever", "edad": 9, "peso": 15, "id_cuidador": 9},
                {"nombre": "Duke", "raza": "Pastor Alemán", "edad": 5, "peso": 2, "id_cuidador": 16},
                {"nombre": "Choco", "raza": "Beagle", "edad": 8, "peso": 35, "id_cuidador": 15},
                {"nombre": "Rocco", "raza": "Poodle", "edad": 4, "peso": 25, "id_cuidador": 4},
                {"nombre": "Gala", "raza": "Labrador", "edad": 5, "peso": 35, "id_cuidador": 10},
                {"nombre": "Lassie", "raza": "Pastor Alemán", "edad": 3, "peso": 30, "id_cuidador": 12}
            ])
            db.session.execute(insert_perros) 
            db.session.commit()  
            print("Perros insertados correctamente")

      
            
    app.run(debug=True)