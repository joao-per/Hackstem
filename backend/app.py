from flask import Flask, jsonify, g, current_app
import sqlite3
from flask_bcrypt import Bcrypt
from models import userTable, userTokenTable, avatarTable, hatsTable, shirtTable, pantsTable
from auth import auth_bp
import os


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
		cursor.execute(hatsTable)
		cursor.execute(shirtTable)
		cursor.execute(pantsTable)
		cursor.execute(avatarTable)
		cursor.execute(userTable)
		cursor.execute(userTokenTable)

		# Commit changes
		conn.commit()
		conn.close()
		print('Tables created successfully!')

def populate_tables():
	with app.app_context():
		# Connect to database
		conn = sqlite3.connect(app.config['DATABASE'])
		cursor = conn.cursor()

		# Populate hats table
		cursor.execute("INSERT INTO hat (name) VALUES ('Fedora')")
		cursor.execute("INSERT INTO hat (name) VALUES ('Baseball Cap')")

		cursor.execute("INSERT INTO shirt (name) VALUES ('T-Shirt')")
		cursor.execute("INSERT INTO shirt (name) VALUES ('Button-down Shirt')")

		cursor.execute("INSERT INTO pant (name) VALUES ('Jeans')")
		cursor.execute("INSERT INTO pant (name) VALUES ('Khakis')")

		# Commit changes
		conn.commit()
		conn.close()

@app.route('/test')
def index():
	return jsonify({'message': 'Hello World'})
	

if __name__ == '__main__':
	create_tables()
	populate_tables()
	app.run(debug=True)
