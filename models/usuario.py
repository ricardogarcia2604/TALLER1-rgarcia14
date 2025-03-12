from config.db import db
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    __tablename__ = "usuarios" 
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True, nullable =False)
    password = db.Column(db.String(50), nullable =False)
    es_admin = db.Column(db.Boolean, nullable=False)
