import os
import libreria

#INPUT
dni=int(os.sys.argv[1])

#PEDIR LA FUNCION
ped=libreria.pedir_dni(dni)

#OUPUT
print("***********************")
print("el dni es: ", ped)
print("************************")
