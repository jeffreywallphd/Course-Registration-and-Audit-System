from django.test import TestCase
from CourseCatalog.DBAccess import DBAccess
from CourseCatalog.models import Course, Subject

# Create your tests here.

class CourseTests(TestCase):

    def setUp(self):
  
        # Initialize the data you want to test on here. Django tests do not run on the current data
        # Instead a temporary Database is created with the exact same tables as the live tables
        # This function is where you would initaize any fake data you need to run tests
        # Below is an example of creating a temporary Subject called MIS, and a course for MIS3200

        subject = Subject.objects.create(Abbrev='MIS') 

        course = Course.objects.create(
            Subject=subject,
            CourseNumber=3200,
            Title='Systems Analysis and Design',
            Description='Idk man some random shit',
            Credits='3',
        )

    def tearDown(self):
        # Use this function to clean up any data in between CourseTests
        pass


    # Tests that getting a Valid
    def testDBAccessGetCourseByIDSuccess(self):
        course = DBAccess.getCourseByID(1)

        self.assertNotEquals(course, None)
    
    def testDBAccessGetCourseByIDFailure(self):

        course = DBAccess.getCourseByID(2)

        self.assertEquals(course, None)
