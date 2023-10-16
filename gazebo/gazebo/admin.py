from django.contrib import admin
from gazebo.models import Course, Student  

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['number', 'name', 'instructor', 'current_enrollment', 'capacity']
    search_fields = ['name', 'instructor', 'number']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'major', 'graduation_year']
    search_fields = ['user__username', 'major']

# Need configuration for other models
