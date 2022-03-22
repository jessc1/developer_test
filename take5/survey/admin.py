from django.contrib import admin
from django.contrib import admin
from .models import (Survey, SurveyQuestion, SurveyQuestionAlternative, 
     SurveyUserAnswer)

@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    
    list_display = ('title',)
    
@admin.register(SurveyQuestion)
class SurveyQuestionAdmin(admin.ModelAdmin):
    list_display = ('question',)

@admin.register(SurveyQuestionAlternative)
class SurveyQuestionAlternativeAdmin(admin.ModelAdmin):
    list_display = ('alternative', 'question',)
    




