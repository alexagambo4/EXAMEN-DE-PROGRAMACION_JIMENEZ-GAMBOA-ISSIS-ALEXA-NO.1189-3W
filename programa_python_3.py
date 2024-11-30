#se imprimen los datos de la autora 
print("Jimenez Gamboa Issis Alexa")
print("no.1189")
print("3W")
#se imprime una linea en blanco paa que se vea mas limpio
print("")
#se imprime el titulo del programa 
print("Ejercicio no.3")
#se imprime una linea en blaco 
print("")
#se imprimen las instrucciones
print("Instrucciones: ") 
print("Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para inicializar los atributos, imprimir el valor del")
print("lado con un tamaño mayor y  el tipo de triángulo que es (equilátero, isósceles o escaleno).")
#se imprime una linea en blanco para iniciar con el programa 
print("")
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        """
        Inicializa los lados del triángulo.
        :param lado1: Primer lado del triángulo
        :param lado2: Segundo lado del triángulo
        :param lado3: Tercer lado del triángulo
        """
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def imprimir_lado_mayor(self):
        """
        Imprime el lado con el tamaño mayor del triángulo
        """
        mayor = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado mayor es: {mayor}")

    def tipo_triangulo(self):
        """
        Determina el tipo de triángulo según la igualdad de sus lados
        """
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero")
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            print("El triángulo es isósceles.")
        else:
            print("El triángulo es escaleno")


#ejemplo de uso
triangulo1 = Triangulo(5, 5, 8)
triangulo1.imprimir_lado_mayor()
triangulo1.tipo_triangulo()
