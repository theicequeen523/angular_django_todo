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

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(null=True, blank=True,max_length=100)
    flavor = models.CharField(null=True, blank=True,max_length=100)
    glyc_index = models.IntegerField(null=True, blank=True,max_length=10)
    tag = models.ManyToManyField("Tag")

    def __unicode__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(null=True, blank=True,max_length=100)
    prep_time = models.CharField(null=True, blank=True,max_length=50)
    ingredient = models.ManyToManyField(Ingredient)
    instruction = models.CharField(null=True, blank=True,max_length=2000)
    temp = models.CharField(max_length=10)
    time = models.CharField(max_length=10)
    serv_size = models.IntegerField(null=True, blank=True, max_length=10)
    tag = models.ManyToManyField("Tag")


    def __unicode__(self):
        return self.name


class RecipeImage(models.Model):
     img = models.ImageField(null=True, blank=True, upload_to="static/img")
     recipe = models.ForeignKey(Recipe)


class IngredientImage(models.Model):
    img = models.ImageField(null=True, blank=True, upload_to="static/img")
    ingredient = models.ForeignKey(Ingredient)


class Tag(models.Model):
    name = models.CharField(null=True, blank=True, max_length=30)

    def __unicode__(self):
        return self.name




