#wghile #while <condicion<verdadera>:
#cuerpo del ciclo 
#condiciones son : expresiones booleanas (or,and) y operadores de comparador 
#ciclos controlados por un controlador entero
#i=0
#while i<10:
# print("ciclo")
      #importante modificar el valor del controlador 
#i+=1
#ciclos controlados 

#import random
#a=0
#while a!=5:
 #   a=random.randint(1,10)
 #   print (a)
#print("se acabo")
#ciclos controlados por un evento 

#a=0
#while 1==1:
    
 #   a= int(input("ingrese un numero "))
  #  if a == 10:
   #     break
    
#for: se utiliza para recorrer "iterable", se repita tanats veces como elemntos tenga el iterable, en cada ciclo se guarda
#lista,tupla,diccionario....
#lista: conjunto de variables organizadas en espacios consecutivos  de memoria, a las que se le asigna un unico nombre , la unnica manera de diferenciarlas es la posicion
#que ocupan respecto al primer elemento de la lista 

#miLista=[ 1, True, "textos", 3.89 ]
#miLista2=[]
#print(miLista)
#print(miLista2)
#en python todos son objetos
#print(miLista)
#miLista.sort()
#print(miLista)
#funcion Len longitud de la lista 
#print(len(miLista))
#tupla es una lista inmutable
#miTupla=(2,45,6,8,9,10)
#estructura for en python: 
#for<variable_donde_guardo_el_elemento in iterable:

#for x in miLista:
    #if x<50:
        #print("grande ")
#si solo utilizo el iterable para definir la cantidad de repeticiones entonces no es necesaria la variable 
#for _ in miLista:
    #print("ciclo")  
    #si no tengo un itrable puedo usa la funcion range para generar una secuencia de numeros 
    #for x in range (100):
     #print(x) 
     
     #taller crear un programa en consola que pida un numero al usuario y:
     #1. Imprima los numeros impares entre - numero y numero
     #2.Imprima los numeros primos entre 0 y numero 100
     
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def imprimir_impares_entre_negativo_y_positivo(numero):
    for i in range(-numero, numero + 1):
        if i % 2 != 0:
            print(i, end=" ")

def imprimir_primos_entre_0_y_multiplicado_por_100(numero):
    limite_superior = numero * 100
    for i in range(limite_superior + 1):
        if es_primo(i):
            print(i, end=" ")

def main():
    numero = int(input("Introduce un número: "))
    print("Números impares entre -{} y {}:".format(numero, numero))
    imprimir_impares_entre_negativo_y_positivo(numero)
    print("\nNúmeros primos entre 0 y {}:".format(numero * 100))
    imprimir_primos_entre_0_y_multiplicado_por_100(numero)

if __name__ == "__main__":
    main()
