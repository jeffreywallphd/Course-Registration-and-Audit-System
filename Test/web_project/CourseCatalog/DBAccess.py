from CourseCatalog.models import Subject, Course

# This file serves as a boiler plate accessor class for the Database. If you don't want to use this class you can access the data directly using Django functionality
# Documentation is incomplete. Add more functions if necessary

class DBAccess():

    # Returns all Subject Objects in a Dictionary where the Subject ID is the key and the value is the Subject Object
    @staticmethod
    def getAllSubjects() -> list:
        responseObject = {}

        subjects = Subject.objects.all()

        for subject in subjects:
            responseObject[subject.id] = subject

        return responseObject
   
    # Returns the Subject by ID. If the ID doesn't correspond with a Subject return None
    @staticmethod
    def getSubjectByID(ID: int) -> Subject:
        return Subject.objects.filter(id=ID).first()
   
    # Retuns Subject by Abbreviation
    @staticmethod
    def getSubjectByAbbrev(Abbrev: str) -> Subject:
        return Subject.objects.filter(Abbrev=Abbrev).first()
    
    # Returns all Course Objects in a Dictionary where the Course ID is the key and the value is the Course Object
    @staticmethod
    def getAllCourses() -> list:
        responseObject = {}

        courses = Course.objects.all()

        for course in courses:
            responseObject[course.id] = course

        return responseObject
    
    # Returns the Course by ID. If the ID doesn't correspond with a Course return None
    @staticmethod
    def getCourseByID(ID: int) -> Course:
        return Course.objects.filter(id=ID).first()

    # Returns all Courses that have a given subject
    @staticmethod
    def getCoursesBySubject(Subject: Subject) -> list:
        return Course.objects.filter(Subject=Subject)

    # Returns a course from its subject and course number
    @staticmethod
    def getCourseBySubjectAndCourseNumber(Subject: Subject, CourseNumber: int) -> Course:
        return Course.objects.filter(Subject=Subject, CourseNumber=CourseNumber).first()
   
    # Returns all courses where the description contains
    @staticmethod
    def getCourseWhereDescriptionContains(Description: str) -> list:
        return Course.objects.filter(Description__icontains=Description)

    # Returns all courses that match the description exactly
    @staticmethod
    def getCourseByExactDescription(Description: str) -> Course:
        return Course.objects.filter(Description=Description)
    
    # Returns all courses that with the given Title
    @staticmethod
    def getCourseByExactTitle(Title: str) -> Course:
        return Course.objects.fitler(Title=Title)

    # Helper function for setting database data. Checks if course is already created. If it is not create the course 
    @staticmethod
    def checkAddCourse(Subject: Subject, CourseNumber: int, Title: str, Description: str, Credits: str) -> Course:
        course = DBAccess.getCourseBySubjectAndCourseNumber(Subject, CourseNumber)

        if Course is None:
            return Course.Object.create(
                Subject=Subject,
                CourseNumber=CourseNumber,
                Title=Title,
                Description=Description,
                Credits=Credits,
            )
        else:
            return course
    
