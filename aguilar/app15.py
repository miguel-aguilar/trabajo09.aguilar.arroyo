import os
import libreeria

#input
velocidad=int(os.sys.argv[1])
tiempo=int(os.sys.argv[2])

#pedir la funsion
dis=libreeria.pedir_distancia(velocidad,tiempo)

#ouput
print("==================================")
print("la velocidad toma el valor de: " + str(dis))
print("==================================")
