from django.contrib import admin
from app1.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'teacher_name', 'email', 'password']


# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['student_id', 'first_name', 'admission_date']