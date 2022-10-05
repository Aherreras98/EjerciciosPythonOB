# Crear la clase Vehiculo con los siguientes atributos: Color, Ruedas y Puertas
# Crear la clase Coche que herede de Vehiculo y tenga los atributos Velocidad y Cilindrada
# Crear un objeto de la clase coche y mostrarlo por consola

class Vehiculo():
    # inicializamos los atributos
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        return "Color {}, {} ruedas".format( self.color, self.ruedas, self.puertas )

class Coche(Vehiculo):

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "color {}, {} km/h, {} ruedas, {} puertas, {} cc".format( self.color, self.velocidad, self.ruedas, self.puertas, self.cilindrada )

# bloque principal
# creamos el nuevo objeto, lo inicializamos y se imprime
coche = Coche("negro", 4, 5, 210, 3100)
print(coche)