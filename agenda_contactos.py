class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
    def mostrar_info(self):
        print(f"\n nombre: {self.nombre}")
        print(f"telefono: {self.telefono}")
        print(f"correo: {self.correo}")
        print("-" * 30)
class Agenda:
    def __init__(self):
        self.contactos = []
    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)
        print("contacto agregado correctamente.")
    def mostrar_contactos(self):
        if not self.contactos:
            print("no hay contactos en la agenda.")
        else:
            print("\n lista de contactos")
            print("=" * 30)
            for contacto in self.contactos:
                contacto.mostrar_info()
    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                print("contacto encontrado:")
                contacto.mostrar_info()
                return
        print("contacto no encontrado.")
agenda = Agenda()
while True:
    print("\n agenda de contactos")
    print("1. agregar contacto")
    print("2. buscar contacto")
    print("3. mostrar todos los contactos")
    print("4. salir")
    opcion = input("seleccione una opcion: ")
    if opcion == "1":
        nombre = input("nombre: ")
        telefono = input("telefono: ")
        correo = input("correo: ")
        nuevo_contacto = Contacto(nombre, telefono, correo)
        agenda.agregar_contacto(nuevo_contacto)
    elif opcion == "2":
        nombre_buscar = input("ingrese el nombre a buscar: ")
        agenda.buscar_contacto(nombre_buscar)
    elif opcion == "3":
        agenda.mostrar_contactos()
    elif opcion == "4":
        print("saliendo de la agenda...")
        break
    else:
        print("opcion invalida, intente nuevamente.")