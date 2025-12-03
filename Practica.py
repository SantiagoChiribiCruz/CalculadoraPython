import constantes
import os
import Funciones

opciones_validas = ["1","2","3","4","5"]
opcion = Funciones.pedir_opcion_valida(opciones_validas, constantes.MENU_PRINCIPAL)

match opcion:
    case "1":
        numero1 = Funciones.ingresar_numero(1,"+")
        numero2 = Funciones.ingresar_numero(2,"+")
        resultado = Funciones.operar(numero1, 1, numero2)
        print(f"El resultado de la suma de '{numero1}' Y '{numero2}' es =", resultado)

     

    case "2":
        numero1 = Funciones.ingresar_numero(1,"-")
        numero2 = Funciones.ingresar_numero(2,"-")
        resultado = Funciones.operar(numero1, 2, numero2)
        print(f"El resultado de la resta de '{numero1}' Y '{numero2}' es =", resultado)


    
    case "3":
        numero1 = Funciones.ingresar_numero(1,"*")
        numero2 = Funciones.ingresar_numero(2,"*")
        resultado = Funciones.operar(numero1, 3, numero2)
        print(f"El resultado de la multiplicacion de '{numero1}' Y '{numero2}' es =", resultado)

    case "4": 
     
        numero1 = Funciones.ingresar_numero(1,"/")
        numero2 = Funciones.ingresar_numero(2,"/")
        resultado = Funciones.operar(numero1, 4, numero2)
        print(f"El resultado de la division de '{numero1}' Y '{numero2}' es =", resultado)   
     
    case "5":
     print("\nUsted ha salido...") 

