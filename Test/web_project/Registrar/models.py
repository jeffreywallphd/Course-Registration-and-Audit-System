from django.db import models
from CourseCatalog.models import Course, Subject

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
# If you want a graphical representation of the tables and their fields, use the code in quickdb.txt and


# --- MODELS FOR STORING CONSTANT VALUES ---
# These models are for holding tables with constant values. 
# The Day table holds the days of the week (Monday, Tuesday, etc). Subject stores the different subjects (HU, CS, MIS, etc).

# Table for the days of the week. 
# Each row represents a day. There should only be 7 rows in this table. 
# Ex Data:
# ┌────┬────────┬───────────┐
# │ id │ Abbrev │   Text    │
# ├────┼────────┼───────────┤
# │ 1  │ M      │ Monday    │
# │ 2  │ T      │ Tuesday   │
# │ 3  │ W      │ Wednesday │
# │ 4  │ R      │ Thursday  │
# │ 5  │ F      │ Friday    │
# │ 6  │ S      │ Saturday  │
# │ 7  │ U      │ Sunday    │
# └────┴────────┴───────────┘
class Day(models.Model):

    # id Column is automatically generated

    # Day of the week abbreviated to one Character: 'M' -> Monday, 'T' -> Tuesday, etc
    Abbrev = models.CharField(max_length=1, unique=True)

    # Text version of the day
    Text = models.TextField(unique=True)

    # Function for converting the Instance of the row into a string
    def __str__(self):
        return f'Day<[{self.id}]: {self.Abbrev}>'

# Table for storing the different semesters
# Each row represents a semester
# Ex Data:
# ┌────┬────────┐
# │ id │  Name  │
# ├────┼────────┤
# │ 1  │ Fall   │
# │ 2  │ Spring │
# │ 3  │ Summer │
# └────┴────────┘
class Semester(models.Model):

    # Stores the Name for a given semester
    Name = models.TextField()   

    def __str__(self):
        return f'Semester<[{self.id}]: {self.Name}>'

# Table for storing the different terms
# Each row represent a term which is a match of a year and a semester
# ┌────┬──────┬─────────────┐
# │ id │ Year │ Semester_id │
# ├────┼──────┼─────────────┤
# │ 1  │ 2024 │ 1           │
# └────┴──────┴─────────────┘
class Term(models.Model):

    # Link to the semetser table
    Semester = models.ForeignKey(Semester, on_delete=models.RESTRICT)

    # The year of the semester stored as a string
    Year = models.TextField()

    # Add a unique restraint between Year and Semester. This means that no 2 rows
    # Can have the same Year and Semester. This allows for the term 'Fall 2024'
    # to serve as a primary key to search the database
    class Meta:
        constraints = [
            models.UniqueConstraint(
                name='year_semester_unique_contstraint',
                fields=['Year', 'Semester']
            )
        ]

    def __str__(self):
        return f'Term<[{self.id}]: {self.Semester} {self.Year}>'


# --- MODELS FOR STORING DYNAMIC VALUES --- 
    
class Professor(models.Model):

    Name = models.TextField(editable=True)

    def __str__(self):
        return f'Professor<[{self.id}]: {self.Name}>'

# Table for storing Offerings of Classes. Seperating Classes and Offerings
# allows for one class to have multiple offerings
# Ex Data
# ┌───────┬─────────┬─────┬─────┬─────┬───────────┬──────────┬─────────┐
# │  CRN  │ Section │ Cap │ Act │ Rem │ Professor │ Class_id │ Term_id │
# ├───────┼─────────┼─────┼─────┼─────┼───────────┼──────────┼─────────┤
# │ 10008 │ L01     │ 40  │ 16  │ 24  │ Marchese  │ 811      │ 1       │
# │ 10020 │ 0A      │ 80  │ 68  │ 12  │ Shonnard  │ 351      │ 1       │
# │ 10021 │         │ 10  │ 0   │ 10  │ Collins   │ 354      │ 1       │
# │ 10022 │         │ 10  │ 0   │ 10  │ Sandell   │ 354      │ 1       │
# │ 10023 │         │ 10  │ 0   │ 10  │ Mullins   │ 354      │ 1       │
# │       │         │     │     │ ... │           │          │         │
# └───────┴─────────┴─────┴─────┴─────┴───────────┴──────────┴─────────┘

class Offering(models.Model):

    # Ex row for MIS3000
    # ┌───────┬─────────┬─────┬─────┬─────┬───────────┬──────────┬─────────┐
    # │  CRN  │ Section │ Cap │ Act │ Rem │ Professor │ Class_id │ Term_id │
    # ├───────┼─────────┼─────┼─────┼─────┼───────────┼──────────┼─────────┤
    # │ 14965 │ R01     │ 35  │ 20  │ 15  │ Wall      │ 889      │ 1       │
    # └───────┴─────────┴─────┴─────┴─────┴───────────┴──────────┴─────────┘

    # Stores the Course Registration Number. Is an arbitrary Integer 
    # Ex 14965
    CRN = models.AutoField(primary_key=True, default=0)

    # Stores the id of the Class the offering relates 
    # on_delete=CASCADE - If the class is deleted from the table all offerings with that classes id will be deleted
    # Ex 889 points to Class table MIS3000
    Course = models.ForeignKey(Course, on_delete=models.CASCADE, default=0)

    # Stores the Section as a string
    # Ex. 'RO1'
    Section = models.TextField(null=True, editable=True)

    # Stores the capacity as an Integer
    # Ex 35
    Cap = models.IntegerField(null=True, editable=True)

    # Stores the number of registered students as an integer
    # Ex 20
    Act = models.IntegerField(null=True, editable=True)

    # Stores the remaining seats as an integer
    # Ex 15
    Rem = models.IntegerField(null=True, editable=True)

    # Stores the Professor as a String
    # Ex. Wall
    Professor = models.TextField(null=True, editable=True)

    # Stores the Link to the Term Table
    Term = models.ForeignKey(Term, on_delete=models.RESTRICT, default=1)

    # Function for converting the Instance of the row into a string
    def __str__(self):
        return f'Offering<[{self.CRN}]: {self.Course}>'
    

# Table for storing with professors teach which offering
# Each row represents one professor teaching an offering
class Teaches(models.Model):

    # Stores the ID of the offering from the Offering table
    Offering = models.ForeignKey(Offering, on_delete=models.RESTRICT, default=0)

    # Stores the ID of the Professor from the Professor table
    Professor = models.ForeignKey(Professor, on_delete=models.RESTRICT, default=0)

    # Add a unique restraint between Offering and Professor. This means that no 2 rows
    # Can have the same Offering and Professor. This allows for Jeff Wall teaching MIS3000
    # to serve as a primary key to search the database
    class Meta:
        constraints = [
            models.UniqueConstraint(
                name='crn_professor_unique_contstraint',
                fields=['Offering', 'Professor']
            )
        ]
    
    def __str__(self):
        return f'Teaches<{self.Professor}, {self.Offering}>'

# Table for storing which days an offering is being held on
# Each row represents a day
# Ex Data
# ┌────┬───────────┬───────────┬────────┬─────────────┐
# │ id │ StartTime │  EndTime  │ Day_id │ Offering_id │
# ├────┼───────────┼───────────┼────────┼─────────────┤
# │ 1  │ 13:00.000 │ 13:50.000 │ 5      │ 13350       │
# │ 2  │ 13:00.000 │ 13:50.000 │ 5      │ 14170       │
# │ 3  │ 10:00.000 │ 10:50.000 │ 5      │ 14478       │
# │ 4  │ 08:00.000 │ 09:50.000 │ 5      │ 11956       │
# │ 5  │ 10:00.000 │ 11:40.000 │ 5      │ 14501       │
# |    |           |    ...    |        |             | 
# └────┴───────────┴───────────┴────────┴─────────────┘
class OfferingDay(models.Model):

    # Ex Rows for MIS3000
    # ┌──────┬───────────┬───────────┬────────┬─────────────┐
    # │  id  │ StartTime │  EndTime  │ Day_id │ Offering_id │
    # ├──────┼───────────┼───────────┼────────┼─────────────┤
    # │ 1369 │ 13:00.000 │ 13:50.000 │ 1      │ 14965       │
    # │ 1370 │ 13:00.000 │ 13:50.000 │ 3      │ 14965       │
    # │ 1371 │ 13:00.000 │ 13:50.000 │ 5      │ 14965       │
    # └──────┴───────────┴───────────┴────────┴─────────────┘


    # id Colum Automatically generated

    # Link to the Offering Table. Stores the CRN the offering
    # on_delete=CASCADE - If an offering is deleted all offeringDay with that id will be deleted
    # Ex 14965 is the CRN of MIS3000 in the offerings table
    Offering = models.ForeignKey(Offering, on_delete=models.CASCADE, default=0)

    # Link to the Day Table. Stores the ID of the offering is on
    # Ex 1 is the ID of Monday in the Day Table
    Day = models.ForeignKey(Day, on_delete=models.RESTRICT, editable=True, null=True)

    # The StartTime of the offering stored in Text. SQLite doesn't have time functionality
    # so it is just stored as text in military format
    # Ex 13:00.000 -> 1:00 pm
    StartTime = models.TextField(null=True, editable=True)

    # The EndTime of the offering stored in Text. SQLite doesn't have time functionality
    # so it is just stored as text in military format
    # Ex 13:50.00 -> 1:50 pm
    EndTime = models.TextField(null=True, editable=True)

    # Unique Constraint on the Day and the Offering. This means that one class cannot 
    # have 2 meeting times on the same day. It also allows the Offering and the Day to 
    # serve as a Primary Key for the table
    class Meta:
        constraints = [
            models.UniqueConstraint(
                name='offering_day_unique_constraint',
                fields=['Offering', 'Day']
            )
        ]

    # Function for converting the Instance of the row into a string
    def __str__(self):
        return f'OfferingDay<[{self.id}]: {self.Offering}>'
    
 
