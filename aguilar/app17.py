import os
import libreeria

#input
clave=int(os.sys.argv[1])

#pedir la funsion
cla=libreeria.pedir_clave(clave)

#ouput
print("==================================")
print("la clave de mi tarjeta de credito es " + str(cla))
print("==================================")
