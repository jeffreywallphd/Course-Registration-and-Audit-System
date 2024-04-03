from Registrar.models import Day, Offering, OfferingDay, Professor, Teaches

class DBAccess():

    # Days Functions
    @staticmethod
    def getAllDays() -> dict:
        allDays = Day.objects.all()
        response = {}

        for day in allDays:
            response[day.id] = day

        return response
    
    @staticmethod
    def getDayByID(ID) -> Day:
        return Day.objects.filter(ID=ID).first()

    @staticmethod 
    def getDayByName(Name) -> Day:
        return Day.objects.filter(Name=Name).first()
    
    @staticmethod
    def filterDayByName(Name) -> list:
        return Day.objects.filter(Name)
    
    # Offering Functions
    @staticmethod
    def getAllOfferings() -> dict:
        allOfferings = Offering.objects.all()
        response = {}

        for offering in allOfferings:
            response[offering.id] = offering

        return response

    @staticmethod
    def getOfferingByCRN(CRN) -> Offering:
        return Offering.objects.filter(CRN=CRN).first()
    
    @staticmethod
    def getOfferingByCourse(Course) -> list:
        return Offering.objects.fitler(Course=Course)
    
    # OfferingDays Fucntions
    @staticmethod
    def getAllOfferingDays() -> dict:
        allOfferingDays = OfferingDay.objects.all()
        response = {}

        for offeringDay in allOfferingDays:
            response[offeringDay.id] = offeringDay

        return response
    

    @staticmethod
    def getProfessorByName(Name):
        return Professor.objects.filter(Name=Name).first()
        

    @staticmethod
    def getProfessorByID(ID):
        return Professor.objects.filter(id=ID).first()

    @staticmethod
    def checkAddProfessor(Name):
        prof = DBAccess.getProfessorByName(Name)

        if prof is None:
            return Professor.objects.create(Name=Name)
        else:
            return prof
        
    @staticmethod
    def profTeachesOffering(Professor, Offering):
        try:
            Teaches.objects.create(Professor=Professor, Offering=Offering)
        except:
            return 'An error occured'
