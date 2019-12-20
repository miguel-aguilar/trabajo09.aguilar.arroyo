import os
import libreria

masa=int(os.sys.argv[1])
volumen=int(os.sys.argv[2])

dis=libreria.calcular_densidad(masa,volumen)
  #IMPRESION DE DATOS OBTENIDOS
print("*************************************************************")
print("Velocidad= ", masa)
print("Tiempo= ", volumen)
print("DESCRIPCION BREVE:", dis)
print("*************************************************************")
