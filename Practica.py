import constantes
import os
opciones_validos = ["1","2","3","4","5"]

print(constantes.MENU_PRINCIPAL)
opcion = input()

while opcion not in opciones_validos:
    print(f"'{opcion}' no es una opcion valida")
    input("Ingrese una opcion valida, Presione ENTER para continuar")
    os.system('cls')
    print(constantes.MENU_PRINCIPAL)
    opcion = input()
    
match opcion:
    case "1":
     numero1= int(input(constantes.PRIMER_VALOR+"Sumar:"))
     numero2= int(input(constantes.SEGUNDO_VALOR+"Sumar:"))
     print ("Este es el resultado de la Suma:", numero1+numero2)

    case "2":
     numero1= int(input(constantes.PRIMER_VALOR+"Restar:"))
     numero2= int(input(constantes.SEGUNDO_VALOR+"Restar:"))
     print ("Este es el resultado de la Resta:", numero1-numero2)
    
    case "3":
     numero1= int(input(constantes.PRIMER_VALOR+"Multiplicar:"))
     numero2= int(input(constantes.SEGUNDO_VALOR+"Multiplicar:"))
     print ("Este es el resultado de la Multiplicacion:", numero1*numero2)

    case "4": 
     numero1= int(input(constantes.PRIMER_VALOR+"Division:"))
     numero3= int(input(constantes.SEGUNDO_VALOR+"Division:"))
     while numero3 == 0: 
           print("No se puede dividir en 0\n")
           input("Ingrese un numero valido, Presione ENTER para continuar")
           os.system('cls')
           numero3= int(input(constantes.SEGUNDO_VALOR+"Division:"))
     print ("Este es el resultado de la Division:", numero1//numero3)    
    case "5":
     print("\nUsted ha salido") 
