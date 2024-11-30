#se imprimen los datos de la autora 
print("Jimenez Gamboa Issis Alexa")
print("no.1189")
print("3W")
#se imprime una linea en blanco paa que se vea mas limpio
print("")
#se imprime el titulo del programa 
print("Ejercicio no.4")
#se imprime una linea en blaco 
print("")
#se imprimen las instrucciones
print("Instrucciones: ") 
print("Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división.")
print("Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.")
#se imprime una linea en blanco para iniciar con el programa 
print("")
class Calculadora:
    def __init__(self, valor1, valor2):
        """
        Inicializa los valores para las operaciones
        :param valor1: Primer valor entero
        :param valor2: Segundo valor entero
        """
        self.valor1 = valor1
        self.valor2 = valor2

    def suma(self):
        """
        Realiza la suma de los dos valores
        """
        return self.valor1 + self.valor2

    def resta(self):
        """
        Realiza la resta de los dos valores
        """
        return self.valor1 - self.valor2

    def multiplicacion(self):
        """
        Realiza la multiplicación de los dos valores
        """
        return self.valor1 * self.valor2

    def division(self):
        """
        Realiza la división de los dos valores
        Si el segundo valor es 0, muestra un mensaje de error
        """
        if self.valor2 == 0:
            return "Error: División por cero"
        else:
            return self.valor1 / self.valor2


#ejemplo de uso
calculadora = Calculadora(10, 5)
print(f"Suma: {calculadora.suma()}")
print(f"Resta: {calculadora.resta()}")
print(f"Multiplicación: {calculadora.multiplicacion()}")
print(f"División: {calculadora.division()}")
