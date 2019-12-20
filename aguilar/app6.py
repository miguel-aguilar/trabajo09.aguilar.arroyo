import os
import libreeria

#input
jugador=os.sys.argv[1]
bol1=int(os.sys.argv[2])
bol2=int(os.sys.argv[3])

#pedimos la funcion
res=libreeria.pedir_bolillas(bol1,bol2)

#ouput
print("===========================================")
print("JUGADOR    :  " + jugador)
print("BOLILLAS   :  " + str(res))
print("===========================================")
