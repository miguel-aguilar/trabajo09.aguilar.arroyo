import os
import libreria

nombre=os.sys.argv[1]
nacimiento=int(os.sys.argv[2])

anos=libreria.hallar_edad(nombre,nacimiento)

print("****************************")
print(anos)
print("****************************")

