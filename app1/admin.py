from django.contrib import admin
from app1.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'password']