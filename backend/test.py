import unittest
from flask import Flask
from flask_testing import TestCase
from database import db
from create_table import app
from models import User

class TestApp(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # Use a separate test database
        return app

    def setUp(self):
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_register_and_login(self):
        # Test User Registration
        response = self.client.post('/auth/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 201)

        # Test User Login
        response = self.client.post('/auth/login', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.json)

if __name__ == '__main__':
    unittest.main()
