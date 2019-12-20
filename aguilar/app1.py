import os
import libreeria

#input
nom=os.sys.argv[1]
a=int(os.sys.argv[2])
b=int(os.sys.argv[3])
c=int(os.sys.argv[4])

#se pedira la funcion
prom=libreeria.promedio(a,b,c)

#ouput
print("==================================")
print("la nota promedio del alumno " + nom + " es: " + str(prom))
print("==================================")
