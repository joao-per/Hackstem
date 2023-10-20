from flask import jsonify, request, current_app, Blueprint
from flask_bcrypt import Bcrypt
import sqlite3

auth_bp = Blueprint('auth', __name__)
bcrypt = Bcrypt()

def create_user(username, email, password):
	hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

	with current_app.app_context():
		conn = sqlite3.connect(current_app.config['DATABASE'])
		cursor = conn.cursor()

		cursor.execute('''
			SELECT * FROM user
			WHERE username = ?
		''', (username,))

		user = cursor.fetchone()
		if user is not None:
			conn.close()
			return {'error': 'User already exists'}, 400

		cursor.execute('''
			INSERT INTO user (username, email, password)
			VALUES (?, ?, ?)
		''', (username, email, hashed_password))

		conn.commit()
		conn.close()
		return {'message': 'User registered successfully'}, 201

def login_user(username, password):
	with current_app.app_context():
		conn = sqlite3.connect(current_app.config['DATABASE'])
		cursor = conn.cursor()

		cursor.execute('''
			SELECT * FROM user
			WHERE username = ?
		''', (username,))

		user = cursor.fetchone()


		if user and bcrypt.check_password_hash(user[3], password):
			conn.close()
			return {'message': 'Login successful'}
		else:
			conn.close()
			return {'error': 'Invalid credentials'}, 401

# Example route to use these functions in your Flask app
@auth_bp.route('/register', methods=['POST'])
def register():
	data = request.json
	username = data.get('username')
	email = data.get('email')
	password = data.get('password')

	if not username or not email or not password:
		return jsonify({'error': 'Missing required fields'}), 400

	return create_user(username, email, password)

@auth_bp.route('/login', methods=['POST'])
def login():
	data = request.json
	username = data.get('username')
	password = data.get('password')

	print(username, password)
	if not username or not password:
		return jsonify({'error': 'Missing required fields'}), 400

	return login_user(username, password)
