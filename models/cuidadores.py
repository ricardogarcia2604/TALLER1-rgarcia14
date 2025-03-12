from config.db import db


class Cuidadores(db.Model):
    __tablename__ = "cuidadores" 
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50), nullable =True)
    telefono = db.Column(db.String(15), nullable=True)




