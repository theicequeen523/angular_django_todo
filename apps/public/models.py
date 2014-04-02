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


class CookingMethod(models.Model):                  #
    method = models.CharField(max_length=500)

    def __unicode__(self):
        return self.method


class Tool(models.Model):                           # utinsiles used for the ingredient
    tool = models.CharField(max_length=100)

    def __unicode__(self):
        return self.tool


class Equipment(models.Model):                      # Equipment to to Use
    equipment = models.CharField(max_length=100)

    def __unicode__(self):
        return self.equipment


class ShelfLife(models.Model):                      # Date bought and life of product
    ShelfLife = models.CharField(max_length=100)

    def __unicode__(self):
        return self.ShelfLife


class RecipeImage(models.Model):                    # Loads up pictures
    image = models.ImageField(upload_to="logos")

    def __unicode__(self):
        return self.image
