from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Tag)
admin.site.register(RecipeImage)
admin.site.register(IngredientImage)

