import unittest
from flask import Flask, jsonify
from app import app, create_tables, get_db

class TestYourApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        with app.test_request_context():
            create_tables()

    def tearDown(self):
        pass  # Optionally, you can perform cleanup after each test

    def test_index_route(self):
        response = self.app.get('/test')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'Hello World')

    def test_database_connection(self):
        with app.test_request_context():
            db = get_db()
            self.assertIsNotNone(db)

if __name__ == '__main__':
    unittest.main()
