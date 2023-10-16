from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from database import db
from create_table import app
import os

load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)

from models import User, UserToken
from auth import *


def create_tables():
    with app.app_context():
        db.create_all()
        print('Tables created successfully!')

@app.route('/test')
def hello_world():
    data = {
        'name': 'John Doe',
        'age': 25,
        'city': 'Example City'
    }
    return jsonify(data)

if __name__ == '__main__':
    create_tables()
    
    app.run(debug=True)
