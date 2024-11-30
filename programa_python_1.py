#se imprimen los datos de la autora 
print("Jimenez Gamboa Issis Alexa")
print("no.1189")
print("3W")
#se imprime una linea en blanco paa que se vea mas limpio
print("")
#se imprime el titulo del programa 
print("Ejercicio no.1")
#se imprime una linea en blaco 
print("")
#se imprimen las instrucciones
print("Instrucciones: ")
print("Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno.")
print("Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.")
#se imprime una linea en blanco para iniciar con el programa 
print("")

class Alumno:
    def __init__(self, nombre, nota):
        """
        Inicializa los atributos de la clase
        :param nombre: Nombre del alumno
        :param nota: Nota del alumno
        """
        self.nombre = nombre
        self.nota = nota

    def imprimir_datos(self):
        """
        Imprime los datos del alumno.
        """
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    def resultado(self):
        """
        Muestra el resultado del alumno dependiendo de su nota
        Si la nota es mayor o igual a 5, el alumno aprueba
        """
        if self.nota >= 5:
            print("Aprobado")
        else:
            print("Reprobado")


#ejemplo de uso
alumno1 = Alumno("Alexa Gamboa", 8)
alumno1.imprimir_datos()
alumno1.resultado()
