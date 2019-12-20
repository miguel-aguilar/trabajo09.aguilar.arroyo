import os
import libreria

area_base=int(os.sys.argv[1])
altura=int(os.sys.argv[2])
resultado=libreria.hallar_volumn_piramide(area_base,altura)
print("*************************************")
print("El volumen de la piramide: ", resultado)
print("*************************************")
