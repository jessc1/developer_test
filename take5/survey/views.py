from rest_framework import generics
from django.views.generic import TemplateView
from .models import Survey, SurveyQuestion, SurveyQuestionAlternative
from .serializers import (SurveyListSerializer, SurveyDetailSerializer, 
    SurveyQuestionListSerializer, SurveyQuestionDetailSerializer, 
    SurveyQuestionAlternativeListSerializer)

class SurveyListAPIView(generics.ListAPIView):

    """
    Survey List in the API
    """
    
    queryset = Survey.objects.all()
    serializer_class = SurveyListSerializer


class Home(TemplateView):
    template_name = "home.html"

class SurveyRetrieveAPIView(generics.RetrieveAPIView):
    """
    Return the survey's detail in the API 
    """
    lookup_field = "id"
    queryset = Survey.objects.all()
    serializer_class = SurveyDetailSerializer 

class SurveyCreateAPIView(generics.CreateAPIView):
    """
    Add a new survey in the API
    """    
      
    queryset = Survey.objects.all()
    serializer_class = SurveyDetailSerializer

class SurveyQuestionListAPIView(generics.ListAPIView):
    """
    Return Survey Question List in the API
    """
    
    queryset = SurveyQuestion.objects.all()
    serializer_class = SurveyQuestionListSerializer

class SurveyQuestionRetrieveAPIView(generics.RetrieveAPIView):
    """
    Return the survey's question detail in the API 
    """
    lookup_field = "id"
    queryset = SurveyQuestion.objects.all()
    serializer_class = SurveyQuestionDetailSerializer

class SurveyQuestionAlternativeListAPIView(generics.ListAPIView):
    """
    Return Survey Question List in the API
    """
    
    queryset = SurveyQuestionAlternative.objects.all()
    serializer_class = SurveyQuestionAlternativeListSerializer    



