from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

class AccountHolder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120))
    username = db.Column(db.String(80))
    phone = db.Column(db.String(11))
    password = db.Column(db.String(140))
    def __init__(self,username,password,email,phone):
        self.username = username
        self.email = email
        self.phone = phone
        self.password = password

    def __repr__(self):
        return '<AccountHolder %r>' % self.username

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    phone = db.Column(db.String(11))
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))

    def __init__(self, username, email,phone,name):
        self.username = username
        self.email = email
        self.name = name
        self.phone = phone

    def __repr__(self):
        return '<User %r>' % self.username
