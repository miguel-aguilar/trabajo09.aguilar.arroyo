import os
import libreeria

#input
pasajero=os.sys.argv[1]
asiento=int(os.sys.argv[2])

#pedir la funsion
asi=libreeria.pedir_asiento(asiento)

#ouput
print ("###############################")
print ("# pasajero      : " + pasajero)
print ("# asiento       : " + str(asi))
print ("###############################")
