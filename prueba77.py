from operaciones import Operacion
from Token import Token
from analizadorPrueba import*
import graphviz 
import math

def comenzar():
    autom = Automata()
    cadena = open('archivo.txt', 'r').read()

    resultado = autom.analizar(cadena , Operacion('sexo'))
    autom.imprimir_tokens()
    autom.imprimir_errores()
    lista_operaciones=[]
    grafo = graphviz.Digraph('ejemplo', filename="grafo");
    grafo.attr(rankdir="TB")

    if autom.estado_actual in autom.estados_aceptacion:
        for oper in resultado[1]:
            try:
                resultado = oper.operar(lista_operaciones,grafo)
                print(resultado[0], "=", resultado[1])
                lista_operaciones=resultado[2]
                grafo=resultado[3]
            except Exception as e:
                print("Hubo un error")
    print(lista_operaciones)
    grafo.view()
    '''lista_operacion_igualar=lista_operaciones
    lista_operacion_resultados=lista_operaciones

    grafo = graphviz.Digraph('ejemplo', filename="grafo");
    grafo.attr(rankdir="TB")
    indice=0
    for numero in lista_operaciones:
        grafo.node(str(indice), f'{numero}', shape="doublecircle")
        indice+=1

    indice1=0
    for num in lista_operaciones:
        indice2=0
        for num2 in lista_operacion_igualar:
            if num!=num2:

                if (float(num)+float(num2)) in lista_operacion_resultados:
                    indice3=0
                    for num3 in lista_operacion_resultados:
                        if (float(num)+float(num2)==float(num3)):
                            if f'{indice3} -> {indice1}' not in grafo.body and f'{indice3} -> {indice2}' not in grafo.body:
                                grafo.edge(str(indice3),str(indice1))
                                grafo.edge(str(indice3),str(indice2))
                        indice3+=1
                if (float(num)-float(num2)) in lista_operacion_resultados:
                    indice3=0
                    for num3 in lista_operacion_resultados:
                        if (float(num)-float(num2)==float(num3)):
                            if f'{indice3} -> {indice1}' not in grafo.body and f'{indice3} -> {indice2}' not in grafo.body:
                                grafo.edge(str(indice3),str(indice1))
                                grafo.edge(str(indice3),str(indice2))
                        indice3+=1
                if (float(num)*float(num2)) in lista_operacion_resultados:
                    indice3=0
                    for num3 in lista_operacion_resultados:
                        if (float(num)*float(num2)==float(num3)):
                            if f'{indice3} -> {indice1}' not in grafo.body and f'{indice3} -> {indice2}' not in grafo.body:
                                grafo.edge(str(indice3),str(indice1))
                                grafo.edge(str(indice3),str(indice2))
                        indice3+=1
                if (float(num)/float(num2)) in lista_operacion_resultados:
                    indice3=0
                    for num3 in lista_operacion_resultados:
                        if (float(num)/float(num2)==float(num3)):
                            if f'{indice3} -> {indice1}' not in grafo.body and f'{indice3} -> {indice2}' not in grafo.body:
                                grafo.edge(str(indice3),str(indice1))
                                grafo.edge(str(indice3),str(indice2))
                        indice3+=1
                if (float(num)**float(num2)) in lista_operacion_resultados:
                    indice3=0
                    for num3 in lista_operacion_resultados:
                        if (float(num)**float(num2)==float(num3)):
                            if f'{indice3} -> {indice1}' not in grafo.body and f'{indice3} -> {indice2}' not in grafo.body:
                                grafo.edge(str(indice3),str(indice1))
                                grafo.edge(str(indice3),str(indice2))
                        indice3+=1
                if (float(num)%float(num2)) in lista_operacion_resultados:
                    indice3=0
                    for num3 in lista_operacion_resultados:
                        if (float(num)%float(num2)==float(num3)):
                            if f'{indice3} -> {indice1}' not in grafo.body and f'{indice3} -> {indice2}' not in grafo.body:
                                grafo.edge(str(indice3),str(indice1))
                                grafo.edge(str(indice3),str(indice2))
                        indice3+=1
            indice2+=1

        
        if (float(num)**float(0.5)) in lista_operacion_resultados:
            indice4=0
            for num4 in lista_operacion_resultados:
                if (float(num)**float(0.5)==float(num4)):
                    if f'{indice4} -> {indice1}' not in grafo.body:
                        grafo.edge(str(indice4),str(indice1))
                indice4+=1
        if (1/float(num)) in lista_operacion_resultados:
            indice4=0
            for num4 in lista_operacion_resultados:
                if (1/float(num)==float(num4)):
                    if f'{indice4} -> {indice1}' not in grafo.body:
                        grafo.edge(str(indice4),str(indice1))
                indice4+=1
        if (float(math.sin(math.radians(float(num))))) in lista_operacion_resultados:
            indice4=0
            for num4 in lista_operacion_resultados:
                if (float(math.sin(math.radians(float(num))))==float(num4)):
                    if f'{indice4} -> {indice1}' not in grafo.body:
                        grafo.edge(str(indice4),str(indice1))
                indice4+=1
        if (float(math.cos(math.radians(float(num))))) in lista_operacion_resultados:
            indice4=0
            for num4 in lista_operacion_resultados:
                if (float(math.cos(math.radians(float(num))))==float(num4)):
                    if f'{indice4} -> {indice1}' not in grafo.body:
                        grafo.edge(str(indice4),str(indice1))
                indice4+=1
        if (float(math.tan(math.radians(float(num))))) in lista_operacion_resultados:
            indice4=0
            for num4 in lista_operacion_resultados:
                if (float(math.tan(math.radians(float(num))))==float(num4)):
                    if f'{indice4} -> {indice1}' not in grafo.body:
                        grafo.edge(str(indice4),str(indice1))
                indice4+=1
        indice1+=1
        
    grafo.view()'''


comenzar()