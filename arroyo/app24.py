import os
import libreria

diagonal_mayor=int(os.sys.argv[1])
diagonal_menor=int(os.sys.argv[2])
resultado=libreria.area_rombo(diagonal_menor,diagonal_mayor)
print("*************************************")
print("El area del rombo es: ", resultado)
print("*************************************")
