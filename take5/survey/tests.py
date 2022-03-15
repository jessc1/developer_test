from django.test import TestCase, Client
from django.urls import reverse
from .models import Survey
from django.contrib.auth.models import User


class TestSurveyView(TestCase):

    def setUp(self):
        test_user = User.objects.create_user(username='user', password='12345')
        test_user.save()
        self.client = Client()
    
    def test_survey_list_view(self):
        response = self.client.get(reverse('surveys'))
        self.assertEqual(response.status_code, 200)
    
    def test_survey_detail_view(self):
        response= self.client.get('/survey/1/')

    def test_survey_create_view(self):
        response =self.client.post(reverse('survey_create'), {
            'title':'vegan bread gluten free',
            'creator' :'user',
            
            
        })
    
    def test_survey_update_view(self): 
        response = self.client.put(reverse('survey_update', args='1'), {
            'title':'Vegan Bread',
            'creator' :'user',
                        
            
        })       

    def test_survey_delete_view(self): 
        response = self.client.delete(
            reverse('survey_delete', args='1'))


class TestSurveyQuestionView(TestCase):
    
    def setUp(self):
        test_user = User.objects.create_user(username='user', password='12345')
        test_user.save()
        self.client = Client()


    def test_survey_question_list_view(self):
        response = self.client.get(reverse('questions'))
        self.assertEqual(response.status_code, 200)


    def test_survey_question_detail_view(self):
        response= self.client.get('/question/1/')

    def test_survey_question_create_view(self):
        response =self.client.post(reverse('question_create'), {
            'survey':'4',
            'question' :'is vegan bread gluten free?',
                        
            
        })
    
    def test_survey_question_update_view(self): 
        response = self.client.put(reverse('question_update', args='1'), {
            'survey':'4',
            'question' :'is  bread gluten free?',
                        
            
        })       

    def test_survey_question_delete_view(self): 
        response = self.client.delete(
            reverse('question_delete', args='1'))


class TestSurveyQuestionAlteernativeView(TestCase):
    
    def setUp(self):
        test_user = User.objects.create_user(username='user', password='12345')
        test_user.save()
        self.client = Client()


    def test_survey_question_alternative_list_view(self):
        response = self.client.get(reverse('alternatives'))
        self.assertEqual(response.status_code, 200)


    def test_survey_question_alternative_detail_view(self):
        response= self.client.get('/alternative/1/')

    def test_survey_question_alternative_create_view(self):
        response =self.client.post(reverse('alternative_create'), {
            'question':'1',
            'alternative' :'yes',
            'useralternative' :'yes',
                        
            
        })
    
    def test_survey_question_alternative_update_view(self): 
        response = self.client.put(reverse('alternative_update', args='1'), {
            'question':'1',
            'alternative' :'no',
            'useralternative' :'no',
                        
            
        })       

    def test_survey_question_alternative_delete_view(self): 
        response = self.client.delete(
            reverse('alternative_delete', args='1'))        
