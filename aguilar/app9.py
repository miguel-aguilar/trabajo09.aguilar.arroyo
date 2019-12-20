import os
import libreeria

#input
nombre=os.sys.argv[1]
apellido=os.sys.argv[2]


#pedir la funsion
nom=libreeria.pedir_nombre(nombre,apellido)

#ouput
print("==================================")
print("el nombre completo del alumno es: " + nombre + " " +  apellido)
print("estado de nombre: " + nom)
print("==================================")
