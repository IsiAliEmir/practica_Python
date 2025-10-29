# modulo_operaciones.py

# Función con valor de retorno
def operar(a, b):
    return (a + 3) * (b - 1) - (a * b)

# Función que recibe una tupla y devuelve el doble de cada nro. par
def map1(valores):
    return [x * 2 for x in valores if x % 2 == 0]

# Función que recibe una tupla y devuelve el triple de cada nro. impar
def map2(valores):
    return [x * 3 for x in valores if x % 2 != 0]

# Función con cantidad variable de parámetros (args) + documentación (docstring)
def promedio(*valores):
    """
    Calcula el promedio de una colección de elementos de tamaño variable.

    Args:
        valores: la colección de valores numéricos.

    Returns:
        int: el promedio de dichos valores.
    """
    suma = sum(valores)
    cantidad = len(valores)
    return suma / cantidad

# Función con manejo de excepciones (bloque try-except)
def dividir_y_sumar(a, b):
    try:
        resultado = a/b + (a*b)
        print("El resultado de dividir y sumar el producto de", a, "con", b, "es:", resultado)
    except ZeroDivisionError:
        print("Error: división por cero.")
    except TypeError:
        print("Error: los parámetros deben ser numéricos.")