import os
import libreeria

#input
nombre=os.sys.argv[1]
edad=int(os.sys.argv[2])

#pedimos la funsion
edad=libreeria.pedir_edad(edad)

#ouput
print("==================================")
print ("la edad de " + nombre + " es: " + str(edad))
print("==================================")
