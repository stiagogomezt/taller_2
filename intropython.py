#comentario de una linea todo lo que va despues de la linea es ignorado por el interprte de python
#variables: espacio de memoria, con nombre , donde guardo vvalores 
#los nombres de variables deben ser cortos, descriptivos, no tener espacios en blanco ni caracteres especiales, no deben empezar por un numero.

#descriptivo significa que representa la catgoria del dato que quiero guardar
#las variables pueden tener cualquier dato de tipo primitivo 
#numeros (entero, real), cadenas de caracteres (string), boleanos (true, false)
#caracteres (letras).

variable=1
variable = 'juventud divino tesoro, te vas para no volver'
variable= True
variable='a'
variable =3.1415926535
#para asignar valor a la variable se usa el operador =

#operadores:mecanismo para obtener un dato apartir de otros datos.
#los datos que intervienen se llaman operandos.
#aritmeticos: +,-,/,*,%
#de comparacion: retornan true o false.<> >= <= == !=
#de logica booleana :OR AND. Retornan True o False de acuerdo a una tabla de verdad, los operadores siempre son booleanos (true o false)

a=True
b=False
print(a and b)
#los operadores booleanos y de comparacion son muy utilizados al definir condiciones 
#estructuras de control de flujo:
#en general un programa se ejecuta linea por linea de manera secuencial,se puede romper esa secuencialidad empleando conjuntos de expresiones que permiten 
#1 seleccionar  la ejecucion de bloque de cdigo
# 2 repetir la ejecucion d eun bloque de codigo 
# 3 seleccionar entre ejecutar un bloque de codigo u otro bloque de codigo
# de esta manera podemos romper la secuencialidad
#principios del paradigma de programacion estructurado

#Sentencia if. Si se cumple una condicion se ejecuta un bloque de codigo (se evalua como true)
print ("linea1")

print ("linea2")

if 5>3 or 3<7 :
    print ("esto se muestra si la condicion es verdadera")
else:
    print ("esto se muestra si la condicion es false")
    
entrada = int(input("cuantos años tiene?"))
if entrada < 18:
    print ("es un menor de edad")
else:
    print("es mayor")
    
    #taller crear un programa en python que genere un numero aleatorio entre 2 y 12. si el numero es 7 imprimir gano si no imprimir deje el juego