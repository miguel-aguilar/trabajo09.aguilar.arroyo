import os
import libreria

a=int(os.sys.argv[1])
b=int(os.sys.argv[2])
c=int(os.sys.argv[3])

respuesta=libreria.hallando_posibles_soluciones(a,b,c)
print("*******************************************")
print("VALOR DE a:", a)
print("VALOR DE b:", b)
print("VALOR DE c:", c)
print("RESPUESTA DE LA FORMULA GENERAL:", respuesta)
print("******************************************")
