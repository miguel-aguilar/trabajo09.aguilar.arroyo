import os
import libreeria

#input
chofer=os.sys.argv[1]
placa=os.sys.argv[2]

#pedir la funsion
plac=libreeria.pedir_placa(placa)

#ouput
print ("##################################")
print ("la placa del chofer " + chofer + " es " + plac)
print ("##################################")
