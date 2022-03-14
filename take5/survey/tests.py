from django.test import TestCase, Client
from django.urls import reverse
from .models import Survey
from django.contrib.auth.models import User


class TestSurveyView(TestCase):

    def setUp(self):
        test_user = User.objects.create_user(username='ani', password='mktj')
        test_user.save()
        self.client = Client()
    
    def test_survey_list_view(self):
        response = self.client.get(reverse('surveys'))
        self.assertEqual(response.status_code, 200)
    
    def test_survey_detail_view(self):
        response= self.client.get('/survey/1/')

    def test_survey_create_view(self):
        response =self.client.post(reverse('survey_create'), {
            'title':'Is carmin vegan?',
            'creator' :'ani',
            
            
        })

    


