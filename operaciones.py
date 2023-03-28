import math
class Operacion:
    def __init__(self, tipo):
        self.tipo = tipo
        self.operandos = []

    def operar(self):
        res = '' # 1 + (1 + 1) = 3
        resnum = 0
        if self.tipo.lower() == 'suma':
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' + '
                    resnum += float(operando)
                else:
                    operado = operando.operar()
                    res += '(' + operado[0] + ') + '
                    resnum += operado[1]

        if self.tipo.lower() == 'resta':
            lista_resta=[]
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' - '
                    lista_resta.append(operando)
                    if len(lista_resta)==2:
                        resnum=float(lista_resta[0])-float(lista_resta[1])
                else:
                    operado = operando.operar()
                    res += '(' + operado[0] + ') - '
                    lista_resta.append(operado[1])
                    if len(lista_resta)==2:
                        resnum=float(lista_resta[0])-float(lista_resta[1])


        elif self.tipo.lower() == 'multiplicacion':
            resnum = 1
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' * '
                    resnum = resnum * float(operando)
                else:
                    operado=operando.operar()
                    res += '(' + operado[0] + ') * '
                    resnum = resnum * float(operado[1])

        elif self.tipo.lower() == 'division':
            resnum = 1
            lista_division=[]
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' / '
                    lista_division.append(operando)
                    if len(lista_division)==2:
                        resnum=float(lista_division[0])/float(lista_division[1])
                else:
                    operado=operando.operar()
                    res += '(' + operado[0] + ') / '
                    lista_division.append(float(operado[1]))
                    if len(lista_division)==2:
                        resnum=float(lista_division[0])/float(lista_division[1])

        elif self.tipo.lower() == 'potencia':
            resnum = 1
            lista_potencia=[]
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' ^ '
                    lista_potencia.append(operando)
                    if len(lista_potencia)==2:
                        resnum=float(lista_potencia[0])**float(lista_potencia[1])
                else:
                    operado=operando.operar()
                    res += '(' + operado[0] + ') ^ '
                    lista_potencia.append(float(operado[1]))
                    if len(lista_potencia)==2:
                        resnum=float(lista_division[0])**float(lista_division[1])

        elif self.tipo.lower() == 'raiz':
            resnum = 1
            lista_raiz=[]
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' ^0.5 '
                    lista_raiz.append(operando)
                    if len(lista_raiz)==1:
                        resnum=float(lista_raiz[0])**float(0.5)
                else:
                    operado=operando.operar()
                    res += '(' + operado[0] + ') ^ (1/2) '
                    lista_raiz.append(operado[1])
                    if len(lista_raiz)==1:
                        resnum=float(lista_raiz[0])**float(0.5)

        elif self.tipo.lower() == 'inverso':
            resnum = 1
            lista_inverso=[]
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += 'Inv('+operando+')'
                    lista_inverso.append(operando)
                    if len(lista_inverso)==1:
                        resnum=float(1/lista_inverso[0])
                else:
                    operado=operando.operar()
                    res += 'Inverso(' + operado[0] + ') '
                    lista_inverso.append(operado[1])
                    if len(lista_inverso)==1:
                        resnum=float(1/lista_inverso[0])

        elif self.tipo.lower() == 'seno':
            resnum = 1
            lista_seno=[]
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += 'Sen('+operando+')'
                    lista_seno.append(operando)
                    if len(lista_seno)==1:
                        resnum=float(math.sin(math.radians(float(lista_seno[0]))))
                else:
                    operado=operando.operar()
                    res += 'Sen(' + operado[0] + ') '
                    lista_seno.append(operado[1])
                    if len(lista_seno)==1:
                        resnum=float(math.sin(math.radians(float(lista_seno[0]))))

        elif self.tipo.lower() == 'coseno':
            resnum = 1
            lista_coseno=[]
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += 'Cos('+operando+')'
                    lista_coseno.append(operando)
                    if len(lista_coseno)==1:
                        resnum=float(math.cos(math.radians(float(lista_coseno[0]))))
                else:
                    operado=operando.operar()
                    res += 'Cos(' + operado[0] + ') '
                    lista_coseno.append(operado[1])
                    if len(lista_coseno)==1:
                        resnum=float(math.cos(math.radians(float(lista_coseno[0]))))

        elif self.tipo.lower() == 'tangente':
            resnum = 1
            lista_tangente=[]
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += 'Tan('+operando+')'
                    lista_tangente.append(operando)
                    if len(lista_tangente)==1:
                        resnum=float(math.tan(math.radians(float(lista_tangente[0]))))
                else:
                    operado=operando.operar()
                    res += 'Tan(' + operado[0] +')'
                    lista_tangente.append(operado[1])
                    if len(lista_tangente)==1:
                        resnum=float(math.tan(math.radians(float(lista_tangente[0]))))

        elif self.tipo.lower() == 'mod':
            resnum = 1
            lista_mod=[]
            for operando in self.operandos:
                if type(operando) is not Operacion:
                    res += operando + ' mod '
                    lista_mod.append(operando)
                    if len(lista_mod)==2:
                        resnum=float(lista_mod[0])%float(lista_mod[1])
                else:
                    operado=operando.operar()
                    res += '(' + operado[0] + ') / '
                    lista_mod.append(float(operado[1]))
                    if len(lista_mod)==2:
                        resnum=float(lista_mod[0])%float(lista_mod[1])

        return [res[0:-3], resnum]