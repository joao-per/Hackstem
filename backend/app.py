from flask import Flask, jsonify, g, current_app
from dotenv import load_dotenv
import sqlite3
from flask_bcrypt import Bcrypt
from models import userTable, userTokenTable
from auth import auth_bp
import os

load_dotenv()

app = Flask(__name__)
DATABASE = './app.db'
app.config['DATABASE'] = DATABASE
bcrypt = Bcrypt(app)

app.register_blueprint(auth_bp)

def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect(app.config['DATABASE'])
	return db

@app.teardown_appcontext
def close_connection(exception):
	db = getattr(g, '_database', None)
	if db is not None:
		db.close()

def create_tables():
	with app.app_context():
		# Connect to database
		conn = sqlite3.connect(app.config['DATABASE'])
		cursor = conn.cursor()

		# Create tables
		cursor.execute(userTable)
		cursor.execute(userTokenTable)

		# Commit changes
		conn.commit()
		conn.close()
		print('Tables created successfully!')

@app.route('/test')
def index():
	return jsonify({'message': 'Hello World'})
    

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
