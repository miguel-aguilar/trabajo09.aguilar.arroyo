import os
import libreria

radio=int(os.sys.argv[1])
velocidad_angular=int(os.sys.argv[2])

dis=libreria.calcular_ACELERACION_ANGULAR(radio,velocidad_angular)
  #IMPRESION DE DATOS OBTENIDOS
print("*************************************************************")
print("Velocidad angular= ", velocidad_angular)
print("Radio= ", radio)
print("MENSAJE DE RECOMENDACION:", dis)
print("*************************************************************")
