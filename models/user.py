#this is an api
import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)#auto assign the id
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password): #using _id because id is a key word for python
        self.username = username
        self.password = password

    def save_to_db(self):#update and insert
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
