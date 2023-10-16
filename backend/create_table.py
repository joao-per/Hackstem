from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database import db
    
app = Flask(__name__)
    
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'


with app.app_context():
    db.init_app(app)
    # Added this import just beore create_all
    from models import User, UserToken
    db.create_all()
    db.session.commit()