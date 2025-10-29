# modulo_estandar.py

# Importa módulos y funciones de la biblioteca estándar
import math
from random import randint
from datetime import datetime

def imprimir_operaciones():
    print(f"\nLa raiz cuadrada entera de 25 es: {math.isqrt(25)}")
    print(f"La raiz cuadrada de 2 es: {math.sqrt(2)}")
    print(f"La raiz cuadrada de -4 es: {(-4) ** (1/2)}")
    print(f"El factorial de 8 es: {math.factorial(8)}")
    print(f"El GCD entre 175 y 165 es: {math.gcd(175, 165)}")
    print(f"El LCM entre 17 y 35 es: {math.lcm(17, 35)}")
    pi = math.pi
    print(f"El valor de pi es: {pi}")
    print(f"El techo de pi es: {math.ceil(pi)}")
    print(f"El piso de pi es: {math.floor(pi)}")
    print(f"El logaritmo en base 2 de 4096 es: {math.log2(4096)}")
    print(f"El resultado de elevar 2 a la 16 es: {math.pow(2, 16)}")
    print(f"El seno de 0 es: {math.sin(math.radians(0))}")
    print(f"El arcoseno de 1 es: {math.degrees(math.asin(1))}°")
    print(f"El coseno de 0° es: {math.cos(math.radians(0))}")
    print(f"El arcotangente de 1 es: {math.degrees(math.atan(1))}°")

def imprimir_aleatorios():
    print(f"\nNúmero aleatorio del 1 al 10: {randint(1, 10)}")
    print(f"Número aleatorio del 10 al 99: {randint(10, 99)}")

def imprimir_fecha_y_hora_actual():
    print(f"\nLa fecha y hora actual es: {datetime.now()}")