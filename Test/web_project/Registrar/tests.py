from django.test import TestCase
from Registrar.models import Subject, Professor
from Registrar.DBAccess import DBAccess

# Create your tests here.
'''
class SubjectTests(TestCase):

    def setUp(self):
        Subject.objects.create(Abbrev='HU', id=1)

    def test_getValidSubjectAbbrev(self):
        tmp = DBAccess.getSubjectByAbbreviation('HU')
        self.assertEqual(tmp.id, 1)

    def test_getValidSubjectID(self):
        tmp = DBAccess.getSubjectByID(1)
        self.assertEqual(tmp.Abbrev, 'HU')

    def test_getInvalidSubjectAbbrev(self):
        tmp = DBAccess.getSubjectByAbbreviation('AU')
        self.assertEqual(tmp, None)
    

class ProfessorTests(TestCase):

    def setUp(self):

        Professor.objects.create(Name='John Smith', id=1)
        Professor.objects.create(Name='Jane Doe', id=2)
        Professor.objects.create(Name='Jeff Wall', id=3)
        Professor.objects.create(Name='Todd Arney', id=4)


    def test_getValidProfName(self):
        tmp = DBAccess.getProfessorByName('John Smith')
        self.assertEqual(tmp.id, 1)

    def test_getInvliadProfName(self):
        tmp = DBAccess.getProfessorByName('Gabe Smit')
        self.assertEqual(tmp, None)

    def test_addProfessor(self):

        tmp1 = Professor.objects.get(Name='Jeff Wall')
        tmp2 = DBAccess.checkAddProfessor('Jeff Wall')

        self.assertEqual(tmp1, tmp2)

    def test_addProfessor1(self):

        tmp1 = DBAccess.checkAddProfessor('Gabe Smit')

        self.assertNotEqual(tmp1, None)

'''
