import os
import libreria

largo=int(os.sys.argv[1])
ancho=int(os.sys.argv[2])
altura=int(os.sys.argv[3])


resultado=libreria.volumen_hexaedro(largo,ancho,altura)
print("**************************************************************************")
print("el volumen de hexaedro es: ",resultado)
print("**************************************************************************")
