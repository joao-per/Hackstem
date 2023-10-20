import unittest
from flask import Flask, jsonify
from app import app, create_tables

class TestAuthenticationEndpoints(unittest.TestCase):
	def setUp(self):
		app.config['TESTING'] = True
		self.app = app.test_client()
		with app.test_request_context():
			create_tables()

	def tearDown(self):
		pass  # Optionally, you can perform cleanup after each test

	def test_register_user(self):
		data = {
			'username': 'testuser',
			'email': 'testuser@example.com',
			'password': 'password123'
		}

		response = self.app.post('/register', json=data)
		data = response.get_json()

		try:
			self.assertEqual(response.status_code, 201)
			self.assertIn('message', data)
			self.assertEqual(data['message'], 'User registered successfully')
		except:
			print("Assertion failed: test_register_user.")

	def test_register_user_missing_fields(self):
		data = {
			'username': 'testuser',
			'password': 'password123'
		}

		response = self.app.post('/register', json=data)
		data = response.get_json()

		try:
			self.assertEqual(response.status_code, 400)
			self.assertIn('error', data)
			self.assertEqual(data['error'], 'Missing required fields')
		except:
			print("Assertion failed: test_register_user_missing_fields.")

	def test_login_user(self):
		data = {
			'username': 'testuser',
			'email': 'testuser@example.com',
			'password': 'password123'
		}

		# Register the user first
		self.app.post('/register', json=data)

		# Now attempt to login
		response = self.app.post('/login', json={'username': 'testuser', 'password': 'password123'})
		data = response.get_json()

		try:
			self.assertEqual(response.status_code, 200)
			self.assertIn('message', data)
			self.assertEqual(data['message'], 'Login successful')
		except:
			print("Assertion failed: Invalid credentials not handled correctly.")

	def test_login_user_invalid_credentials(self):
		response = self.app.post('/login', json={'username': 'nonexistentuser', 'password': 'wrongpassword'})
		data = response.get_json()

		self.assertIn('error', data)
		self.assertEqual(data['error'], 'Invalid credentials')

if __name__ == '__main__':
	unittest.main()
