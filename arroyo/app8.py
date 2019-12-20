import os
import libreria

base_mayor=int(os.sys.argv[1])
altura=int(os.sys.argv[2])
base_menor=int(os.sys.argv[3])
resultado=libreria.area_trapecio(altura,base_menor,base_mayor)
print("*************************************")
print("El area del trapecio es: ", resultado)
print("*************************************")
