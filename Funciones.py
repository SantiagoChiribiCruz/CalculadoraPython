import constantes
import os

def operar (a, opcion, b):
    if opcion == 1:
         Resultado = a+b
    elif opcion == 2:
         Resultado = a-b
    elif opcion == 3:
         Resultado = a*b
    elif opcion == 4:
         Resultado = a/b 
    return Resultado

def ingresar_numero (posicion, operacion):
    if posicion == 1:
        str_solicita_valor = constantes.PRIMER_VALOR
    elif posicion == 2:
        str_solicita_valor = constantes.SEGUNDO_VALOR

    match operacion:
        case "+":
            str_solicita_valor = str_solicita_valor + "Sumar:"
        case "-":
            str_solicita_valor = str_solicita_valor + "Restar:"
        case "*":
            str_solicita_valor = str_solicita_valor + "Multiplicar:"
        case "/":
            str_solicita_valor = str_solicita_valor + "Dividir:"

    while True :
        numero1 = input(str_solicita_valor)
        try:
            numero1 = float(numero1)
            if operacion == "/" and posicion == 2 and numero1 == 0:
             print("No se puede dividir entre 0.\n")
             input("Ingrese un número distinto de cero. Presione ENTER para continuar")
             os.system('cls')
             continue 
            return numero1    
        except ValueError:
            print(f"'{numero1}' no es un 'NUMERO' valido ")
            input("Debe ingresar un 'NUMERO' , Presione ENTER para continuar")
            os.system('cls')

def pedir_opcion_valida (opciones_validos, menu):
    print(menu)
    opcion = input()

    while opcion not in opciones_validos:
        print(f"'{opcion}' no es una opcion valida")
        input("Ingrese una opcion valida, Presione ENTER para continuar")
        os.system('cls')
        print(constantes.MENU_PRINCIPAL)
        opcion = input() 
    return opcion
            