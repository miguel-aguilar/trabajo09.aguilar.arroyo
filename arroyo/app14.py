import os
import libreria

trabajo=int(os.sys.argv[1])
tiempo=int(os.sys.argv[2])

dis=libreria.calcular_potencia(trabajo,tiempo)
  #IMPRESION DE DATOS OBTENIDOS
print("**********************")
print("trabajo= ", trabajo)
print("Tiempo= ", tiempo)
print(dis)
print("**********************")
