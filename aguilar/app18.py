import os
import libreeria
#input
nombre=os.sys.argv[1]
puesto=int(os.sys.argv[2])

#pedir la funsion
pue=libreeria.pedir_puesto(puesto)

#ouput
print("===========================================================")
print("el alumno " + nombre + " " +  pue + " ingresa al consurso porque quedo en el puesto " + str(puesto))
print("===========================================================")
