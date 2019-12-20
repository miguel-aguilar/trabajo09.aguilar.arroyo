import os
import libreria

largo=int(os.sys.argv[1])
ancho=int(os.sys.argv[2])
generatriz=int(os.sys.argv[3])


resultado=libreria.volumen_cilindro(largo,ancho,generatriz)
print("**************************************************************************")
print("el volumen del cilindro  es: ",resultado)
print("**************************************************************************")
