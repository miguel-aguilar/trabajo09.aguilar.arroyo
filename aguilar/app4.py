import os
import libreeria
#input
cliente=os.sys.argv[1]
ruc=int(os.sys.argv[2])

#pedimos la funsion
ruc=libreeria.pedir_ruc(ruc)

#ouput
print ("#########################")
print ("# CLIENTE:    " + cliente)
print ("# RUC    :    " + str(ruc))
print ("#########################")
