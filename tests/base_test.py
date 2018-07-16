"""
BaseTest

This class should be the parent class to each non-unit test.
It allows for instantiation of the database dynamically
and makes sure that it is a new, blank database each time.
"""

from unittest import TestCase
import app
from db import db


class BaseTest(TestCase):
    @classmethod
    def setUpClass(cls):
        app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' #sqlite doesn't enforce foreign keys - so if testing, use postgress or mysql
        with app.app.app_context():
            db.init_app(app.app)


    def setUp(self):
        # Make sure database exists
        with app.app.app_context():
            db.create_all()
        # Get a test client
        self.app = app.app.test_client
        self.app_context = app.app.app_context

    def tearDown(self):
        # Database is blank
        with app.app.app_context():
            db.session.remove()
            db.drop_all()
