#Creem la classe
class university:
    #Li donem la estructura i atributs
    def __init__(self, name, timetable, author, financiation, year, localization):
        self.name = name
        self.timetable = timetable
        self.author = author
        self.financiation = financiation
        self.year = year
        self.localization = localization
    
    #Definim els getters i setters
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def getTimetable(self):
        return self.timetable
    
    def setTimetable(self, timetable):
        self.timetable = timetable

    def getAuthor(self):
        return self.author
    
    def setFinanciation(self, author):
        self.author = author
    
    def getFinanciation(self):
        return self.financiation
    
    def setPages(self, financiation):
        self.financiation = financiation

    def getYear(self):
        return self.year
    
    def setYear(self, year):
        self.year = year

    def getLocalization(self):
        return self.localization
    
    def setLocalization(self, localization):
        self.localization = localization

    #Aquesta funció ens printejarà agafarà el valor de la class en la frase
    def info(self):
        print("L'universitat es diu " + self.name + ", està en " + self.localization + ", va ser creada per " + self.author + " en el " + self.year + " té una financiació " + self.financiation + " i té un horari de " + self.timetable)
