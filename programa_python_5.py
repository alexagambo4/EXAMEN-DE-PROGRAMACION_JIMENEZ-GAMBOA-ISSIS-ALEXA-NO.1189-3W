#se imprimen los datos de la autora 
print("Jimenez Gamboa Issis Alexa")
print("no.1189")
print("3W")
#se imprime una linea en blanco paa que se vea mas limpio
print("")
#se imprime el titulo del programa 
print("Ejercicio no.5")
#se imprime una linea en blaco 
print("")
#se imprimen las instrucciones 
print("Instrucciones: ")
print("Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones")
print("Añadir contacto")
print("Lista de contactos")
print("Buscar contacto")
print("Editar contacto")
print("Cerrar agenda")
#se imprime una linea en blanco para iniciar con el programa 
print("")
class Agenda:
    def __init__(self):
        """
        Inicializa la agenda vacía.
        """
        self.contactos = {}

    def añadir_contacto(self, nombre, telefono, email):
        """
        Añade un nuevo contacto a la agenda
        :param nombre: Nombre del contacto
        :param telefono: Teléfono del contacto
        :param email: Email del contacto
        """
        self.contactos[nombre] = {'telefono': telefono, 'email': email}

    def lista_contactos(self):
        """
        Muestra la lista de contactos
        """
        if not self.contactos:
            print("La agenda está vacía")
        else:
            for nombre, datos in self.contactos.items():
                print(f"Nombre: {nombre}, Teléfono: {datos['telefono']}, Email: {datos['email']}")

    def buscar_contacto(self, nombre):
        """
        Busca un contacto por nombre
        """
        if nombre in self.contactos:
            print(f"Contacto encontrado: {nombre}, Teléfono: {self.contactos[nombre]['telefono']}, Email: {self.contactos[nombre]['email']}")
        else:
            print("Contacto no encontrado")

    def editar_contacto(self, nombre, telefono=None, email=None):
        """
        Edita los datos de un contacto
        :param nombre: Nombre del contacto
        :param telefono: Nuevo teléfono (opcional)
        :param email: Nuevo email (opcional)
        """
        if nombre in self.contactos:
            if telefono:
                self.contactos[nombre]['telefono'] = telefono
            if email:
                self.contactos[nombre]['email'] = email
            print(f"Contacto {nombre} actualizado")
        else:
            print("Contacto no encontrada")

    def cerrar_agenda(self):
        """
        Cierra la agenda.
        """
        print("Agenda cerrada")


#ejemplo de uso
agenda = Agenda()
agenda.añadir_contacto("Alexa Gamboa", "656 203 6781", "AlexaGamboa@example.com")
agenda.añadir_contacto("Issis Jimenez", "656 203 6781", "IssisJimenez@example.com")
agenda.lista_contactos()
agenda.buscar_contacto("Alexa Gamboa")
agenda.editar_contacto("Alexa Gamboa", telefono="656 203 6781")
agenda.cerrar_agenda()
