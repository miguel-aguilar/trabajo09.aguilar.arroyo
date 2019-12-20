import os
import libreria

velocidad=int(os.sys.argv[1])
tiempo=int(os.sys.argv[2])

dis=libreria.calcular_aceleracion_auto(velocidad,tiempo)
  #IMPRESION DE DATOS OBTENIDOS
print("**********************")
print("velocidad= ", velocidad)
print("Tiempo= ", tiempo)
print(dis)
print("**********************")

