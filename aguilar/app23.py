import os
import libreeria

#input
variacion=int(os.sys.argv[1])
tiempo=int(os.sys.argv[2])

#pedir la funsion
ace=libreeria.pedir_aceleracion(variacion,tiempo)

#ouput
print("==================================")
print("la aceleracion es: " + str(ace))
print("==================================")
