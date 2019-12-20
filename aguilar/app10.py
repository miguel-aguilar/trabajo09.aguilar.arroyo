import os
import libreeria

#input
palabra=os.sys.argv[1]

#pedimos la funsion
pala=libreeria.pedir_palabra_palindroma(palabra)

#ouput
print("==================================")
print("la palabra " + palabra + pala)
print("==================================")
