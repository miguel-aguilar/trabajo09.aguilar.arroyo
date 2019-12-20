import os
import libreeria

#input
nombre=os.sys.argv[1]
dni=int(os.sys.argv[2])

#pedimos la funsion
dni=libreeria.pedir_dni(dni)

#ouput
print ("#########################")
print ("# CLIENTE:    " + nombre)
print ("# DNI    :    " + str(dni))
print ("#########################")
