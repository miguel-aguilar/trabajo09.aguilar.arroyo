import os
import libreeria

#input
companero=os.sys.argv[1]
cel=int(os.sys.argv[2])

#pedimos la funsion
cel=libreeria.pedir_numero_de_cel(cel)

#ouput
print ("==========================================")
print ("el numero de " + companero + " es: " + str(cel))
print ("==========================================")
