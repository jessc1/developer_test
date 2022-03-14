from rest_framework import generics
from .models import Survey
from .serializers import SurveyListSerializer

class SurveyListAPIView(generics.ListAPIView):

    """
    Survey List in the API
    """
    
    queryset = Survey.objects.all()
    serializer_class = SurveyListSerializer
