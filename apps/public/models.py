from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=4000)
    create_date = models.DateTimeField()
    completed = models.BooleanField(default=0)

    def __unicode__(self):
        return self.title


class Cooking_Methods(models.model):
    type_methods = models.CharField(max_length=16)


class Tools(models.model):
    tool = models.CharField(max_length=100)


class Equipment(models.model):
    equipment = models.CharField(max_length=100)
