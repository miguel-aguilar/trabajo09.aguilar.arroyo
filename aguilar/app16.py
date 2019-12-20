import os
import libreeria

#input
nombre=os.sys.argv[1]
fecha_de_nacimiento=os.sys.argv[2]

#pedir la funsion
dia=libreeria.pedir_fecha(fecha_de_nacimiento)

#ouput
print("==================================")
print("mi nombre es "+ nombre + " y naci un dia " + dia)
print("==================================")
