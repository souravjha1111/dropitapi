from django.contrib import admin

# Register your models here.
from .models import UserProfile, User
admin.site.register(UserProfile)
admin.site.register(User)