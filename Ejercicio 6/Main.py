
class Vehiculo:
    color = ""
    Ruedas = None
    Puertas = None

    def cambiarNumRuedas(self, ruedas):
        self.Ruedas = ruedas
    def cambiarNumPuertas(self, puertas):
        self.Puertas = puertas

class Coche(Vehiculo):
    Velocidad = 210
    Cilindrada = 3100


c = Coche()
c.cambiarNumRuedas(4)
c.cambiarNumPuertas(5)
print("El coche tiene", c.Ruedas, "ruedas")
print("El coche tiene", c.Puertas, "puertas")