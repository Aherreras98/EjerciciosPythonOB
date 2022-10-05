#Crear un programa con la clase Alumno y los atributos nombre y nota.
#Inicializar los atributos, imprimirlos y mostrar un mensaje con la nota y si ha aprobado o no.

class Alumno:
    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre", self.nombre)
        print("Nota", self.nota)

    def resultado(self):
        if self.nota >= 5:
            print("Ha aprobado")
        else:
            print("Ha suspendido")

alumno1 = Alumno()
alumno2 = Alumno()

alumno1.inicializar("Adrian", 4)
alumno2.inicializar("Shania", 9)
alumno1.imprimir()
alumno1.resultado()
print("")
alumno2.imprimir()
alumno2.resultado()

