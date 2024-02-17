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

def agregar_alumno(nombre, apellido, dni, fecha_nac, tutor):
    return Alumno(nombre, apellido, dni, fecha_nac, tutor)

def datos_iniciales(alumno, notas, faltas, amonestaciones):
    alumno.ingresar_nota(notas)
    for _ in range(faltas):
        alumno.asignar_falta()
    alumno.amonestaciones = amonestaciones 

def mostrar_alumno(alumno):
    print("Datos del Alumno: ")
    print(alumno)

def mostrar_alumnos(alumnos):
    for i, alumno in enumerate(alumnos, 1):
        print(f"Alumno {i}:")
        mostrar_alumno(alumno)

def modificar_datos(alumno, notas=None, faltas=None, amonestaciones=None):
    if notas:
        alumno.ingresar_nota(notas)
    if faltas:
        for _ in range(faltas):
            alumno.asignar_falta()
    if amonestaciones:
        alumno.amonestaciones = amonestaciones

def expulsar_alumno(alumnos, alumno):
    alumnos.remove(alumno)
    print(f"Alumno {alumno.nombre} {alumno.apellido} expulsado.")

def guardar(alumnos):
    alumnos_data = []
    for alumno in alumnos:
        alumno_data = {
            "Nombre": alumno.nombre,
            "Apellido": alumno.apellido,
            "DNI": alumno.dni,
            "Fecha de Nacimiento": alumno.fecha_nac,
            "Tutor": alumno.tutor,
            "Notas": alumno.notas,
            "Faltas": alumno.faltas,
            "Amonestaciones": alumno.amonestaciones
        }
        alumnos_data.append(alumno_data)

    with open("alumnos.json", "w") as archivoalumnos:
        json.dump(alumnos_data, archivoalumnos)
     
def cargar():
    try:
        with open("alumnos.json", "r") as archivoalumnos:
            data = json.load(archivoalumnos)
            alumnos = []
            for alumno_data in data:
                alumno = Alumno(alumno_data["Nombre"], alumno_data["Apellido"], alumno_data["DNI"], alumno_data["Fecha de Nacimiento"], alumno_data["Tutor"])
                alumno.notas = alumno_data["Notas"]
                alumno.faltas = alumno_data["Faltas"]
                alumno.amonestaciones = alumno_data["Amonestaciones"]
                alumnos.append(alumno)
            return alumnos
    except FileNotFoundError:
        return []

alumnos = cargar()

if not alumnos:
    alumnos.append(agregar_alumno("Ana", "Torres", 55234123, "19/11/2000", "Juan Guzman"))
    alumnos.append(agregar_alumno("Facundo", "Guzman", 87154253, "17/10/2000", "Yolanda Jaime"))

datos_iniciales(alumnos[0], [8, 7, 7], 2, 1)
datos_iniciales(alumnos[1], [10, 8, 5], 1, 10)

guardar(alumnos)

mostrar_alumnos(alumnos)

modificar_datos(alumnos[0], notas=[6, 8, 9], faltas=1, amonestaciones=2)

mostrar_alumnos(alumnos)

expulsar_alumno(alumnos, alumnos[0])

mostrar_alumnos(alumnos)
