#Se crea la clase vehicle que nos permitira trabajar con los conceptos de la programación orientada a objetos.
class vehicle:

    #Definimos un constructor el cual tiene como parametro 6 atributos.
    def __init__(self, marca, modelo, color, capacidad, kilometraje, placa):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.capacidad = capacidad
        self.kilometraje = kilometraje
        self.placa = placa

    #Trabajamos el metodo getter y setter de cada atributo que hemos especificado anteriormente en el constructor.
    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

    def getModelo(self):
        return self.modelo

    def setModelo(self, modelo):
        self.modelo = modelo

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getCapacidad(self):
        return self.capacidad

    def setCapacidad(self, capacidad):
        self.capacidad = capacidad

    def getKilometraje(self):
        return self.kilometraje

    def setKilometraje(self, kilometraje):
        self.kilometraje = kilometraje

    def getPlaca(self):
        return self.placa

    def setPlaca(self, placa):
        self.placa = placa
        
    #Creamos un mensaje que permita ver los atributos de nuestro objeto.
    def parts(self):
        txt = "El coche es de marca {mar} y de modelo {mod}, es de color {co} con una capacidad de {cap}, la placa es {pl} y su kilometraje es de {kil}"
        print(txt.format(mar = self.marca, mod = self.modelo, co = self.color, cap = self.capacidad, pl = self.placa, kil = self.kilometraje))