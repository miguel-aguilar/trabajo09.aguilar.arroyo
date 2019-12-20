#EJERCICIO NUMERO 1
#EN ESTE EJERCICIO PEDIREMOS EL DNI DE LA PERONAS
#NO DEBE SER DIFERENTE DE UN NUMERO Y NO SOBREPASAR LOS 8 DIGITOS,

def pedir_dni(dni):
    if (len(str(dni)) != 8):
        mensa="el DNI es falso"
        return mensa
    else:
        return dni

################################################################################

#EJERCICIOS NUMERO 2
#EN ESTE EJERCICIO PEDIREMOS UN CODIGO PARA PODER ACCEDER A LA CUENTA GOOGLW
#EL CODIGO NO DEBE PASAR LOS 6 DIGTTOS, DE LO CONTRARIO VOLVERA A PEDIR EL CODIGO

################################################################################

def pedir_codigo_google(codigo):
    if(len(str(codigo)) == 6):
        print("el codigo es correcto")
    else:
        print("el codigo es incorrecto")
    return codigo

################################################################################

#EJERCICIO NUMERO 3
#EN ESTE EJERCCIO NOS AYUDARA A CALCULAR LA EDAD DE CUALQUIER PERSONA
#PARA CALCULAR LA EDAD HALLAREMOS LA DIFERENCIA ENTRE LA FECHA ACTUAL Y LA DE SU NACIMIENTO
def hallar_edad(nombre,nacimiento):
    #DEFINIREMOS EL NOMBRE CON MAYUSCULA AL MOMENTO DEL PRINT
    nombre=nombre.upper()
    #CALCULAMOS LA EDAD MEDIANTE OPERACION DE DIFERENCIA
    edad=2019-nacimiento
    edad_calculada="La edad de "+ nombre+" es: "+str(edad)
    return edad_calculada

################################################################################

#EJERCICIO NUMERO 4
#EN ESTE EJRCICO HALLAREMOS LA TABAL DE MULTIPLICA DE CUALQUIER NUMERO
#LA TABLA SERA DESDE EL UNO HASTA EL 12

def tabla_multiplicar(n):
    #DEFINIMOS EL RANGO DE MULTIPLICIDAD
    for i in range(1,13):
        #DEFINIMOS LA FORMA EN QUE IRA IMPRESO
        print("ªª ",n,"*",i,"=",i*n, "ªª")
    return n

################################################################################

#EJERCICIO NUMERP  5
#EN ESTE EJERCICIO RESOLVERMOS EL FACTORIAL DE CUALQUIER NUMERO
#EL FACTORIAL CONSISTE EN LA MULTIPLICACION DE UN NUMEROS POR SU MISMO NUMEROS DISMINUIDO EN UNO,
# ASI SUCESIVAMENTE HASTA LLEGAR A UNO

def factorial_numero(m):
    factorial=1
    #VERIFICAMOS QUE EL NUMERO SEA DIFERENTE DE CERO , CASO CONTRARIO NO TENDRIA SENTIDO EL FACTORIAL
    while m>0:
        factorial=factorial*m
        m -=1
    return factorial

################################################################################

#EJERCICIO NUMERO 6
#ESTE EJERCICIO COSNISTE EN SEPARAR LAS PALABRAS QUE COMIENZEN CON minuscula CON LAS PALABRAS QUE COMIENZEN CON MAYUSCULAS
#INTRODUCIMOS CUALQUIER PALABA Y EL PROGRAMA LAS SEPARARA

def separandor_de_mayusculas_minusculas(lista):
    #ESTABLECEMOS LISTAS, DONDE SE GUARDARAN LAS PALABRAS YA SEPARADAS
    mayuscula=[]
    minuscula=[]
    for i in lista:
        #VERIFICAMOS QUE LAS PALABRAS QUE COMIENZEN CON CUALQUIER LETRA MINUSCULA SE TRASLADEN A LAS LISTA minuscula
        if (i[0:1]=="a" or i[0:1]=="b" or i[0:1]=="c" or i[0:1]=="d" or i[0:1]=="e" or i[0:1]=="f" or
        i[0:1]=="g" or i[0:1]=="h" or i[0:1]=="i" or i[0:1]=="j" or i[0:1]=="k" or i[0:1]=="l" or
        i[0:1]=="m" or i[0:1]=="n" or i[0:1]=="o" or i[0:1]=="p" or i[0:1]=="q" or i[0:1]=="r" or
        i[0:1]=="s" or i[0:1]=="t" or i[0:1]=="y" or i[0:1]=="w" or i[0:1]=="z"):
            minuscula.append(i)
        else:
            #CASO CONTRARIO SE BASEARAN A LA LISTA mayuscula
            mayuscula.append(i)
    return minuscula,mayuscula

################################################################################

#EJERCICIO NUMERO 7
#EN ESTE EJERCICIO NOS PEDIRA EL NOMBRE DE UNA PERSONAS
#SI SI INTRODUCE UN NUMERO, APARECERA FALSE
def letra(valor):
    #ESTABLECEMSO QUE VALOR ES UNA CADENA
    if (valor!=valor.isalpha()):
        respu=("Los signos introducidos son correctos, puede acceder señor", valor)
    else:
        respu=("La palabra es incorrecta, verifique bien sus signos :", valor)
    return respu

################################################################################

#EJERCICIO NUMERO 8
#EN ESTE EJERCICO CALCULAREMOS EL AREA DE UN TRAPECIO
#EL AREA DE UN TRAPECIO SE HALLA CON LOS DATOS DE ALTURA, BASE MAYOR Y BASE MENOR
def area_trapecio(base_mayor, altura,base_menor):
    #ESTABLECEMOS LA FORMULA PARA HALLA EL AREA
    resultado=(int(base_mayor)+int(base_menor)*altura)/2
    return resultado
area_trapecio(base_mayor=10,base_menor=23,altura=32)

################################################################################

#EJERCICIO NUMERO 9
#EN ESTE EJERCICIO HALLAREMOS LA MEDIDA DE UN TERRENO
#EL AREA DE ESTABLECE EN METROS CUADRADOS, LOS DATOS PARA HALLA EL AREA ES; LARGO Y ANCHO

def medicion_terreno(largo,ancho):
    #ESTABLECEMOS LA FORMAULA PARA HALLAR EL AREA AUTOMATICAMENTE
    area=largo*ancho
    #ESTABLECEMOS CONCION PARA CLASIFICAR EL TERRENO; TERRENO COMERCIAL Y TERRENO DE USO DOMESTICO
    if (area<100):
        mensa="El terreno es para uso domestico(construccion para casa familiar) y  La medida del terreno en metros cuadrados es: ", area

    else:
        mensa="El terreno esta acto para contruccion de centros comerciales y La medida del terreno en metros cuadrados es: ", area

    return mensa

################################################################################

#EJERCICIO NUMERO 10
#EN ESTE EJERCICO HALLAREMOS EL VOLUMEN DE CUALQUIER HEXAEDRO TENIENDO LOS DATOS
#DATOS PARA OBTENER EL HEXAEDRO; LARGO, ANCHO Y ALTURA
def volumen_hexaedro(largo,ancho,altura):
    volumen=largo*ancho*altura
    #SI EL HEXAEDRO ES MAYOR 500 ENTONCES SIRVIRA PARA CONTENER MAS DE MIL LITROS DE AGUA
    if (volumen>500):
         print("Puede contener mil litros de agua y el volumen del hexaedro es: ", volumen)
    else:
        #SI EL VOLUMEN DEL EHEXAEDRO ES MENOR A 500 NO ESTA ACTO PARA CONTENER UN LIQUIDO
        print("No esta acto, para contener liquidos ya que su volumen es: ", volumen)
    return volumen

################################################################################

#EJERCICIO NUMERO 11
#ESTE EJERCICIO CONSISTE EN HALLAR EL TRABAJO Y MOSTRALE UN MENSAJE SEGUN LA CANTIDA DE TRABAJO RESULTANTE
#ESTA CALCULADORA HALLA EL TRABAJOREALIZADO
def calcular_tranjohecho(fuerza,aceleracion):
    #DEFINIMOS LA FORMULA DE TRABAJO
    trabajo=fuerza*aceleracion
    if (trabajo>100):
        msg="Ustes es un trabajador muy eficiente "
    else:
        msg="Debe esforzarse mas"
    trabajo_calculado="el trabajo es; ", trabajo
    return msg

################################################################################

#EJERCICIO NUMERO 12
#EN ESTE EJERCICO CALCULAREMOS LA DISCTANCIA DE CUALQUIER VEHICULO QUE HALLA RECORRIDO
#PARA HALLAR LA DISTANCIA NECESITAREMOS LA VELOCIDAD Y EL TIEMPO
def calcular_distacia_recorrida(velocidad,tiempo):
    distancia=velocidad*tiempo
    #SI LA DISTANCIA ES MAYOR A 800 LE SALDRA UN MENSAJE DE ALIENTO; Ha recorrido un muy buen trayecto
    if (distancia>800):
        mensaje="Ha recorrido un muy buen trayecto y su distancia es: ", distancia
    #CASO COTRARIO LE MOSTRARA QUE DEBE RECORRER MAS LUGARES
    else:
        mensaje="Maneje, y conosca mas lugares y su distancia es: ", distancia

    return mensaje

################################################################################

#EJERCICIO NUMERO 13
#EN ESTE EJERCICO CALCULAREMOS LA DISCTANCIA DE CUALQUIER VEHICULO QUE HALLA RECORRIDO
#PARA HALLAR LA DISTANCIA NECESITAREMOS LA VELOCIDAD Y EL TIEMPO
def calcular_aceleracion_auto(velocidad,tiempo):
    aceleracion=(velocidad)/tiempo
    #SI LA DISTANCIA ES MAYOR A 800 LE SALDRA UN MENSAJE DE ALIENTO; Ha recorrido un muy buen trayecto
    if (aceleracion>100):
        mensaje="Usted esta infrinfiendo la ley ya que su aceleracion es: ", aceleracion
    #CASO COTRARIO LE MOSTRARA QUE DEBE RECORRER MAS LUGARES
    else:
        mensaje="Usted es un muy buen ciudadano, sigua asi y su aceleracion aproximadamente es", aceleracion

    return mensaje

################################################################################

#EJERCICIO NUMERO 14
#EN ESTE EJERCICO CALCULAREMOS LA POTENCIA DE UN MOTOR
#PARA HALLAR LA POTENCIA SE NECECISTA DOS VARIABLES; TRABAJO Y TIEMPO
def calcular_potencia(trabajo,tiempo):
    potencia=trabajo/tiempo
    #DEFINIMOS UNA FORMULA
    if (potencia>50):
        mensaje="La potencia de su motor es optimo, numericamente es igual a: ", potencia
    #CASO COTRARIO LE MOSTRARA QUE DEBE RECORRER MAS LUGARES
    else:
        mensaje="Usted deberia cambiar su motor, La potencia de su motor es", potencia

    return mensaje

################################################################################

#EJERCICIO NUMERO 15
#EN ESTE INTERESANTE EJERCICIO NOS HALLARAN LOS NOMBRES QUE COMIENCEN CON LAS LETRAS A,B,C;D;F,G Y LAS PONDRA EN UNA LISTA
#LOS DEMAS NOMBRES SOBRANTES SE BASEARAN EN OTRA LISTA
def separandor_de_normabres_porinicial(lista):
    #ESTABLECEMOS LAS LISTA
    aletra=[]
    gletra=[]
    for i in lista:
        #VERIFICAMOS QUE LOS NOMBRES COMIENCEN CON LAS LETRAS A,B,C;D;F,G PARA UBICARLAS EN UNA LISTA APARTE DE LOS DEMAS NOMBRES
        if (i[0:1]=="A" or i[0:1]=="B" or i[0:1]=="C" or i[0:1]=="D" or i[0:1]=="F" or i[0:1]=="G"):
            aletra.append(i)
        #SI LOS NOMBRES NO COMIENZAN CON LAS LETRAS ESTABLECIDAS SE BASEARAN EN OTRA LSTA
        else:
            gletra.append(i)
    return gletra,aletra

################################################################################

#EJERCICIO NUMERO 16
#EN ESTE EJERCICIO HALLAREMOS LAS POSIBLES SOLUCIONES, CON LA FORMULA GENERAL
#LA FORMULA GENERA SE ESTABLECE CON b(cuadraro) -4ac, lo cual me dara unas posibles soluciones
def hallando_posibles_soluciones(a,b,c):
    #Establecemos la formula general
    valor=(float(b)**2)-4*float(a)*float(c)
    if valor < 0:
        return "No hay solucion"
    #SI EL RESULTADO ES MENOR A CERO NO HAY POSIBLES SOLUCIONES

    elif valor==0:
        x1=-1*float(b)/(2*float(a))
        return x1
    #SI EL RESULTADO ES MAYOR A CERO Y HAY RESULTADO
    else:
        x1=(-1*float(b)+valor**(0.5))/(2*float(a))
        x2=(-1*float(b)-valor**(0.5))/(2*float(a))
        return x1,x2
    #TAMBIEN HABRA RESULTADOS
    return valor

################################################################################

#EJERCICIO NUMERO 17
#EN ESTE EJERCICIO DETECTAREMOS EL EXCESO DE VELOCIDAD
#PARA HALLAR LA VELOCIDAD SE NECESITA DISTNACI Y TIEMPO
def detectar_excso_velocidad(distancia,tiempo):
    velocidad=distancia/tiempo
    #USAMOS LA CONDICION SOBRE LA VELOCIDAD, SI SOBREPASA LOS 300 KM/H ES EXCESO DE VELOCIDAD
    if (velocidad>800):
        mensaje="La velocidad es muy acta, sobrepasa los limites, segun figuera su velocidad es :", velocidad

    #CASO COTRARIO LE MOSTRARA QUE DEBE RECORRER MAS LUGARES
    else:
        mensaje="Excelente conductor, su velocidad figura es :", velocidad

    return mensaje

################################################################################

#EJERCICIO NUMERO 18
#ESTE EJERCICIO CONSISTE EN MULTIPLICAR LAS ORACIONES, CUNATAS VECES QUERRAMOS
#LO HARA EN ORACIONES SEPARADAS
def palabra_rep(palabra,numero):
    var=""
    var=("\nLa palabra "+palabra+" se repitio "+str(numero)+" veces")

    for i in range (numero):
        i=palabra
        print(i)
    return var

################################################################################

#EJERCICIO NUMERO 19
#EN ESTE EJERCICO CALCULAREMOS LA VELOCIDAD FINAL
#PARA HALLAR LA VELOCIDAD FINAL=DOS VARIABLES: VELOCIDAD INICIAL,ACELERACION Y TIEMPO
def calcular_velocidad_final(velinical,aceleracion,tiempo):
    velocidaad_final=velinical+aceleracion*tiempo
    #ESTABLECEMOS UNA CONDICION
    if (velocidaad_final>50):
        mensaje="El auto es demasiado rapido , Su velocidad final fue de : ", velocidaad_final
    #ESTABLECEMOS UNA CONDICION
    else:
        mensaje="UEl auto es demasiado lento, deberia equiparlo, Su velocidad final fue", velocidaad_final

    return mensaje

################################################################################

#EJERCICIO NUMERO 20
#EN ESTE EJERCICO HALLAREMOS EL VOLUMEN DE CUALQUIER CELIENDRO
#DATOS PARA OBTENER EL CILINDRO; GENERATRIZ, LARGO,ANCHO
def volumen_cilindro(largo,ancho,generatriz):
    volumen=largo*ancho*generatriz
    #ESTABLECEMOS UNA CONDICION
    if (volumen>200):
         print("El cilindro es grande puede ser utilizado  y el volumen del cilindro es: ", volumen)
    else:
        #ESTABLECEMOS UNA CONDICION
        print("El volumen del cilindro es pequeñod ya que su volumen es: ", volumen)
    return volumen

################################################################################

#EJERCICIO NUMERO 21
#ESTE EJERCICIO CONSISTE EN CALCULAR LA DENSIDAD DE CAULQUIER PISCINA

def calcular_densidad(masa,volumen):
    densidad=(masa)/volumen
    #ESTABECEMOS UNA CONDICION
    if (densidad>100):
        msg="El objeto es demasiado denso "
    else:
        msg="El pbjeto es liviano"
    trabajo_calculado="LA densidad medida fue ; ", densidad
    return msg

################################################################################

#EJERCICIO NUMERO 22
#EN ESTE EJERCICO CALCULAREMOS LA DISCTANCIA DE CUALQUIER VEHICULO QUE HALLA RECORRIDO
#PARA HALLAR LA DISTANCIA NECESITAREMOS LA VELOCIDAD Y EL TIEMPO
def calcular_ACELERACION_ANGULAR(radio,velocidad_angular):
    ACELERACION_ANGULAR=radio*velocidad_angular
    #SI LA DISTANCIA ES MAYOR A 800 LE SALDRA UN MENSAJE DE ALIENTO; Ha recorrido un muy buen trayecto
    if (ACELERACION_ANGULAR>400):
        mensaje="El disco esta girando bastante rapido  y la revolucion por minuto es: ", ACELERACION_ANGULAR
    #CASO COTRARIO LE MOSTRARA QUE DEBE RECORRER MAS LUGARES
    else:
        mensaje="El disto estagirando demasiado lentro, quiza se deba a algun problema y la revolucion por minuto es: ", ACELERACION_ANGULAR

    return mensaje

################################################################################

#EJERCICIO NUMERP  23
#EN ESTE EJERCICIO RESOLVERMOS EL FACTORIAL DE CUALQUIER NUMERO
#EL FACTORIAL CONSISTE EN LA MULTIPLICACION DE UN NUMEROS POR SU MISMO NUMEROS DISMINUIDO EN UNO, Y SUMANDO
# ASI SUCESIVAMENTE HASTA LLEGAR A UNO Y AL VEZ SUMAND LA DIFERENCIA

def factorial_numero(m):
    factorial=1
    #VERIFICAMOS QUE EL NUMERO SEA DIFERENTE DE CERO , CASO CONTRARIO NO TENDRIA SENTIDO EL FACTORIAL
    while m>0:
        factorial=factorial*m+m
        m -=1
    return factorial

################################################################################

#EJERCICIO NUMERO 24
#EN ESTE EJERCICO CALCULAREMOS EL AREA DE UN ROMBO
#EL AREA DE UN TRAPECIO SE HALLA CON LOS DATOS DE DIAGONAL MAYO, DIAGONAL MENOR
def area_rombo(diagonal_mayor, diagonal_menor):
    #ESTABLECEMOS LA FORMULA PARA HALLA EL AREA
    resultado=(diagonal_mayor*diagonal_menor)/2
    return resultado

################################################################################

#EJERCICIO NUMERO 25
#EN ESTE EJERCICO CALCULAREMOS EL VOLUMEN DE UNA PIRAMIDE
#EL AREA DE UN TRAPECIO SE HALLA CON LOS DATOS DE ALTURA, AREA DELA BASE
def hallar_volumn_piramide(area_base, altura):
    #ESTABLECEMOS LA FORMULA PARA HALLA EL AREA
    resultado=(area_base*altura)
    return resultado

################################################################################
