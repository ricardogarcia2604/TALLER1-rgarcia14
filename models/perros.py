from config.db import db


class Perros(db.Model):
    __tablename__ = "Perros" 
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50), nullable =True)
    raza = db.Column(db.String(50), nullable=True)
    edad = db.Column(db.Integer, nullable=True)
    peso = db.Column(db.Float, nullable=True)
    id_cuidador = db.Column(db.Integer, db.ForeignKey("cuidadores.id"), nullable=False)
