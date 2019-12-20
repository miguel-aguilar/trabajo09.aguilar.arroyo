import os
import libreeria

#input
a=int(os.sys.argv[1])
b=int(os.sys.argv[2])
c=int(os.sys.argv[3])

#llamamos a la funsion
re=libreeria.area_del_trapecio(a,b,c)

#ouput
print("==================================")
print ("el area del trapecio es: " + str(re))
print("==================================")
