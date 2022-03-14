from django.db import models

from django.db import models
from django.contrib.auth.models import User


class Survey(models.Model):
    """A survey created """

    title = models.CharField(max_length=64)    
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class SurveyQuestion(models.Model):
    """A question in a survey"""

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.CharField(max_length=128)
    
    def __str__(self):
        return self.question


class SurveyQuestionAlternative(models.Model):
    """A multi-choice option available as a part of a survey question."""

    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    alternative = models.CharField(max_length=255)
    useralternative = models.CharField(max_length=3)

    def __str__(self):
        return self.alternative


class SurveyUserAnswer(models.Model):
    """An answer in a survey's questions."""

    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    answer= models.CharField(max_length=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer

    
