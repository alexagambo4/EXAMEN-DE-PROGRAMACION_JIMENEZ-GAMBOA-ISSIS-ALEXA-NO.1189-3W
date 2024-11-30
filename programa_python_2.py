#se imprimen los datos de la autora 
print("Jimenez Gamboa Issis Alexa")
print("no.1189")
print("3W")
#se imprime una linea en blanco paa que se vea mas limpio
print("")
#se imprime el titulo del programa 
print("Ejercicio no.2")
#se imprime una linea en blaco 
print("")
#se imprimen las instrucciones 
print("Instrucciones: ")
print("Realizar un programa que tenga una clase Persona con las siguientes características. La clase tendrá como atributos el nombre y la edad de una persona.")
print("Implementar los métodos necesarios para inicializar los atributos, mostrar los datos e indicar si la persona es mayor de edad o no.")
#se imprime una linea en blanco para iniciar con el programa 
print("")
class Persona:
    def __init__(self, nombre, edad):
        """
        Inicializa los atributos de la persona
        :param nombre: Nombre de la persona
        :param edad: Edad de la persona
        """
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        """
        Muestra los datos de la persona.
        """
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

    def es_mayor_de_edad(self):
        """
        Verifica si la persona es mayor de edad (18 años o más)
        """
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad")
        else:
            print(f"{self.nombre} no es mayor de edad")


#ejemplo de uso
persona1 = Persona("Alexa Gamboa", 20)
persona1.mostrar_datos()
persona1.es_mayor_de_edad()
