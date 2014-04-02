from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Todo)
admin.site.register(CookingMethod)
admin.site.register(Equipment)
admin.site.register(Tool)