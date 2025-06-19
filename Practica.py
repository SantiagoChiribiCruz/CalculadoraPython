PRIMER_VALOR = "Ingrese el primer valor a "
SEGUNDO_VALOR = "Ingrese el segundo valor a "
MENU_PRINCIPAL = """//BIENVENIDO A CALCULADORA SANTI - NO FUNCIONA CON HINCHAS DE MILLOS//
¿Que operacion desea hacer?
1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Salir del Menu
Ingrese un numero de (1 a 5):
"""

print(MENU_PRINCIPAL)

opcion = int(input())

match opcion:
    case 1:
     numero1= int(input(PRIMER_VALOR+"Sumar:"))
     numero2= int(input(SEGUNDO_VALOR+"Sumar:"))
     print ("Este es el resultado de la Suma:", numero1+numero2)

    case 2:
     numero1= int(input(PRIMER_VALOR+"Restar:"))
     numero2= int(input(SEGUNDO_VALOR+"Restar:"))
     print ("Este es el resultado de la Resta:", numero1-numero2)
    
    case 3:
     numero1= int(input(PRIMER_VALOR+"Multiplicar:"))
     numero2= int(input(SEGUNDO_VALOR+"Multiplicar:"))
     print ("Este es el resultado de la Multiplicacion:", numero1*numero2)

    case 4: 
     numero1= int(input(PRIMER_VALOR+"Division:"))
     numero2= int(input(SEGUNDO_VALOR+"Division:"))
     print ("Este es el resultado de la Division:", numero1//numero2)    
    case _:
     print("\nUsted ha salido") 
