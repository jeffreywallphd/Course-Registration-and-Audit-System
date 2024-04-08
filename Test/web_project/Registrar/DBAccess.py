from Registrar.models import Day, Offering, OfferingDay, Professor, Teaches

# Class that accesses the data stored in the models for this app

class DBAccess():

    # Days Functions

    # Return all day objects as a Dictionary where the Day ID is the key and the value is the Day Object
    @staticmethod
    def getAllDays() -> dict:
        allDays = Day.objects.all()
        response = {}

        for day in allDays:
            response[day.id] = day

        return response
   
    # Return the day object from its ID
    @staticmethod
    def getDayByID(ID) -> Day:
        return Day.objects.filter(ID=ID).first()

    # Return the Day object by its Name
    @staticmethod 
    def getDayByName(Name) -> Day:
        return Day.objects.filter(Name=Name).first()
   
    
    # Offering Functions

    # Return all Offering objects as a Dictionary where the Offering ID is the key and the value is the Offering object
    @staticmethod
    def getAllOfferings() -> dict:
        allOfferings = Offering.objects.all()
        response = {}

        for offering in allOfferings:
            response[offering.id] = offering

        return response

    # Return the Offering object from its ID
    @staticmethod
    def getOfferingByCRN(CRN) -> Offering:
        return Offering.objects.filter(CRN=CRN).first()
   
    # Return a list of Offerings of the given Course
    @staticmethod
    def getOfferingsByCourse(Course) -> list:
        return Offering.objects.fitler(Course=Course)
    
    # OfferingDays Fucntions

    # Return all OfferingDay objects as a Dictionary where the OfferingDay ID is the key and the value is the Offering Day object
    @staticmethod
    def getAllOfferingDays() -> dict:
        allOfferingDays = OfferingDay.objects.all()
        response = {}

        for offeringDay in allOfferingDays:
            response[offeringDay.id] = offeringDay

        return response
    

    # Professor Functions

    # Return the Professor object with the given name
    @staticmethod
    def getProfessorByName(Name) -> Professor:
        return Professor.objects.filter(Name=Name).first()
        
    # Return the Professor object with the given ID
    @staticmethod
    def getProfessorByID(ID) -> Professor:
        return Professor.objects.filter(id=ID).first()

    # Assign the Professor to teach the given Offering 
    @staticmethod
    def profTeachesOffering(Professor, Offering):
        try:
            Teaches.objects.create(Professor=Professor, Offering=Offering)
        except:
            return 'An error occured when trying to assign ' + Professor.__str__() + ' to the Offering ' + Offering.__str__()
