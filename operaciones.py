import math
class Operacion:
    def __init__(self, tipo):
        self.tipo = tipo
        self.operandos = []

    def operar(self,lista_operaciones,grafo):
        res = '' # 1 + (1 + 1) = 3
        resnum = 0
        tipo=self.tipo
        if self.tipo.lower() == 'suma':
            
            lista_suma=[]
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' + '
                    grafo.node(str(operando), f'{operando}', shape="doublecircle")
                    lista_operaciones.append(float(operando))
                    lista_suma.append(operando)
                    if len(lista_suma)==2:
                        resnum=float(lista_suma[0])+float(lista_suma[1])
                        grafo.node(str(resnum), f'{self.tipo}\n'+f'{resnum}', shape="doublecircle")
                        grafo.edge(str(resnum),str(lista_suma[0]))
                        grafo.edge(str(resnum),str(lista_suma[1]))
                        
                else:
                    operado = operando.operar(lista_operaciones,grafo)
                    res += '(' + operado[0] + ') + '
                    grafo.node(str(operado[1]), f'{operado[1]}', shape="doublecircle")
                    lista_operaciones=operado[2]
                    grafo=operado[3]
                    lista_suma.append(operado[1])
                    if len(lista_suma)==2:
                        resnum=float(lista_suma[0])+float(lista_suma[1])
                        grafo.node(str(resnum), f'{self.tipo}\n'+f'{resnum}', shape="doublecircle")
                        grafo.edge(str(resnum),str(lista_suma[0]))
                        grafo.edge(str(resnum),str(lista_suma[1]))
                    

        if self.tipo.lower() == 'resta':
            lista_resta=[]
        
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' - '
                    grafo.node(str(operando), f'{operando}', shape="doublecircle")
                    lista_resta.append(operando)
                    lista_operaciones.append(float(operando))
                    if len(lista_resta)==2:
                        resnum=float(lista_resta[0])-float(lista_resta[1])
                        grafo.node(str(resnum),f'{tipo}\n'+f'{resnum}', shape="doublecircle")
                        grafo.edge(str(resnum),str(lista_resta[0]))
                        grafo.edge(str(resnum),str(lista_resta[1]))
                else:
                    operado = operando.operar(lista_operaciones,grafo)
                    res += '(' + operado[0] + ') - '
                    grafo.node(str(operado[1]), f'{operado[1]}', shape="doublecircle")
                    lista_operaciones=operado[2]
                    grafo=operado[3]
                    lista_resta.append(operado[1])
                    if len(lista_resta)==2:
                        resnum=float(lista_resta[0])-float(lista_resta[1])
                        grafo.node(str(resnum), f'{tipo}\n'+f'{resnum}', shape="doublecircle")
                        grafo.edge(str(resnum),str(lista_resta[0]))
                        grafo.edge(str(resnum),str(lista_resta[1]))


        elif self.tipo.lower() == 'multiplicacion':
            resnum = 1
            lista_multiplicacion=[]
            
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' * '
                    grafo.node(str(operando), f'{operando}', shape="doublecircle")
                    lista_operaciones.append(float(operando))
                    lista_multiplicacion.append(operando)
                    if len(lista_multiplicacion)==2:
                        resnum = float(lista_multiplicacion[0])*float(lista_multiplicacion[1])
                        grafo.node(str(resnum), f'{tipo}\n'+f'{resnum}', shape="doublecircle")
                        grafo.edge(str(resnum),str(lista_multiplicacion[0]))
                        grafo.edge(str(resnum),str(lista_multiplicacion[1]))
                else:
                    operado=operando.operar(lista_operaciones,grafo)
                    res += '(' + operado[0] + ') * '
                    grafo.node(str(operado[1]), f'{operado[1]}', shape="doublecircle")
                    lista_operaciones=operado[2]
                    grafo=operado[3]
                    lista_multiplicacion.append(operado[1])
                    if len(lista_multiplicacion)==2:
                        resnum = float(lista_multiplicacion[0])*float(lista_multiplicacion[1])
                        grafo.node(str(resnum), f'{tipo}\n'+f'{resnum}', shape="doublecircle")
                        grafo.edge(str(resnum),str(lista_multiplicacion[0]))
                        grafo.edge(str(resnum),str(lista_multiplicacion[1]))

        elif self.tipo.lower() == 'division':
            resnum = 1
            lista_division=[]
            
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' / '
                    grafo.node(str(operando), f'{operando}', shape="doublecircle")
                    lista_operaciones.append(float(operando))
                    lista_division.append(operando)
                    if len(lista_division)==2:
                        resnum=float(lista_division[0])/float(lista_division[1])
                        grafo.node(str(resnum), f'{tipo}\n'+f'{resnum}', shape="doublecircle")
                        grafo.edge(str(resnum),str(lista_division[0]))
                        grafo.edge(str(resnum),str(lista_division[1]))
                else:
                    operado=operando.operar(lista_operaciones,grafo)
                    res += '(' + operado[0] + ') / '
                    grafo.node(str(operado[1]), f'{operado[1]}', shape="doublecircle")
                    lista_operaciones=operado[2]
                    grafo=operado[3]
                    lista_division.append(float(operado[1]))
                    if len(lista_division)==2:
                        resnum=float(lista_division[0])/float(lista_division[1])
                        grafo.node(str(resnum), f'{tipo}\n'+f'{resnum}', shape="doublecircle")
                        grafo.edge(str(resnum),str(lista_division[0]))
                        grafo.edge(str(resnum),str(lista_division[1]))

        elif self.tipo.lower() == 'potencia':
            resnum = 1
            lista_potencia=[]
            
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' ^ '
                    grafo.node(str(operando), f'{operando}', shape="doublecircle")
                    lista_operaciones.append(float(operando))
                    lista_potencia.append(operando)
                    if len(lista_potencia)==2:
                        resnum=float(lista_potencia[0])**float(lista_potencia[1])
                        grafo.node(str(resnum), f'{tipo}\n'+f'{resnum}', shape="doublecircle")
                        grafo.edge(str(resnum),str(lista_potencia[0]))
                        grafo.edge(str(resnum),str(lista_potencia[1]))
                else:
                    operado=operando.operar(lista_operaciones,grafo)
                    res += '(' + operado[0] + ') ^ '
                    grafo.node(str(operado[1]), f'{operado[1]}', shape="doublecircle")
                    lista_operaciones=operado[2]
                    grafo=operado[3]
                    lista_potencia.append(float(operado[1]))
                    if len(lista_potencia)==2:
                        resnum=float(lista_potencia[0])**float(lista_potencia[1])
                        grafo.node(str(resnum), f'{tipo}\n'+f'{resnum}', shape="doublecircle")
                        grafo.edge(str(resnum),str(lista_potencia[0]))
                        grafo.edge(str(resnum),str(lista_potencia[1]))

        elif self.tipo.lower() == 'raiz':
            resnum = 1
            lista_raiz=[]
            
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' ^0.5 '
                    grafo.node(str(operando), f'{operando}', shape="doublecircle")
                    lista_operaciones.append(float(operando))
                    lista_raiz.append(operando)
                    if len(lista_raiz)==1:
                        resnum=float(lista_raiz[0])**float(0.5)
                        grafo.node(str(resnum), f'{tipo}\n'+f'{resnum}', shape="doublecircle")
                        grafo.edge(str(resnum),str(lista_raiz[0]))
                else:
                    operado=operando.operar(lista_operaciones,grafo)
                    res += '(' + operado[0] + ') ^ (1/2) '
                    grafo.node(str(operado[1]), f'{operado[1]}', shape="doublecircle")
                    lista_operaciones=operado[2]
                    grafo=operado[3]
                    lista_raiz.append(operado[1])
                    if len(lista_raiz)==1:
                        resnum=float(lista_raiz[0])**float(0.5)
                        grafo.node(str(resnum), f'{tipo}\n'+f'{resnum}', shape="doublecircle")
                        grafo.edge(str(resnum),str(lista_raiz[0]))

        elif self.tipo.lower() == 'inverso':
            resnum = 1
            
            lista_inverso=[]
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += 'Inv('+operando+')'
                    grafo.node(str(operando), f'{operando}', shape="doublecircle")
                    lista_operaciones.append(float(operando))
                    lista_inverso.append(operando)
                    if len(lista_inverso)==1:
                        resnum=float(1/lista_inverso[0])
                        grafo.node(str(resnum), f'{tipo}\n'+f'{resnum}', shape="doublecircle")
                        grafo.edge(str(resnum),str(lista_inverso[0]))
                else:
                    operado=operando.operar(lista_operaciones,grafo)
                    res += 'Inverso(' + operado[0] + ') '
                    grafo.node(str(operado[1]), f'{operado[1]}', shape="doublecircle")
                    lista_operaciones=operado[2]
                    grafo=operado[3]
                    lista_inverso.append(operado[1])
                    if len(lista_inverso)==1:
                        resnum=float(1/lista_inverso[0])
                        grafo.node(str(resnum), f'{tipo}\n'+f'{resnum}', shape="doublecircle")
                        grafo.edge(str(resnum),str(lista_inverso[0]))

        elif self.tipo.lower() == 'seno':
            resnum = 1
            lista_seno=[]
            
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += 'Sen('+operando+')'
                    grafo.node(str(operando), f'{operando}', shape="doublecircle")
                    lista_operaciones.append(float(operando))
                    lista_seno.append(operando)
                    if len(lista_seno)==1:
                        resnum=float(math.sin(math.radians(float(lista_seno[0]))))
                        grafo.node(str(resnum), f'{tipo}\n'+f'{resnum}', shape="doublecircle")
                        grafo.edge(str(resnum),str(lista_seno[0]))
                else:
                    operado=operando.operar(lista_operaciones,grafo)
                    res += 'Sen(' + operado[0] + ') '
                    grafo.node(str(operado[1]), f'{operado[1]}', shape="doublecircle")
                    lista_operaciones=operado[2]
                    grafo=operado[3]
                    lista_seno.append(operado[1])
                    if len(lista_seno)==1:
                        resnum=float(math.sin(math.radians(float(lista_seno[0]))))
                        grafo.node(str(resnum), f'{tipo}\n'+f'{resnum}', shape="doublecircle")
                        grafo.edge(str(resnum),str(lista_seno[0]))

        elif self.tipo.lower() == 'coseno':
            resnum = 1
            lista_coseno=[]
            
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += 'Cos('+operando+')'
                    grafo.node(str(operando), f'{operando}', shape="doublecircle")
                    lista_operaciones.append(float(operando))
                    lista_coseno.append(operando)
                    if len(lista_coseno)==1:
                        resnum=float(math.cos(math.radians(float(lista_coseno[0]))))
                        grafo.node(str(resnum), f'{tipo}\n'+f'{resnum}', shape="doublecircle")
                        grafo.edge(str(resnum),str(lista_coseno[0]))
                else:
                    operado=operando.operar(lista_operaciones,grafo)
                    res += 'Cos(' + operado[0] + ') '
                    grafo.node(str(operado[1]), f'{operado[1]}', shape="doublecircle")
                    lista_operaciones=operado[2]
                    grafo=operado[3]
                    lista_coseno.append(operado[1])
                    if len(lista_coseno)==1:
                        resnum=float(math.cos(math.radians(float(lista_coseno[0]))))
                        grafo.node(str(resnum), f'{tipo}\n'+f'{resnum}', shape="doublecircle")
                        grafo.edge(str(resnum),str(lista_coseno[0]))

        elif self.tipo.lower() == 'tangente':
            resnum = 1
            lista_tangente=[]
            
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += 'Tan('+operando+')'
                    grafo.node(str(operando), f'{operando}', shape="doublecircle")
                    lista_operaciones.append(float(operando))
                    lista_tangente.append(operando)
                    if len(lista_tangente)==1:
                        resnum=float(math.tan(math.radians(float(lista_tangente[0]))))
                        grafo.node(str(resnum), f'{tipo}\n'+f'{resnum}', shape="doublecircle")
                        grafo.edge(str(resnum),str(lista_tangente[0]))
                else:
                    operado=operando.operar(lista_operaciones,grafo)
                    res += 'Tan(' + operado[0] +')'
                    grafo.node(str(operado[1]), f'{operado[1]}', shape="doublecircle")
                    lista_operaciones=operado[2]
                    grafo=operado[3]
                    lista_tangente.append(operado[1])
                    if len(lista_tangente)==1:
                        resnum=float(math.tan(math.radians(float(lista_tangente[0]))))
                        grafo.node(str(resnum), f'{tipo}\n'+f'{resnum}', shape="doublecircle")
                        grafo.edge(str(resnum),str(lista_tangente[0]))

        elif self.tipo.lower() == 'mod':
            resnum = 1
            lista_mod=[]
            
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' mod '
                    grafo.node(str(operando), f'{operando}', shape="doublecircle")
                    lista_operaciones.append(float(operando))
                    lista_mod.append(operando)
                    if len(lista_mod)==2:
                        resnum=float(lista_mod[0])%float(lista_mod[1])
                        grafo.node(str(resnum), f'{tipo}\n'+f'{resnum}', shape="doublecircle")
                        grafo.edge(str(resnum),str(lista_mod[0]))
                        grafo.edge(str(resnum),str(lista_mod[1]))
                else:
                    operado=operando.operar(lista_operaciones,grafo)
                    res += '(' + operado[0] + ') / '
                    grafo.node(str(operado[1]), f'{operado[1]}', shape="doublecircle")
                    lista_operaciones=operado[2]
                    grafo=operado[3]
                    lista_mod.append(float(operado[1]))
                    if len(lista_mod)==2:
                        resnum=float(lista_mod[0])%float(lista_mod[1])
                        grafo.node(str(resnum), f'{tipo}\n'+f'{resnum}', shape="doublecircle")
                        grafo.edge(str(resnum),str(lista_mod[0]))
                        grafo.edge(str(resnum),str(lista_mod[1]))

        lista_operaciones.append(resnum)
        return [res[0:-3], resnum,lista_operaciones,grafo]