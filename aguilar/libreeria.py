#para el primero ejercicio
def promedio(a,b,c):
    res=(a+b+c)/3
    return res

#para el segundo ejercicio
def area_del_trapecio(a,b,c):
    resul=((a+b)*c)/2
    return resul

#para el tercer ejercicio
def pedir_dni(dni):
    #verificamos su extension
    if(len(str(dni))!=8):
        men="el dni es falso"
        return men
    #fin_if
    else:
        return dni

#para el cuarto ejercicio
def pedir_ruc(ruc):
    #verificamos su extension
    if(len(str(ruc))!=11):
        msg="el numero de ruc es falso"
        return msg
    #fin_if
    else:
        return ruc

#para el quinto ejercicio
def pedir_edad(edad):
    #verificamos la edad correcta
    if(edad<0 or edad>120):
        msg="incorrecta"
        return msg
    #fin_if
    else:
        return edad

#para el sexto ejercicio
def pedir_bolillas(bol1,bol2):
    #verificamos las bolillas y comprovamos que sean siferentes
    #revisamos tambien si es un numero menor a 0 y mayor, mostraremos falsos los numeros
    if(bol1<0 or bol1>100):
        msg1="la primera bolilla es falsa"
        return msg1
    #fin_if
    if(bol2<0 or bol2>100 or bol2==bol1):
        msg2="la segunda bolilla es falsa"
        return msg2
    #fin_if
    else:
        return bol1,bol2
#para el septimo ejercicio
def pedir_numero_de_cel(cel):
    #verificamos su extension
    #el numero tiene que ser peruano
    if(len(str(cel))!=9 or int(str(cel)[0])!=9):
        msg="falso"
        return msg
    #fin_if
    else:
        return cel

#para el octavo ejercicio
def pedir_placa(placa):
    #varificamos su extension
    #la placa debe ser tipo ***-*** para que sea validad
    #los " * " pueden ser numeros o letras
    if(len(placa)!= 7 or placa[3]!="-"):
        msg="falsa"
        return msg
    #fin_if
    else:
        return placa

#para el noveno ejercicio
def pedir_nombre(nombre,apellido):
    #varificamos la extension del nombre
    #no debe de tener mas de 20 letras
    if(len(nombre)>20):
        msg="el nombre es falso"
        return msg
    #fin_if
    if(len(apellido)>20):
        msg="el apellido es falso"
        return msg
    #fin_if
    else:
        msg="son verdaderos"
        return msg

#para el decimo ejercicio
#en este caso pediremos una palabra palindroma
def pedir_palabra_palindroma(pal):
    #verificamos si la palabra es palindroma
    if(pal[::-1]!=pal):
        msg=" no es palindroma"
        return msg
    #fin_if
    else:
        msg=" es palindroma"
        return msg

#para el decimo primero ejercicio
#en este caso pediremos la presion con valores correctos, o sea no menores que 0
def pedir_presion(fuerza,area):
    #verificamos si las variables son las correctas
    if(fuerza<0):
        msg="fuerza incorrecta"
        return msg
    #fin_if
    if(area<0):
        msg="el area es incorrecta"
        return msg
    #fin_if
    else:
        presion=fuerza/area
        return presion

#para el decimo segundo ejercicio
#en este caso pediremos un asiento de bus interprovincial
def pedir_asiento(asi):
    #verificamos si el asiento mayor a cero pero menor que 80
    if(asi<0 or asi>80):
        msg="invalido"
        return msg
    #fin_if
    else:
        return asi

#para el decimo tercero ejercicio
#en este caso pediremos el codigo del estudiante
def pedir_codigo(cod):
    #verificamos si el codigo tiene 7 digitos
    if(len(cod)!=7):
        msg="FALSO"
        return msg
    #fin_if
    else:
        return cod

#para el decimo cuarto ejercicio
#en este caso pediremos el numero de tarjeta
def pedir_numero_de_tarejta(nume):
    #verificamos si el numero de la tarjeta tiene 16 digitos
    if(len(str(nume))!=16):
        msg="FALSO"
        return msg
    #fin_if
    else:
        return nume

#para el decimo quinto ejercicio
#en este caso pediremos la distancia
def pedir_distancia(velocidad,tiempo):
    #verificamos si la velocidad y el tiempo son las correctas, o sea mayores que 0
    if(velocidad<0):
        msg="velocidad incorrecta"
        return msg
    #fin_if
    if(tiempo<0):
        msg="tiempo incorrecto"
        return msg
    #fin_if
    else:
        distnacia=velocidad*tiempo
        return distnacia

#para el decimo sexto ejercicio
#en este caso pediremos la fecha de nacimiento
def pedir_fecha(fecha):
    #verificamos si la fecha es la correcta
    if(len(fecha)!=10 or fecha[2]!="/" or fecha[5]!="/" or int(fecha[6:])<1900 or int(fecha[6:])>2020):
        msg="FALSO"
        return msg
    #fin_if
    else:
        return fecha

#para el decimo septimo ejercicio
#en este caso pediremos la clave de una tarjeta VISA
def pedir_clave(clave):
    #verificamos si la canidad de cifras de la clave sea la correcta, o sea que sen 4 cicras
    if(len(str(clave))!=4):
        msg="FALSA"
        return msg
    #fin_if
    else:
        return clave

#para el decimo octavo ejercicio
#en este caso pediremos el puesto de un estudiante
def pedir_puesto(puesto):
    #verificamos si es puesto es el correcto para entrar al concurso
    if(puesto<0 or puesto>10):
        msg="NO"
        return msg
    #fin_if
    else:
        msg="SI"
        return msg

#para el decimo noveno ejercicio
#en este caso pediremos la temperatura del paciente
def pedir_temperatura(temperatura):
    #verificamos si la temperatura es la correcta
    if(temperatura>35 and temperatura<42):
        msg="correcta"
        return msg
    else:
        msg="incorrecta"
        return msg
    #fin_if
    #no me salio :(
    #quise que aparaciera si estaba enfermo o no pero no salio, lo anide y no se pudo, luego hice una condicion multiple y nada

#para el vigesimo ejercicio
#en este caso pediremos la hora
def pedir_hora(hora):
    #verificamos si la hora es la correcta
    if(len(hora)!=5 or hora[2]!=":" or int(hora[0:2])>23 or int(hora[3:])>59):
        msg="ES INCORRECTA"
        return msg
    #fin_if
    else:
        return hora

#para el vigesimo primero ejercicio
#en este caso pediremos el dia de la semana
def pedir_dia_semana(dia):
    #verificamos si el dia es correcto
    if(dia!="lunes" and dia!="martes" and dia!="miercoles" and dia!="jueves" and dia!="viernes" and dia!="sabado" and dia!="domingo"):
        msg="INCORRECTO"
        return msg
    #fin_if
    else:
        return dia

#para el vigesimo segundo ejercicio
#en este caso pediremos un calculo sobre el trabajo
def pedir_trabajo(fuerza,distancia):
    #verificamos si la fuerza es la correcta
    if(fuerza<0):
        msg="la fuerza es invalida"
        return msg
    #verificamos si la distancia es valida
    if(distancia<0):
        msg="la distancia es invalida"
        return msg
    #fin_if
    else:
        trabajo=fuerza*distancia
        return trabajo

#para el vigesimo tercero ejercicio
#en este caso pediremos la aceleracion
def pedir_aceleracion(variaciacion_de_velocidad,tiempo):
    #verificamos si la veracion de velocidades es la correcta
    if(variaciacion_de_velocidad<0):
        msg="la variacion es incorrecta"
        return msg
    #fin_if
    #verificamos si el tiempo es el correcto
    if(tiempo<0):
        msg="el tiempo es incorrecto"
        return msg
    #fin_if
    else:
        aceleracion=variaciacion_de_velocidad/tiempo
        return aceleracion

#para el vigesimo cuarto ejercicio
#en este caso pediremos el correo de gmail
def pedir_correo(correo):
    #verificamos si el correo es correcto
    cor=correo[::-1]
    if(cor[0:9]!="moc.liamg"):
        msg="el correo es invalido"
        return msg
    #fin_if
    else:
        return correo

#para el vigesimo quinto ejercicio
#en este caso pediremos el numero telefonico peruano (chiclayo)
def pedir_telfono(tel):
    if(len(str(tel))!=9 or str(tel[0:3])!="074"):
        msg="FALSO"
        return msg
    #fin_if
    else:
        return tel
