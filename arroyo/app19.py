
import os
import libreria

velinical=int(os.sys.argv[1])
aceleracion=int(os.sys.argv[2])
tiempo=int(os.sys.argv[3])

calc=libreria.calcular_velocidad_final(velinical,aceleracion,tiempo)
print("condicion: ", calc)
print("**********************")
print("Su velocidad inicial fue= ", velinical)
print("Promedio de la acelracion = ", aceleracion)
print("**********************")
