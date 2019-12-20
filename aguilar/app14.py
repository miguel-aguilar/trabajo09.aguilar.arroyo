import os
import libreeria

#input
asociado=os.sys.argv[1]
nume=int(os.sys.argv[2])

#pedir la funsion
num=libreeria.pedir_numero_de_tarejta(nume)

#ouput
print("==================================")
print("ASOCIADO           : " + asociado)
print("DEPOSITO AL NUMERO : " + str(num))
print("==================================")
