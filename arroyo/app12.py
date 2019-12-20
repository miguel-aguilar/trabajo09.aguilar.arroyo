import os
import libreria

velocidad=int(os.sys.argv[1])
tiempo=int(os.sys.argv[2])

dis=libreria.calcular_distacia_recorrida(velocidad,tiempo)
  #IMPRESION DE DATOS OBTENIDOS
print("*************************************************************")
print("Velocidad= ", velocidad)
print("Tiempo= ", tiempo)
print("MENSAJE DE RECOMENDACION:", dis)
print("*************************************************************")

