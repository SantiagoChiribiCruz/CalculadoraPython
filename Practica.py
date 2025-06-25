import constantes

print(constantes.MENU_PRINCIPAL)

opcion = int(input())
if opcion != int:
 print ("Opcion no valida")
 
     


match opcion:
    case 1:
     numero1= int(input(constantes.PRIMER_VALOR+"Sumar:"))
     numero2= int(input(constantes.SEGUNDO_VALOR+"Sumar:"))
     print ("Este es el resultado de la Suma:", numero1+numero2)

    case 2:
     numero1= int(input(constantes.PRIMER_VALOR+"Restar:"))
     numero2= int(input(constantes.SEGUNDO_VALOR+"Restar:"))
     print ("Este es el resultado de la Resta:", numero1-numero2)
    
    case 3:
     numero1= int(input(constantes.PRIMER_VALOR+"Multiplicar:"))
     numero2= int(input(constantes.SEGUNDO_VALOR+"Multiplicar:"))
     print ("Este es el resultado de la Multiplicacion:", numero1*numero2)

    case 4: 
     numero1= int(input(constantes.PRIMER_VALOR+"Division:"))
     numero2= int(input(constantes.SEGUNDO_VALOR+"Division:"))
     print ("Este es el resultado de la Division:", numero1//numero2)    
    case _:
     print("\nUsted ha salido") 
