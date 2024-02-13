from unittest import TestCase

from app.infra.db.connector import AppSession

class AppSessionTestCase(TestCase):
    
    def setUp(self):
        self.app_session = AppSession()
    
    def test_create_all(self):
        self.app_session.create_tables()