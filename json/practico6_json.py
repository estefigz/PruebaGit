import json

def agregar_alumnos(alumnos, Nombre, Apellido, DNI, Fecha_Nac, Nombre_Tutor):
    Alumno = { 
        "Nombre": Nombre,
        "Apellido": Apellido,
        "DNI": DNI,
        "Fecha de Nacimiento": Fecha_Nac,
        "Tutor": Nombre_Tutor,
        "Notas": [],
        "Faltas": 0,
        "Amonestaciones": 0
    }
    alumnos.append(Alumno)
    return alumnos

def datos_iniciales(Alumno, notas, faltas, amonestaciones):
     Alumno["Notas"] = notas
     Alumno["Faltas"] = faltas
     Alumno["Amonestaciones"] = amonestaciones 

def mostrar_alumno(Alumno):
    print("Datos del Alumno: ")
    for key, value in Alumno.items():
            print(f"{key}:{value}")

def mostrar_alumnos(alumnos):
    for i in range(len(alumnos)):
         print(f"Alumno {i+1}:")
         mostrar_alumno(alumnos[i])

def modificar_datos(Alumno, notas=None, faltas=None, amonestaciones=None ):
    if notas:
        Alumno["Notas"] = notas
    if faltas:
        Alumno["Faltas"] = faltas
    if amonestaciones:
        Alumno["Amonestaciones"] = amonestaciones

def expulsar_alumno(alumnos, Alumno):
     alumnos.remove(Alumno)
     print(f"Alumno {Alumno ['Nombre']} expulsado.")

def guardar(alumnos):
    with open ("alumnos.json" , "w") as archivoalumnos:
        json.dump(alumnos, archivoalumnos)
     
def cargar():
     try:
          with open ("alumnos.json" , "r") as archivoalumnos:
            return json.load(archivoalumnos)
    except FileNotFoundError:
        return []
     
alumnos = cargar()

if not alumnos:
    alumnos= agregar_alumnos(alumnos, "Ana","Torres",55234123,"19/11/2000","Juan Guzman")
    alumnos=agregar_alumnos(alumnos, "Facundo" , "Guzman", 87154253, "17/10/2000", "Yolanda Jaime")

datos_iniciales(alumnos[0], [8, 7, 7] , 2 , 1)
datos_iniciales(alumnos[1], [10,8,5], 1 , 10)

guardar(alumnos)

mostrar_alumnos(alumnos)

modificar_datos(alumnos[0], notas=[6, 8, 9], faltas=1, amonestaciones=2)

mostrar_alumnos(alumnos)

expulsar_alumno(alumnos, alumnos[0])

mostrar_alumnos(alumnos)
