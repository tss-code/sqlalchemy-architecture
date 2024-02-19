from unittest import TestCase

from app.infra.db.connector import AppSession
from app.models.recruitment.models import Company, Recruiter

class AppSessionTestCase(TestCase):
    
    def setUp(self):
        self.app_session = AppSession()
    
    def test_create_all(self):
        self.app_session.create_tables()
    
    def test_create_company(self):
        company = Company(
            name="New company"
        )
        self.app_session.add(company)
    
    def test_create_recruiter(self):
        recruiter = Recruiter(
            name="Created recruiter",
            company_id="df878bb8-d647-48b7-8f8e-0d2f4ccea187"
        )
        self.app_session.add(recruiter)