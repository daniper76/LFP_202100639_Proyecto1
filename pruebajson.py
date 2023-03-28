from archivoErrores import tabla_errores_total

for te in tabla_errores_total:
        # Crear un diccionario con los atributos del objeto
    diccionario = {
        "No.": {te.id},
        "Descripcion-Token": {
            "Lexema": {te.lexema},
            "Tipo": "Error",
            "Fila": {te.fila},
            "Columna": {te.columna}
        }
    }

print(diccionario)