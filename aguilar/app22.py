import os
import libreeria

#input
fuerza=int(os.sys.argv[1])
distancia=int(os.sys.argv[2])

#pedir la funsion
tra=libreeria.pedir_trabajo(fuerza,distancia)

#ouput
print("==================================")
print("el trabajo vota un resultado: " + str(tra))
print("==================================")
