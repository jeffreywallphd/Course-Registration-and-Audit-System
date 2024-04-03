from django.db import models
# --- Notes ---
# Django Models Basics
# These class definitions are automatically converted to SQLite tables. 
# Each Class member is converted to a column in the SQL table. 
# Ex. Subject
#       Abbrev = models.CharField(max_length=4, unique=True) 
#           L-> Converted to a char column named 'abbrev' in the database 
#               with the restrictions fo 4 characters and each row is unique
# 
# The __str__() method defines what string is returned when you convert the obj to a string
# Ex. If you have a an instance of a day stored in dayObj, calling print(dayObj) would print
# "Day<[1]: M>" Where 1 is the id of the day, and M is the abbreviation
# 
# If no primary key is specified for a table Django will automatically create one. 
# The name of the column will be 'id'. It will automatically generate a unique integer for each record
# 
# Primary keys are set by providing the 'primary_key=True' param when defining a column
# Ex. Offering
#       CRN = models.AutoField(primary_key=True, default=0)
# 
# Fields that I used
#   models.AutoField() -> column that will automatically generate a unqiue integer for each row
#   models.TextField() -> column that will store a string
#   models.CharField() -> column that stores an array of chars (Allows for a length limit on strings)
#   models.IntegerField() -> column that stores Integer value
#   models.ForeignKey() -> column that stores the Primary Key of another table. This allows links 
#                          between the different tables
# 

# Table for storing the different subjects offered
# Each row represents a subject
# Ex Data:
# ┌────┬────────┐
# │ id │ Abbrev │
# ├────┼────────┤
# │ 1  │ HU     │
# │ 2  │ CEE    │
# │ 3  │ ENT    │
# │ 4  │ MEEM   │
# │ 5  │ MSE    │
# │ 6  │ PH     │
# │ 7  │ CH     │
# │     ...     │
# └────┴────────┘ 
class Subject(models.Model):

    # id Column is automatically generated

    # Stores the Abbreviation of the Subject as Chars
    Abbrev = models.CharField(max_length=4, unique=True)

    # Function for converting the Instance of the row into a string
    def __str__(self):
        return f'Subject<[{self.id}]: {self.Abbrev}>'

# Create your models here.
# Table for storing classes
# Each row represents a class 
# Ex Data
# ┌────┬──────────────┬──────────────────────────────┬──────────────────┬─────────────┬────────────┐
# │ id │ CourseNumber │            Title             │   Description    │   Credits   │ Subject_id │
# ├────┼──────────────┼──────────────────────────────┼──────────────────┼─────────────┼────────────┤
# │ 1  │ 4101         │ Writing Center Practicum     │                  │ 1           │ 1          │
# │ 2  │ 4507         │ Water Distr. and WW Collect. │                  │ 0           │ 2          │
# │ 3  │ 5507         │ Water Distr. and WW Collect. │                  │ 0           │ 2          │
# │ 4  │ 3980         │ Velovations Pre-Capstone     │                  │ 1           │ 3          │
# │ 5  │ 5950         │ Velovations Grad I           │                  │ 1.000-3.000 │ 3          │
# └────┴──────────────┴──────────────────────────────┴──────────────────┴─────────────┴────────────┘

class Course(models.Model):

    # Ex Row for MIS3000
    # ┌─────┬──────────────┬───────────────────────────┬──────────────────┬─────────┬────────────┐
    # │ id  │ CourseNumber │           Title           │   Description    │ Credits │ Subject_id │
    # ├─────┼──────────────┼───────────────────────────┼──────────────────┼─────────┼────────────┤
    # │ 625 │ 3000         │ Business Process Analysis │                  │ 3       │ 35         │
    # └─────┴──────────────┴───────────────────────────┴──────────────────┴─────────┴────────────┘


    # Stores the Course Number for each class
    # MIS3000 -> CourseNumber = 3000
    CourseNumber = models.IntegerField(default=0)

    # Stores the primary key of the Subject on the Subject table. 
    # id = 35, 35 -> MIS
    # on_delete=RESTRICT - This will prevent a user from deleting a subject if there a 
    # class with that subject
    Subject = models.ForeignKey(Subject, on_delete=models.RESTRICT, null=True, editable=True) 

    # Stores the title of the class as a string
    # 'Business Process Analysis
    Title = models.TextField()

    # Stores the Description of the Course
    # The registration data I used to for this database did not have course descriptions so it is left blank
    Description = models.TextField(editable=True)

    # Stores the credits of the class as a STRING
    # I chose to store it as a string because some classes have a credit range. 
    # For what we need right now I believe this is easier than creating a range column
    # Is subject to change
    Credits = models.TextField(editable=True)

    # Add a unique restraint between CourseNumber and Subject. This means that no 2 rows
    # Can have the same CourseNumber and Subject. This allows for the course name 'MIS3000'
    # to serve as a primary key to search the database
    class Meta:
        constraints = [
            models.UniqueConstraint(
                name='number_subject_unique_contstraint',
                fields=['CourseNumber', 'Subject']
            )
        ]

    # Function for converting the Instance of the row into a string
    def __str__(self):
        return f'Course<[{self.id}]: {self.Subject}{self.CourseNumber}>'
