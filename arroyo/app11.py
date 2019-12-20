import os
import libreria

fuerza=int(os.sys.argv[1])
aceleracion=int(os.sys.argv[2])


calc=libreria.calcular_tranjohecho(fuerza,aceleracion)
print(calc)
print("**********************")
print("Fuerza utilizada en Newton= ", fuerza)
print("Aceleracion empleada = ", aceleracion)
print("**********************")
