import os
import libreria

largo=int(os.sys.argv[1])
ancho=int(os.sys.argv[2])

resultado=libreria.medicion_terreno(largo,ancho)
print("**********************************************************************************************************************")
print("condicion del terreno es :", resultado)
print("**********************************************************************************************************************")
