import os
import libreria

velocidad=int(os.sys.argv[1])
tiempo=int(os.sys.argv[2])

dis=libreria.detectar_excso_velocidad(velocidad,tiempo)
  #IMPRESION DE DATOS OBTENIDOS
print("**********************")
print("Velocidad= ", velocidad)
print("Tiempo= ", tiempo)
print(dis)
print("**********************")
