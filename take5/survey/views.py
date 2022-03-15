from rest_framework import generics
from django.views.generic import TemplateView
from .models import Survey, SurveyQuestion, SurveyQuestionAlternative
from .serializers import (SurveyListSerializer, SurveyDetailSerializer, 
    SurveyQuestionListSerializer, SurveyQuestionDetailSerializer, 
    SurveyQuestionAlternativeListSerializer, SurveyQuestionAlternativeDetailSerializer)

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

class SurveyUpdateAPIView(generics.RetrieveUpdateAPIView):
    """
    Update Survey
    """
        
    lookup_field = "id"
    queryset = Survey.objects.all()
    serializer_class = SurveyDetailSerializer

class SurveyDeleteAPIView(generics.DestroyAPIView):
    """
    delete the survey in the api
    """
      
    lookup_field = "id"
    queryset = Survey.objects.all()
    

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

class SurveyQuestionCreateAPIView(generics.CreateAPIView):
    """
    Add a new survey question in the API
    """    
      
    queryset = Survey.objects.all()
    serializer_class = SurveyQuestionDetailSerializer


class SurveyQuestionUpdateAPIView(generics.RetrieveUpdateAPIView):
    """
    Update survey question
    """
        
    lookup_field = "id"
    queryset = Survey.objects.all()
    serializer_class = SurveyQuestionDetailSerializer


class SurveyQuestionDeleteAPIView(generics.DestroyAPIView):
    """
    delete the survey in the api
    """
      
    lookup_field = "id"
    queryset = SurveyQuestion.objects.all()    

    

class SurveyQuestionAlternativeListAPIView(generics.ListAPIView):
    """
    Return the alternative list in the API
    """
    
    queryset = SurveyQuestionAlternative.objects.all()
    serializer_class = SurveyQuestionAlternativeListSerializer


class SurveyQuestionAlternativeRetrieveAPIView(generics.RetrieveAPIView):
    """
    Return the alternative detail in the API 
    """
    lookup_field = "id"
    queryset = SurveyQuestionAlternative.objects.all()
    serializer_class = SurveyQuestionAlternativeDetailSerializer


class SurveyQuestionAlternativeCreateAPIView(generics.CreateAPIView):
    """
    Add a new survey question in the API
    """    
      
    queryset = Survey.objects.all()
    serializer_class = SurveyQuestionAlternativeDetailSerializer


class SurveyQuestionAlternativeUpdateAPIView(generics.RetrieveUpdateAPIView):
    """
    Update survey question
    """
        
    lookup_field = "id"
    queryset = Survey.objects.all()
    serializer_class = SurveyQuestionAlternativeDetailSerializer

class SurveyQuestionAlternativeDeleteAPIView(generics.DestroyAPIView):
    """
    delete the survey in the api
    """
      
    lookup_field = "id"
    queryset = SurveyQuestionAlternative.objects.all()    



    



  



