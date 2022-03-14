from django.test import TestCase, Client
from django.urls import reverse
from .models import Survey
from django.contrib.auth.models import User


class TestSurveyView(TestCase):
    
    def test_survey_list_view(self):
        response = self.client.get(reverse('survey'))
        self.assertEqual(response.status_code, 200)

    


