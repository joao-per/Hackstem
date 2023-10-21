import unittest
from flask import Flask, jsonify
import sqlite3
from app import create_tables
import requests

class TestRemoteAuthenticationEndpoints(unittest.TestCase):

	def setUp(self):
		self.base_url = "https://hackstem--pedperei.repl.co"  # Update with your hosted server URL

	def tearDown(self):
		# Truncate tables on the hosted server
		response = requests.post(f"{self.base_url}/truncate-tables")
		self.assertEqual(response.status_code, 200)

	def test_server_is_up(self):
		response = requests.get(self.base_url)
		self.assertEqual(response.status_code, 200)

	def test_register_user(self):
		data = {
			'username': "testRegisterUser",
			'email': "ppppppppppppppppp@example.com",
			'password': "password123"
		}

		response = requests.post(f"{self.base_url}/register", json=data)
		data = response.get_json()
		print(data)
		self.assertEqual(response.status_code, 201)
		self.assertIn('message', data)
		self.assertEqual(data['message'], 'User registered successfully')

	def test_register_user_missing_fields(self):
		data = {
			'username': 'testUserMissingFields',
			'password': 'password123'
		}

		response = requests.post(f"{self.base_url}/register", json=data)
		data = response.get_json()

		self.assertEqual(response.status_code, 400)
		self.assertIn('error', data)
		self.assertEqual(data['error'], 'Missing required fields')

	def test_login_user(self):
		data = {
			'username': "TestLoginUser",
			'email': "testuser@example.com",
			'password': "password123"
		}

		# Register the user first
		response = requests.post(f"{self.base_url}/register", json=data)

		# Now attempt to login
		response = requests.post(f"{self.base_url}/login", json=data)
		data = response.get_json()

		self.assertEqual(response.status_code, 200)
		self.assertIn('message', data)
		self.assertEqual(data['message'], 'Login successful')

	def test_login_user_invalid_credentials(self):
		response = response = requests.post(f"{self.base_url}/login", json={'username': 'nonexistentuser', 'password': 'wrongpassword'})
		data = response.get_json()

		self.assertEqual(response.status_code, 401)
		self.assertIn('error', data)
		self.assertEqual(data['error'], 'Invalid credentials')

	def test_register_user_already_registered(self):
		data = {
			'username': 'testUserAlreadyRegistered',
			'email': 'testemail',
			'password': 'password123'
		}

		# Register the user first
		response = requests.post(f"{self.base_url}/register", json=data)

		# Now attempt to register again
		response = requests.post(f"{self.base_url}/register", json=data)
		data = response.get_json()

		self.assertEqual(response.status_code, 400)
		self.assertIn('error', data)
		self.assertEqual(data['error'], 'User already exists')


if __name__ == '__main__':
	unittest.main()
