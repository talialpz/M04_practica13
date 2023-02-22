#Creem la classe
class user:
    #Li donem la estructura i atributs
    def __init__(self, name, surname, num, email, years, gender):
        self.name = name
        self.surname = surname
        self.num = num
        self.email = email
        self.years = years
        self.gender = gender
    
    #Definim els getters i setters
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def getSurname(self):
        return self.surname
    
    def setSurname(self, surname):
        self.surname = surname

    def getNum(self):
        return self.num
    
    def setNum(self, num):
        self.num = num
    
    def getEmail(self):
        return self.email
    
    def setEmail(self, email):
        self.email = email

    def getYears(self):
        return self.years
    
    def setYears(self, years):
        self.years = years

    def getGender(self):
        return self.gender
    
    def setGender(self, gender):
        self.gender = gender

    #Aquesta funció ens printejarà agafarà el valor de la class en la frase
    def salutacio(self):
        print("L'usuari es diu " + self.name + " " + self.surname + " té " + self.years + " es defineix com " + self.gender + ", el seu nùmero és  " + self.num + " i el seu email és " + self.email)