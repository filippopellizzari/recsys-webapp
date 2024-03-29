from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from .models import *
from recsys.models import Recommender
#from algos.models import InputModel

class Option(models.Model):
    option_id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=30)

    def __str__(self):
        return str(self.option_id) + ": " + self.text

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    genre = models.CharField(max_length=30)
    text = models.TextField()
    last_update = models.DateTimeField(auto_now=True)
    options = models.ManyToManyField(Option, through="OptionOrder")

    def __str__(self):
        return str(self.question_id) + ": "+"("+self.genre+")  " + self.text

class Survey(models.Model):
    TYPE_CHOICES = (
        ('Between-subject', 'Between-subject'),
        ('Within-subject', 'Within-subject'),
    )
    survey_id = models.AutoField(primary_key=True)
    survey_name = models.CharField(max_length=100)
    survey_type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    last_update = models.DateTimeField(auto_now=True)
    opening_time = models.DateTimeField(null=True)
    closing_time = models.DateTimeField(null=True, blank=True)
    questions = models.ManyToManyField(Question, through="QuestionOrder")
    input_length = models.PositiveIntegerField(default=5, blank=False, null=False,
        help_text="This is the number of movies to select in the catalogue. Note: value range is from 1 to 10.",
        validators=[MaxValueValidator(10), MinValueValidator(1)])
    reclist_length = models.PositiveIntegerField(default=5, blank=False, null=False,
        help_text="This is the number of movies in the recommendation list. Note: value range is from 1 to 10.",
        validators=[MaxValueValidator(10), MinValueValidator(1)])
    random_first_page = models.PositiveIntegerField(default=1, blank=False, null=False,
        help_text="This is the first catalogue page used by Random Recommender.",
        validators=[MinValueValidator(1)])
    random_last_page = models.PositiveIntegerField(default=1, blank=False, null=False,
        help_text="This is the last catalogue page used by Random Recommender.",
        validators=[MinValueValidator(1)])
    algorithms = models.ManyToManyField(Recommender, through="Algorithm")

    def __str__(self):
        return str(self.survey_id)

class Algorithm(models.Model):
    recommender = models.ForeignKey(Recommender, related_name='recommender_to_survey',null=True)
    survey = models.ForeignKey(Survey, related_name='survey_to_recommender')
    genre = models.BooleanField(default=False)
    ngenres = models.PositiveIntegerField(default=1,blank=False, null=False, validators=[MinValueValidator(1)])
    crew = models.BooleanField(default=False)
    ncrew = models.PositiveIntegerField(default=1,blank=False, null=False, validators=[MinValueValidator(1)])
    cast = models.BooleanField(default=False)
    ncast = models.PositiveIntegerField(default=1,blank=False, null=False, validators=[MinValueValidator(1)])


class QuestionOrder(models.Model):
    question = models.ForeignKey(Question, related_name='question_to_survey')
    survey = models.ForeignKey(Survey, related_name='survey_to_question')
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ('order',)

class OptionOrder(models.Model):
    option = models.ForeignKey(Option, related_name='option_to_question')
    question = models.ForeignKey(Question, related_name='question_to_option')
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ('order',)

class SurveyResponse(models.Model):
    email = models.CharField(max_length=100)
    completed_at = models.DateTimeField(auto_now_add=True)
    survey_id = models.ForeignKey(Survey)
    is_valid = models.BooleanField(default=True)
    user_profile = models.TextField(null=True)
    algorithms = models.CharField(null=True,max_length=500)
    recommendations = models.TextField(null=True)

class Response(models.Model):
    survey_response = models.ForeignKey(SurveyResponse, related_name='responses')
    question = models.TextField()
    answer = models.CharField(max_length=30)
    email = models.CharField(null=True,max_length=100)
    completed_at = models.DateTimeField(auto_now_add=True)
    survey_id = models.CharField(null=True,max_length=30)
    is_valid = models.BooleanField(default=True)
    user_profile = models.TextField(null=True)
    algorithms = models.CharField(null=True,max_length=500)
    recommendations = models.TextField(null=True)
