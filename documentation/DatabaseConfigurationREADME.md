# Database Configuration Branch 
This branch was created to add the apps used to store Course, Registration and Degree Audit Database

In this branch I created 3 apps in the web_project folder: CourseCatalog, DegreeAudit and Registrar

Each of these apps are responsible for storing and retrieving their corresponding data

## Data Initialization

If you have just pulled the files from the GitHub the database will not be configured. You will need to run the following commands from the web_project directory: 

```python manage.py makemigrations```
```python manage.py migrate```
```python manage.py dbshell < db_init.sql```

## CourseCatalog

This app stores the Course and Subject Information. 

 Ex Row for MIS3000
 ┌─────┬──────────────┬───────────────────────────┬──────────────────┬─────────┬────────────┐
 │ id  │ CourseNumber │           Title           │   Description    │ Credits │ Subject_id │
 ├─────┼──────────────┼───────────────────────────┼──────────────────┼─────────┼────────────┤
 │ 625 │ 3000         │ Business Process Analysis │                  │ 3       │ 35         │
 └─────┴──────────────┴───────────────────────────┴──────────────────┴─────────┴────────────┘

 Ex rows for Subjects Table
 ┌────┬────────┐
 │ id │ Abbrev │
 ├────┼────────┤
 │ 1  │ HU     │
 │ 2  │ CEE    │
 │ 3  │ ENT    │
 │ 4  │ MEEM   │
 │ 5  │ MSE    │
 │ 6  │ PH     │
 │ 7  │ CH     │
 │     ...     │
 └────┴────────┘ 

## Registrar

This app stores the registration information. This includes Course Offerings, times, days, Professors, etc.

## DegreeAudit

The skeleton of this app was created but not implemented. 

## Accessing Data

Both Registrar and CourseCatalog have a file called 'DBAccess.py'. This file contains a Class that has getter methods for each app's data. There are likely going to be more functions necessary to complete all tasks so feel free to add more. You can access the data directly from the Django libraries if that makes more sense


