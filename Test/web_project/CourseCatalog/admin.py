from django.contrib import admin
from CourseCatalog.models import Course, Subject

# Register your models here.

# This page is for declaring what values get shown on the admin page of the Django App

# Registers the Course table and show the fields ID, CourseNumber, Title, Description, Credits
@admin.register(Course)
class DayAdmin(admin.ModelAdmin):
    list_display = ('id', 'CourseNumber', 'Title', 'Description', 'Credits')

# Registers the Subject table and show the id and Abbreviation fields
@admin.register(Subject)
class DayAdmin(admin.ModelAdmin):
    list_display = ('id', 'Abbrev')
