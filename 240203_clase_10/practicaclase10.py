#Escribir un programa que abra un archivo, lea todas sus lineas y cuente cuantas lineas existen en el mismo
file = open(r"D:\Documents\curso python\prueba\PruebaGit\json\practico6_json.py")
contenido=file.readlines()
print(len(contenido))
file.close()

