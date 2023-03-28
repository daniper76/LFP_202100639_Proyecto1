from archivoErrores import tabla_errores_total
import json


with open("archivo.json", "w") as archivo:
    for te in tabla_errores_total:
            numero_error=f'\t\t"No.":{te.id}\n'
            descripcion='\t\t"Descripcion-Token":{\n'
            caracter=f'\t\t\t"Lexema":{te.lexema}\n'
            tipo='\t\t\t"Tipo":Error\n'
            fila=f'\t\t\t"Fila":{te.fila}\n'
            columna=f'\t\t\t"Columna":{te.columna}\n'
            fin='\t\}\n'
            valor='\t{\n'+f'{numero_error}'+','+f'{descripcion}'+','+f'{caracter}'+','+f'{tipo}'+','+f'{fila}'+','+f'{columna}'+f'{fin}'+'\t}'
            json.dump(valor, archivo,indent=4)

archivo.close()
