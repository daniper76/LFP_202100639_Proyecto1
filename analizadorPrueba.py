
from Token import Token
from Errores import Errores
from operaciones import Operacion

class Automata:
    letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s", "t", "u","v","w","x","y","z", "-","1","2"]
    numeros = ["1","2","3","4","5","6","7","8","9","0","."]
    tabla_tokens = []
    cadena = ''
    fila = 0
    columna = 0
    estado_actual = 0
    estado_anterior = 0
    estados_aceptacion = [9]
    tabla_errores=[]
    global operar
    global lista_division
    global lista_resta
    


    def analizar(self, cadena,operacion:Operacion):
        token = ''
        tipo_operacion=''
        operandos=[]
        error=False

        while len(cadena) > 0:
            char = cadena[0]

            if char == '\n':
                self.fila += 1
                self.columna = 0
                cadena = cadena[1:]
                continue
            elif char == '\t':
                self.columna += 4
                cadena = cadena[1:]
                continue
            elif char == ' ':
                self.columna += 1
                cadena = cadena[1:] 
                continue

            if self.estado_actual == 0:
                if char == '{':
                    self.estado_anterior = 0
                    self.estado_actual = 1
                    if error==False:
                        self.guardar_token(char)
                else:
                    error = True
                    self.guardar_errores(char)
                    self.estado_anterior = 0
                    self.estado_actual = 1

            elif self.estado_actual == 1:

                if char == '"':
                    self.estado_anterior = 1
                    self.estado_actual = 2
                    if error==False:
                        self.guardar_token(char)

                elif char == '{':
                    self.estado_anterior = 1
                    self.estado_actual = 10
                    if error==False:
                        self.guardar_token(char)
                else:
                    error = True
                    self.guardar_errores(char)

            elif self.estado_actual == 2:
                if char.lower() in self.letras:
                    self.estado_anterior = 2
                    self.estado_actual = 3
                    if error==False:
                        token += char
                else:
                    error = True
                    self.guardar_errores(char)
                    self.estado_anterior = 2
                    self.estado_actual = 3
            
            elif self.estado_actual == 3:
                if char.lower() in self.letras:
                    self.estado_anterior = 3
                    self.estado_actual = 3
                    if error==False:
                        token += char
                elif char == '"':
                    self.estado_anterior = 3
                    self.estado_actual = 4
                    if error==False:
                        self.guardar_token(token)
                        token = ''
                        self.guardar_token(char)
                else:
                    error = True
                    self.guardar_errores(char)

            elif self.estado_actual == 4:
                if char == ':':
                    self.estado_anterior = 4
                    self.estado_actual = 5
                    if error==False:
                        self.guardar_token(char)
                else:
                    error = True
                    self.guardar_errores(char)
                    self.estado_anterior = 4
                    self.estado_actual = 5

            elif self.estado_actual == 5:
                if char == '"':
                    self.estado_anterior = 5
                    self.estado_actual = 6
                    if error==False:
                        self.guardar_token(char)
                else:
                    error = True
                    self.guardar_errores(char)
                    self.estado_anterior = 5
                    self.estado_actual = 6


            elif self.estado_actual == 6:
                if char.lower() in self.letras:
                    self.estado_anterior = 6
                    self.estado_actual = 7
                    if error==False:
                        token += char
                else:
                    error = True
                    self.guardar_errores(char)
                    self.estado_anterior = 6
                    self.estado_actual = 7
            
            elif self.estado_actual == 7:
                if char.lower() in self.letras:
                    if error==False:
                        token += char
                    self.estado_anterior = 7
                    self.estado_actual = 7
                elif char == '"':
                    if error==False:
                        self.guardar_token(token)
                        token = ''
                        self.guardar_token(char)
                    self.estado_anterior = 7
                    self.estado_actual = 8
                else:
                    error = True
                    self.guardar_errores(char)

            
            elif self.estado_actual == 8:
                if char == '}':
                    if error==False:
                        self.guardar_token(char)
                        self.estado_anterior = 8
                        self.estado_actual = 9
                elif char == ',':
                    self.guardar_token(char)
                    self.estado_anterior = 8
                    self.estado_actual = 1
                    error=False
                else:
                    error = True
                    self.guardar_errores(char)

            
            elif self.estado_actual == 10:
                if char == '"':
                    if error==False:
                        self.guardar_token(char)
                    self.estado_anterior = 10
                    self.estado_actual = 11                 
                else:
                    error = True
                    self.guardar_errores(char)
                    self.estado_anterior = 10
                    self.estado_actual = 11  

            elif self.estado_actual == 11:
                if char.lower() in self.letras:
                    if error==False:
                        token += char
                    self.estado_anterior = 11
                    self.estado_actual = 12  
                else:
                    error = True
                    self.guardar_errores(char)
                    self.estado_anterior = 11
                    self.estado_actual = 12 

            elif self.estado_actual == 12:
                if char.lower() in self.letras:
                    if error==False:
                        token += char
                    self.estado_anterior = 12
                    self.estado_actual = 12
                elif char == '"':
                    if error==False:
                        self.guardar_token(token)
                        token = ''
                        self.guardar_token(char)
                    self.estado_anterior = 12
                    self.estado_actual = 13 
                else:
                    error = True
                    self.guardar_errores(char)

            elif self.estado_actual == 13:
                if char == ':':
                    if error==False:
                        self.guardar_token(char)
                    self.estado_anterior = 13
                    self.estado_actual = 14  
                else:
                    error = True
                    self.guardar_errores(char)
                    self.estado_anterior = 13
                    self.estado_actual = 14 

            elif self.estado_actual == 14:
                if char == '"':
                    if error==False:
                        self.guardar_token(char)
                    self.estado_anterior = 14
                    self.estado_actual = 15 
                else:
                    error = True
                    self.guardar_errores(char)
                    self.estado_anterior = 14
                    self.estado_actual = 15

            elif self.estado_actual == 15:
                if char.lower() in self.letras:
                    if error==False:
                        token += char
                    self.estado_anterior = 15
                    self.estado_actual = 16  
                else:
                    error = True
                    self.guardar_errores(char)
                    self.estado_anterior = 15
                    self.estado_actual = 16


            elif self.estado_actual == 16:
                if char.lower() in self.letras:
                    if error==False:
                        token += char
                    self.estado_anterior = 16
                    self.estado_actual = 16  

                elif char == '"':
                    self.estado_anterior = 16
                    self.estado_actual = 17
                    if error==False:
                        self.guardar_token(token)
                        tipo_operacion=token
                        token = ''
                        self.guardar_token(char)
                        op=Operacion(tipo_operacion)
                        valor = self.analizar(cadena[1:], op)
                        cadena = valor[0]
                        operandos.append(valor[1])
                else:
                    error = True
                    self.guardar_errores(char)

            elif self.estado_actual == 17:
                if char == ',':
                    if error==False:
                        self.guardar_token(char)
                    self.estado_anterior = 17
                    self.estado_actual = 18
                else:
                    error = True
                    self.guardar_errores(char)
                    self.estado_anterior = 17
                    self.estado_actual = 18

            elif self.estado_actual == 18:
                if char == '"':
                    if error==False:
                        self.guardar_token(char)
                    self.estado_anterior = 18
                    self.estado_actual = 19
                else:
                    error = True
                    self.guardar_errores(char)
                    self.estado_anterior = 18
                    self.estado_actual = 19

            elif self.estado_actual == 19:
                if char.lower() in self.letras:
                    if error==False:
                        token += char
                    self.estado_anterior = 19
                    self.estado_actual = 20 
                else:
                    error = True
                    self.guardar_errores(char)
                    self.estado_anterior = 19
                    self.estado_actual = 20 
                

            elif self.estado_actual == 20:
                if char.lower() in self.letras:
                    if error==False:
                        token += char
                    self.estado_anterior = 20
                    self.estado_actual = 20 

                elif char == '"':
                    if error==False:
                        self.guardar_token(token)
                        token = ''
                        self.guardar_token(char)
                    self.estado_anterior = 20
                    self.estado_actual = 21
                else:
                    error = True
                    self.guardar_errores(char)



            elif self.estado_actual == 21:
                if char == ':':
                    if error==False:
                        self.guardar_token(char)
                    self.estado_anterior = 21
                    self.estado_actual = 22
                else:
                    error = True
                    self.guardar_errores(char)
                    self.estado_anterior = 21
                    self.estado_actual = 22


            elif self.estado_actual == 22:
                if char == '[':
                    if error==False:
                        self.guardar_token(char)
                    self.estado_anterior = 22
                    self.estado_actual = 25
                elif char in self.numeros:
                    if error==False:
                        token += char
                    self.estado_anterior = 22
                    self.estado_actual = 23 
                else:
                    error = True
                    self.guardar_errores(char)

            elif self.estado_actual == 23:
                if char == ',':
                    if error==False:
                        self.guardar_token(token)
                        operandos.append(token)
                        token = ''                    
                        self.guardar_token(char)
                    self.estado_anterior = 23
                    self.estado_actual = 18
                elif char == '}':
                    self.estado_anterior = 23
                    self.estado_actual = 26
                    if error==False:
                        self.guardar_token(token)
                        operandos.append(token)
                        token = ''
                        self.guardar_token(char)
                        operacion.operandos = operandos
                        return [cadena, operacion]
                elif char.lower() in self.numeros:
                    if error==False:
                        token += char
                    self.estado_anterior = 23
                    self.estado_actual = 23
                elif char == ']':
                    self.estado_anterior = 23
                    self.estado_actual = 27
                    if error==False:
                        self.guardar_token(token)
                        operandos.append(token)
                        token = ''
                        self.guardar_token(char)   
                        if len(operandos)==2:
                            operacion.operandos = operandos
                            return [cadena, operacion]                                     
                elif char == '.':
                    if error==False:
                        self.guardar_token(token)
                        token = ''
                        self.guardar_token(char)
                    self.estado_anterior = 23
                    self.estado_actual = 24
                else:
                    error = True
                    self.guardar_errores(char)

            elif self.estado_actual == 24:   
                if char == ',':
                    if error==False:
                        self.guardar_token(token)
                        operandos.append(token)
                        token = ''
                        self.guardar_token(char)
                    self.estado_anterior = 24
                    self.estado_actual = 18
                elif char == '}':
                    self.estado_anterior = 24
                    self.estado_actual = 26
                    if error==False:
                        self.guardar_token(token)
                        operandos.append(token)
                        token = ''                    
                        self.guardar_token(char)
                        operacion.operandos = operandos
                        return [cadena, operacion]
                elif char.lower() in self.numeros:
                    if error==False:
                        token += char
                    self.estado_anterior = 24
                    self.estado_actual = 24
                elif char == ']':
                    self.estado_anterior = 24
                    self.estado_actual = 27
                    if error==False:
                        self.guardar_token(token)
                        operandos.append(token)        
                        token = ''
                        self.guardar_token(char)
                        operacion.operandos = operandos
                        return [cadena, operacion]
                else:
                    error = True
                    self.guardar_errores(char)
                    
            elif self.estado_actual == 25:
                if char == '"':
                    if error==False:
                        self.guardar_token(char)
                    self.estado_anterior = 25
                    self.estado_actual = 11
                else:
                    error = True
                    self.guardar_errores(char)
                    self.estado_anterior = 25
                    self.estado_actual = 11


            elif self.estado_actual == 26:
                if char == '}':
                    if error==False:
                        self.guardar_token(char)
                        self.estado_anterior = 26
                        self.estado_actual = 9 
                elif char == ',':
                    error=False
                    self.guardar_token(char)
                    self.estado_anterior = 26
                    self.estado_actual = 1
                else:
                    error = True
                    self.guardar_errores(char)

            elif self.estado_actual == 27:

                if char == ',':
                    self.estado_anterior = 27
                    self.estado_actual = 18
                    if error==False:
                        self.guardar_token(char)
                        if len(operandos)==1 and tipo_operacion.lower()=='seno':
                            operacion.operandos = operandos
                            return [cadena, operacion]
                        if len(operandos)==1 and tipo_operacion.lower()=='coseno':
                            operacion.operandos = operandos
                            return [cadena, operacion]
                        if len(operandos)==1 and tipo_operacion.lower()=='tangente':
                            operacion.operandos = operandos
                            return [cadena, operacion]
                        if len(operandos)==1 and tipo_operacion.lower()=='raiz':
                            operacion.operandos = operandos
                            return [cadena, operacion]
                        if len(operandos)==1 and tipo_operacion.lower()=='inverso':
                            operacion.operandos = operandos
                            return [cadena, operacion]
                        if len(operandos)==2:
                            operacion.operandos = operandos
                            return [cadena, operacion]                    
                elif char == ']':
                    if error==False:
                        self.guardar_token(char)
                    self.estado_anterior = 27
                    self.estado_actual = 27

                elif char == '}':
                    self.estado_anterior = 27
                    self.estado_actual = 26 
                    if error==False:
                        self.guardar_token(char)
                        operacion.operandos = operandos
                        return [cadena, operacion]
                else:
                    error = True
                    self.guardar_errores(char)
                

            self.columna += 1
            cadena = cadena[1:]

        operacion.operandos=operacion
        return [cadena,operandos]
        #return self.estado_actual in self.estados_aceptacion


    def guardar_token(self, lexema):
        nuevo_token = Token(self.fila, self.columna, lexema)
        self.tabla_tokens.append(nuevo_token)

    def guardar_errores(self, lexema):
        nuevo_error = Errores(self.fila, self.columna, lexema)
        self.tabla_errores.append(nuevo_error)
    
    def obtenr_tabla_errores(self):
        return self.tabla_errores
        

                
    def imprimir_tokens(self):
        print('-'*31)
        print ("| {:<4} | {:<7} | {:<10} |".format('Fila','Columna','Lexema'))
        print('-'*31)
        for token in self.tabla_tokens:
            print ("| {:<4} | {:<7} | {:<10} |".format(token.fila, token.columna, token.lexema))

    def imprimir_errores(self):
        for te in self.tabla_errores:
            numero_error=f'\t\t"No.":{te.id}\n'
            descripcion='\t\t"Descripcion-Token":{\n'
            caracter=f'\t\t\t"Lexema":{te.lexema}\n'
            tipo='\t\t\t"Tipo":Error\n'
            fila=f'\t\t\t"Fila":{te.fila}\n'
            columna=f'\t\t\t"Columna":{te.columna}\n'
            fin='\t\}\n'

            print('\t{\n'+numero_error+descripcion+caracter+tipo+fila+columna+fin+'\t}')



'''autom = Automata()
cadena = open('archivo.txt', 'r').read()

resultado = autom.analizar(cadena , Operacion('sexo'))
autom.imprimir_tokens()
autom.imprimir_errores()
errorOperacion=0
if autom.estado_actual in autom.estados_aceptacion:
    for oper in resultado[1]:
        try:
            resultado = oper.operar()
            print(resultado[0], "=", resultado[1])
        except Exception as e:
            print("Hubo un error LPTM!!! :/ :(")'''
