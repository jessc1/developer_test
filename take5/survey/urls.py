from django.urls import path
from . import views

urlpatterns = [
    
    path('surveys',views.SurveyListAPIView.as_view(), name='surveys'),
    path('survey/<int:id>', views.SurveyRetrieveAPIView.as_view(), name='survey'),
    path('survey/create', views.SurveyCreateAPIView.as_view(), name='survey_create'),
    path('survey/delete/<int:id>/', views.SurveyDeleteAPIView.as_view(), name='survey_delete'),
    path('survey/update/<int:id>/', views.SurveyUpdateAPIView.as_view(), name='survey_update'),
    path('questions',views.SurveyQuestionListAPIView.as_view(), name='questions'),
    path('question/<int:id>', views.SurveyQuestionRetrieveAPIView.as_view(), name='question'),
    path('question/create', views. SurveyQuestionCreateAPIView.as_view(), name='question_create'),
    path('question/delete/<int:id>/', views. SurveyQuestionDeleteAPIView.as_view(), name='question_delete'),
    path('question/update/<int:id>/', views.SurveyQuestionUpdateAPIView.as_view(), name='question_update'),
    path('alternatives/',views.SurveyQuestionAlternativeListAPIView.as_view(), name='alternatives'),
    path('alternative/<int:id>', views.SurveyQuestionAlternativeRetrieveAPIView.as_view(), name='alternative'),
    path('alternative/create', views.SurveyQuestionAlternativeCreateAPIView.as_view(), name='alternative_create'),
    path('alternative/delete/<int:id>/', views.SurveyQuestionAlternativeDeleteAPIView.as_view(), name='alternative_delete'),
    path('alternative/update/<int:id>/', views.SurveyQuestionAlternativeUpdateAPIView.as_view(), name='alternative_update'),
    
    
    ]
