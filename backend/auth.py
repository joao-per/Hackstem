from flask import jsonify, request

from database import db
from create_table import app
from models import User, UserToken
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

# Endpoints for Authentication

@app.route('/auth/register', methods=['POST'])
def register_user():
    data = request.json
    # Check if the username already exists
    existing_user = User.query.filter_by(username=data['username']).first()
    if existing_user:
        return jsonify({'error': 'Username already exists'}), 400

    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], email=data['email'],password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/auth/login', methods=['POST'])
def login_user():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        # Create a JWT token and store it in the database
        token = bcrypt.generate_password_hash(data['username']).decode('utf-8')
        new_user_token = UserToken(user_id=user.id, token=token)
        db.session.add(new_user_token)
        db.session.commit()
        return jsonify({'token': token}), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401

@app.route('/auth/validate-token', methods=['POST'])
def validate_token():
    data = request.json
    user_token = UserToken.query.filter_by(token=data['token']).first()
    if user_token:
        return jsonify({'message': 'Token is valid'}), 200
    else:
        return jsonify({'error': 'Invalid token'}), 401

@app.route('/test_db')
def test_db():
    try:
        # Try to query the database
        users = User.query.all()
        return 'Database connectivity test successful!'
    except Exception as e:
        return f'Database connectivity test failed: {str(e)}'