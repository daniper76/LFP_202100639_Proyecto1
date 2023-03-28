from operaciones import Operacion
from Token import Token
from analizadorPrueba import*

def comenzar():
    autom = Automata()
    cadena = open('archivo.txt', 'r').read()

    resultado = autom.analizar(cadena , Operacion('sexo'))
    autom.imprimir_tokens()
    autom.imprimir_errores()
    if autom.estado_actual in autom.estados_aceptacion:
        for oper in resultado[1]:
            try:
                resultado = oper.operar()
                print(resultado[0], "=", resultado[1])
            except Exception as e:
                print("Hubo un error LPTM!!! :/ :(")

comenzar()