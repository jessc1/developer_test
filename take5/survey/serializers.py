from rest_framework import serializers
from .models import (Survey, SurveyQuestion, SurveyQuestionAlternative, 
     SurveyUserAnswer)


class SurveyListSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Survey
        fields = "__all__"


class SurveyDetail(serializers.ModelSerializer):

    class Meta:

        model = Survey
        fields = '__all__'

class SurveyQuestionListSerializer(serializers.ModelSerializer):

    class Meta:

        model = SurveyQuestion
        fields = '__all__'

class SurveyQuestionDetailSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = SurveyQuestion
        fields = '__all__'

class SurveyQuestionAlternativeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = SurveyQuestionAlternative
        fields = '__all__'

class SurveyQuestionAlternativeDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = SurveyQuestionAlternative
        fields = '__all__'        
        
        
