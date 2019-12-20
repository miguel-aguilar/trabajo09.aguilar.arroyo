import os
import libreeria

#input
fuerza=int(os.sys.argv[1])
area=int(os.sys.argv[2])

#pedir la funsion
presion=libreeria.pedir_presion(fuerza,area)

#ouput
print("==================================")
print("la presion toma por valor: " + str(presion))
print("==================================")
