import os
import libreeria

#input
paciente=os.sys.argv[1]
temp=int(os.sys.argv[2])

#pedir la funsion
tm=libreeria.pedir_temperatura(temp)

#ouput
print("==================================")
print("el paciente " + paciente + " tiene una temperatura " + tm + " porque es de " + str(temp))
print("==================================")
