# modulo_io.py

# Definición de función que imprime cosas sin devolver nada
def conversar(actor1, actor2):
    print(f"\n_Hola, {actor1}!")
    print(f"_Hola, {actor2}!")
    print("_Pasó usted ya por casa?")
    print("_Por su casa yo pasé.")
    print(f"_Adiós, {actor1}!")
    print(f"_Adiós, {actor2}!\n")

# Definición de excepción personalizada (que hereda de Exception)
class ErrorNombreInvalido(Exception):
    """Excepción lanzada cuando el nombre ingresado no es válido."""
    pass

# Definición de excepción personalizada (que hereda de Exception)
class ErrorEdadInvalida(Exception):
    """Excepción lanzada cuando la edad ingresada no es válida."""
    pass

nombres_prohibidos = ["user", "User", "USER", "admin", "Admin", "ADMIN"]

# Definición de función de entrada-salida que lanza las excepciones anteriores
def ingresar_datos():
    nombre = input("\nIngrese su nombre: ")
    if nombre in nombres_prohibidos:
        raise ErrorNombreInvalido("Debe ingresar un nombre válido.") # usamos raise para lanzar excepciones.
    edad = int(input("Ingrese su edad "))
    if(edad >= 18):
        print(f"\n¡Hola, {nombre}! Usted está habilitado para votar.") # usamos un f-string para insertar variables dentro de la cadena.
    elif(edad > 0):
        print(f"\n¡Hola, {nombre}! Usted es menor de edad, no puede votar.")
    else:
        raise ErrorEdadInvalida("Debe ingresar una edad válida.")

# Wrapper que llama a la función anterior en un bloque try-except
def try_ingresar_datos():
    try:
        ingresar_datos()
    except ErrorNombreInvalido as e:
        print(f"Error: {str(e)}")
    except ErrorEdadInvalida as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"Error inesperado: {e}")
