from flask_sqlalchemy import SQLAlchemy
from database import db

# UserToken model
class UserToken(db.Model):
    __tablename__ = 'user_token'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    token = db.Column(db.String(100), unique=True, nullable=False)