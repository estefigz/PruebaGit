#Estrucutrar correctamente la clase alumno:
#Esta podria tener, ademas de los parametros que alamacenaran la infomacion del alumno, metodos que le permitan ingresar una nueva nota, asignar una falta, asignar una amonestacion, 
#cambiar domicilio (puede considerar agregar otros datos relevantes) .
#Modificar el repositorio agregando todo lo que considere necesario y reenviar el link.
import json

class Alumno:
    def __init__(self, nombre, apellido, dni, fecha_nac, tutor):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fecha_nac = fecha_nac
        self.tutor = tutor
        self.notas = []
        self.faltas = 0
        self.amonestaciones = 0
    
    def ingresar_nota(self, nota):
        self.notas.append(nota)
    
    def asignar_falta(self):
        self.faltas += 1
    
    def asignar_amonestacion(self):
        self.amonestaciones += 1
    
    def modificar_datos(self, notas=None, faltas=None, amonestaciones=None):
        if notas is not None:
            self.notas = notas
        if faltas is not None:
            self.faltas = faltas
        if amonestaciones is not None:
            self.amonestaciones = amonestaciones
    
    def expulsar(self):
        print(f"Alumno {self.nombre} {self.apellido} expulsado.")
    
    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}\nDNI: {self.dni}\nFecha de Nacimiento: {self.fecha_nac}"

def cargar():
    try:
        with open("alumnos.json" , "r") as archivoalumnos:
            data = json.load(archivoalumnos)
            alumnos = []
            for alumno_data in data:
                alumno = Alumno(alumno_data["Nombre"], alumno_data["Apellido"], alumno_data ["DNI"], alumno_data ["Fecha de Nacimiento"], alumno_data ["Tutor"])
                alumno.notas = alumno_data["Notas"]
                alumno.faltas = alumno_data["Faltas"]
                # Usar get() para acceder a la clave de manera segura con un valor predeterminado de 0
                alumno.amonestaciones = alumno_data.get("amonestaciones", 0)
                alumnos.append(alumno)
            return alumnos
    except FileNotFoundError:
        return []

def guardar (alumnos):
    data = []
    for alumno in alumnos:
        alumno_data = {
            "Nombre": alumno.nombre,
            "Apellido": alumno.apellido,
            "DNI": alumno.dni,
            "Fecha de Nacimiento": alumno.fecha_nac,
            "Tutor": alumno.tutor,
            "Notas": alumno.notas,
            "Faltas": alumno.faltas,
            "amonestaciones": alumno.amonestaciones
        }
        data.append(alumno_data)
    with open("alumnos.json", 'w') as archivoalumnos:
        json.dump(data, archivoalumnos)

alumnos = cargar()

if not alumnos:
    alumnos.append(Alumno("Ana", "Torres", "55234123", "19/11/2000", "Juan Guzman"))
    alumnos.append(Alumno("Facundo", "Guzman", "87154253", "17/10/2000", "Yolanda Jaime"))

alumnos[0].ingresar_nota(9)
alumnos[0].ingresar_nota(7)
alumnos[0].ingresar_nota(4)
alumnos[0].asignar_falta()
alumnos[0].asignar_amonestacion()

alumnos[1].ingresar_nota(8)
alumnos[1].ingresar_nota(8)
alumnos[1].ingresar_nota(8)
alumnos[1].asignar_falta()

guardar(alumnos)

for i, alumno in enumerate(alumnos, 1):
    print(f"Alumno {i}:")
    print(alumno)

alumnos[0].modificar_datos(notas=[4 , 4 ,4], faltas=6, amonestaciones=2)
alumnos[1].modificar_datos(notas=[6, 6, 6], faltas=2, amonestaciones=1)

for i, alumno in enumerate(alumnos, 1):
    print(f"Alumno {i} despues de modificar datos: ")
    print(alumno)

alumnos[0].expulsar()
alumnos.pop(0)

for i, alumno in enumerate(alumnos, 1):
    print(f"Alumno {i} despues de modificar datos: ")
    print(alumno)
