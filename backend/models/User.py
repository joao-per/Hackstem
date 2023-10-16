from flask_sqlalchemy import SQLAlchemy
from database import db

# User model
class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    #participations = db.relationship('Participation', backref='user', lazy=True)
    #rewards = db.relationship('Reward', backref='user', lazy=True)
    #friends = db.relationship('Friendship', backref='user', lazy=True)
    #tokens = db.relationship('UserToken', backref='user', lazy=True)