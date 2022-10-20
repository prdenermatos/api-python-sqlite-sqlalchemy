from flask_sqlalchemy import SQLAlchemy
from app import db


class data(db.Model):
    __tablename__ = "data"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __init__(self, nome, cpf, endereco, relato):
        self.name = nome

    def __repr__(self):
        return '<data %r>' % self.nome    


