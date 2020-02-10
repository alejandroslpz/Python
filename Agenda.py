import os

CARPETA = 'contactos/'  # carpeta de contactos
EXTENSION = '.txt'  # Extensión de archivos

# Contactos


class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria


def agenda():

    crear_directorio()  # Revisar si la carpeta existe o no
    mostrar_menu()  # Mostrar menu

    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opcion: \r\n')
        opcion = int(opcion)

        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            ver_contacto()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False


def agregar_contacto():
    print('Escribe los datos del nuevo contacto')
    nombre_contacto = input('Nombre del contacto: \r\n')

    existe = existe_contacto(nombre_contacto)

    if not existe:

        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:

            # resto de los campos
            telefono_contacto = input('Agrega el teléfono: \r\n')
            categoria_contacto = input('Agrega una categoria: \r\n')

            # instanciar la clase
            contacto = Contacto(
                nombre_contacto, telefono_contacto, categoria_contacto)

            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

            print('\r\nContacto creado correctamente\r\n')
    else:
        print('Ese contacto ya existe\r\n')

    agenda()


def editar_contacto():
    nombre_anterior = input('Nombre del contacto que desea editar: \r\n')

    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
            nombre_contacto = input('Agrega el nuevo nombre: \r\n')
            telefono_contacto = input('Agrega el nuevo teléfono: \r\n')
            categoria_contacto = input('Agrega la nueva categoria: \r\n')

            contacto = Contacto(
                nombre_contacto, telefono_contacto, categoria_contacto)

            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

            os.rename(CARPETA + nombre_anterior + EXTENSION,
                      CARPETA + nombre_contacto + EXTENSION)

            print('\r\nContacto editado correctamente\r\n')
    else:
        print('Ese contacto no existe')

    agenda()


def ver_contacto():
    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')


def buscar_contacto():
    nombre = input('Seleccione el contacto que desea buscar: \r\n')

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Información del contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')

    except IOError:
        print('El archivo no existe')
        print(IOError)

    agenda()


def eliminar_contacto():
    nombre = input('Selecciona el contacto que quieres eliminar: \r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\nEl contacto ha sido eliminado')

    except:
        print('No existe ese contacto')
    
    agenda()


def mostrar_menu():
    print('Selecciona una opción del menu: \n')
    print('1) Agregar nuevo contacto')
    print('2) Editar Contacto')
    print('3) Ver contactos')
    print('4) Buscar Contacto')
    print('5) Eliminar contacto')


def crear_directorio():
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)  # crear carpeta


def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)


agenda()
