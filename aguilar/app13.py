import os
import libreeria

#input
estudiante=os.sys.argv[1]
codigo=os.sys.argv[2]

#pedir la funsion
cod=libreeria.pedir_codigo(codigo)

#ouput
print("==================================")
print("el estudiante " + estudiante + " tiene el codigo " + cod)
print("==================================")
