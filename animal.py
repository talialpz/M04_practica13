#Se crea la clase vehicle que nos permitira trabajar con los conceptos de la programación orientada a objetos.
class animal:

    #Definimos un constructor el cual tiene como parametro 6 atributos.
    def __init__(self, nombre, peso, reproduccion, alimentacion, habitat, estructura):
        self.nombre = nombre
        self.peso = peso
        self.reproduccion = reproduccion
        self.alimentacion = alimentacion
        self.habitat = habitat
        self.estructura = estructura

    #Trabajamos el metodo getter y setter de cada atributo que hemos especificado anteriormente en el constructor.
    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getPeso(self):
        return self.peso

    def setPeso(self, peso):
        self.peso = peso

    def getReproduccion(self):
        return self.reproduccion

    def setReproduccion(self, reproduccion):
        self.reproduccion = reproduccion

    def getAlimentacion(self):
        return self.alimentacion

    def setAlimentacion(self, alimentacion):
        self.alimentacion = alimentacion

    def getHabitat(self):
        return self.habitat

    def setHabitat(self, habitat):
        self.habitat = habitat

    def getEstructura(self):
        return self.estructura

    def setEstructura(self, estructura):
        self.estructura = estructura

    #Creamos un mensaje que permita ver los atributos de nuestro objeto.
    def salutacio(self):
        txt = "El {nom} tiene un peso de {pes} kg, tiene una reproduccion {rep}, una alimentacion {al}, una estructura {es} y su habitat es {hab}"
        print(txt.format(nom = self.nombre, pes = self.peso, rep = self.reproduccion, al = self.alimentacion, es = self.estructura, hab = self.habitat))