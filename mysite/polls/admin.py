from django.contrib import admin
from .models import Question

# Register your models here.
admin.site.register(Question)   #register Question objects with an admin interface.