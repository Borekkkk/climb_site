import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # image = models.ImageField()

    def __str__(self):
        return self.choice_text


class Voie(models.Model):
    """
    Classe de description d'une voie

    De base :
    name
    description
    difficultée
    image
    ++ pour allez plus loin ++
    localisation
    notation
    types de prises
    """
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="voies")
    difficulty = models.CharField(max_length=200)

    def __str__(self):
        return self.name

