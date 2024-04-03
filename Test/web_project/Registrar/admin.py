from django.contrib import admin
from Registrar.models import Day, Offering, OfferingDay, Term, Semester, Teaches, Professor

# Admin page creation
# Each of the following is for registering the models defined in models.py for the website
# If you run the server locally and go to http://127.0.0.1:8000/admin/ and enter your credentials
# you should see a the data 

# If you do not have a username and password do the following:
# Go to your terminal you use to launch the server
# enter 'python manage.py createsuperuser'
# follow the prompts to set your username and password

@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ('id', 'Text', 'Abbrev')

@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ('id', 'Semester', 'Year')

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name')

@admin.register(Offering)
class OfferingAdmin(admin.ModelAdmin):
    list_display = ('CRN', 'Course', 'Section', 'Cap', 'Act', 'Rem', 'Professor', 'Term')

@admin.register(OfferingDay)
class OfferingDayAdmin(admin.ModelAdmin):
    list_display = ('id', 'Offering', 'Day', 'StartTime', 'EndTime')

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name')

@admin.register(Teaches)
class TeachesAdmin(admin.ModelAdmin):
    list_display = ('id', 'Offering', 'Professor')

