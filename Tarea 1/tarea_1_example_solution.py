# Código desarrollado por Francisco López y Daniel Quesada

def separa_letras(Cadena):
    error = 0
    mayusculas = ""  # String al que se le asignan las mayúsculas
    minusculas = ""  # String al que se le asignan las minúsculas
    if isinstance(Cadena, str):   # Valida que Cadena sea string
        if Cadena != "":          # Valida que la cadena no esté vacía
            if Cadena.isalpha():  # Valida que la cadena solo contenga letras
                error = 0
                # Avanza por todas las letras de Cadena
                for caracter in Cadena:
                    # Si el caracter es una letra mayúscula
                    if caracter.isupper():
                        mayusculas = mayusculas + caracter
                    # Si el caracter es una letra minúscula
                    elif caracter.islower():
                        minusculas = minusculas + caracter
            else:
                error = -200      # Error por caracteres inválidos
                mayusculas = None
                minusculas = None
        else:
            error = -300          # Parámetro es un string vacío
            mayusculas = None
            minusculas = None
    else:
        error = -100              # Error por parámetro no de tipo string
        mayusculas = None
        minusculas = None
    return error, mayusculas, minusculas  # Return final de la función


def potencia_manual(base, potencia):
    error = 0    # Código de error
    result = 1   # Resultado de la potencia
    if isinstance(base, str) or isinstance(potencia, str):  # Valida parámetros
        error = -400
        result = None
    else:   # Parámetros son válidos
        error = 0
        result_aux = 0   # Variable auxiliar para guardar el resultado parcial
        # Cada vez se obtiene result = result * base, se hace 'potencia' veces
        for i in range(potencia):
            # Obtiene result_aux = result * base (suma result 'base' veces)
            for j in range(base):
                result_aux += result
            # Se guarda el resultado de (result * base) en result
            # Actualiza su valor
            result = result_aux
            result_aux = 0   # Reinicia la variable auxiliar
    return error, result

# result comienza en 1 para que si el exponente es 0,
# no se entre al ciclo y el resultado sea 1
