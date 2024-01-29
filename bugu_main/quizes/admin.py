from django.contrib import admin

# Register your models here.
# admin.py

from .models import Topic, Quiz


admin.site.register(Topic)
admin.site.register(Quiz)

