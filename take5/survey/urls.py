from django.urls import path
from . import views

urlpatterns = [
    path('survey/list',views.SurveyListAPIView.as_view(), name='survey'),
    ]
