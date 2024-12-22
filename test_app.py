import unittest
import os
os.environ['FLASK_ENV'] = 'testing'
from app import app, db
from models import URL
from config import TestConfig


class URLShortenerTestCase(unittest.TestCase):
    """Test the URL shortener app"""
    def setUp(self):
        """Set up the test environment"""
        app.config.from_object(TestConfig)
        self.app_context = app.app_context()
        self.app = app.test_client()
        self.app_context.push()
        self.client = app.test_client()
        print("Using database:", app.config['SQLALCHEMY_DATABASE_URI'])
        db.create_all()
        print("Database tables created")

    def tearDown(self):
        """Tear down the test environment"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        print('database tables droped')

    def test_shorten_url(self):
        """Test the URL shortening functionality"""
        resp = self.app.post('/', data=dict
                             (original_url='https://www.test.com'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Short URL', resp.data)

    def test_redirect_url(self):
        """Test the URL redirection functionality"""
        url = URL(original_url='https://www.test.com', short_url='abc123')
        db.session.add(url)
        db.session.commit()
        response = self.app.get('/abc123')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, 'https://www.test.com')


if __name__ == '__main__':
    unittest.main()
