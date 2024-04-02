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
     
def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    try:
        numero_usuario = int(input("Ingrese un número: "))
        print("Números impares entre -{} y {}:".format(numero_usuario, numero_usuario))
        for num_imp in range(-numero_usuario, numero_usuario + 1):
            if num_imp % 2 != 0:
                print(num_imp, end=" ")
        print("\nNúmeros primos entre 0 y 100:")
        for num_primo in range(101):
            if es_primo(num_primo):
                print(num_primo, end=" ")
    except ValueError:
        print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
