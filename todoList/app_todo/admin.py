from django.contrib import admin
from .models import AppUser, todo

# Register your models here.
admin.site.register(AppUser)
admin.site.register(todo)