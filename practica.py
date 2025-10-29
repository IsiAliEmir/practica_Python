def main():
    print("\nHola mundo!! Aquí inicia el programa principal.")

    # Tipos de dato simples
    nombre = "Juan"
    edad = 25
    altura = 1.75
    es_estudiante = True

    # Punto y coma para separar sentencias en una misma línea
    nombre = "Fulano"; edad = 22; altura = 1.77; es_estudiante = False 

    # Estructuras de control: if, elif, else
    if edad >= 65:
        print("Juan es jubilado.")
    elif edad >= 40 and edad != 60:
        print("Juan es un adulto mayor.")
    elif edad == 60:
        print("Juan tiene exactamente 60 años.")
    elif edad < 40 and edad >= 18:
        print("Juan es un adulto joven.")
    else:
        print("Juan es menor de edad.")

    # Operadores aritméticos y lógicos
    a = 10; b = 2
    if (a % 2 == 0) and (b % 2 == 0):
        print("Ambos numeros son pares.\n")
    else:
        print("Alguno de los dos es impar.\n")

    print("- El resultado de hacer", a, "a la", b, "es:", a ** b)
    print("- El cociente de la división entera de", a, "por", b, "es:", a // b)
    print("- El resto de la divsión entera de", a, "por", b, "es:", a % b)

    # Bucles for y while, con break, continue y pass
    print("\nCuenta regresiva desde 5:")
    contador = 5
    while contador >= 0:
        print(contador)
        contador -= 1

    print("\nNúmeros del 0 al 5, multiplicados por 2:")
    for numero in range(0, 6):
        print(numero * 2)

    print("\nAlgunas potencias de 2:")
    contador = 2
    while True:
        print(contador)
        contador *= 2
        if contador > 1024:
            break

    print("\nNúmeros pares del 0 al 10:")
    for i in range(11):
        if i % 2 != 0:
            continue
        print(i)

    print("\nOperatoria del 0 al 10:")
    for i in range(11):
        if i % 2 == 0:
            pass # operacion nula (placeholder)
        else:
            print(i*2 + 1)

    # Listas y operaciones con listas
    print("\nLista inicial de frutas:")
    frutas = ["manzana", "banana", "pera"]
    for fruta in frutas:
        print(" -", fruta)

    print("\nAgrego naranja, sandia y durazno:")
    frutas.append("naranja")
    frutas.append("sandia")
    frutas.append("durazno")
    print(frutas)

    print("\nInserto mandarina y quito banana:")
    frutas.insert(0, "mandarina")
    frutas.remove("banana")
    print(frutas)

    print("\nPrimera fruta: ", frutas[0])
    print("Segunda fruta: ", frutas[1])
    print("Última fruta: ", frutas[-1])
    print("Anteúltima fruta: ", frutas[-2])

    print("\nQuito la tercera y las ordeno de menor a mayor:")
    fruta_eliminada = frutas.pop(2)
    print("Fruta eliminada: ", fruta_eliminada)
    frutas.sort()
    print(frutas)

    print("\nLas ordeno en reverse:")
    frutas.reverse()
    print(frutas)

    print("\nElementos de una listita heterogénea random:")
    listita = ["manzana", 1, "Juan", 7.8, True]
    print(listita)

    numeritos = [2, 0, 1, 5, -3, 6, 9, 4, -7]
    print("\nNumeritos: ", numeritos)

    cuadrados = [x ** 2 for x in numeritos]
    print("Cuadrados: ", cuadrados)

    # Creo una nueva lista a partir de transformar y filtrar una anterior
    raices_cuadradas = [x ** (1/2) for x in numeritos if x >= 0] 
    print("Raíces cuadradas: ", raices_cuadradas)

    divisores_de_30 = [x for x in range(1, 31) if (30 % x == 0)]
    print("Divisores de 30: ", divisores_de_30, "\n")

    # Tuplas
    coordenadas = (12.48, 7.09)
    print("Coordenadas:", coordenadas)

    ninetales = ("Ninetales", 73, 76, 75, 81, 100, 100)
    print("Ninetales:", ninetales)

    IVs = (12, 15, 8, 9, 9, 6)
    print("IVs:", IVs)
    print("- Cant de 15s:", IVs.count(15))
    print("- Cant de 0s:", IVs.count(0))

    # Diccionarios
    joan = {"nombre":"Joan", "edad":25, "altura":1.77, "ciudad":"Barcelona", "estudia":True, "trabaja":False}
    print("\nJoan (inicial):", joan)

    print("- Altura:", joan["altura"])
    print("- Trabaja:", joan["trabaja"])
    print("- Ciudad:", joan.get("ciudad"))
    print("- Profesion:", joan.get("profesion"))

    print("\nClaves:", joan.keys())
    print("Valores:", joan.values())
    print("Items:", joan.items())

    joan.update({"ciudad":"Paris", "trabaja":True, "profesion":"Ingeniero"})
    print("\nJoan (update):", joan)

    # Conjuntos y operaciones sobre conjuntos
    A = {2, 2, 4, 6, 8}
    print("\nA =", A)
    B = {0, 2, 1, 3, 3, 7}
    print("B =", B)

    print("\nA v B =", A | B)
    print("A ^ B =", A & B)
    print("A - B =", A - B)
    print("A dif.sim B =", A ^ B)

    A.add(0)
    B.discard(0)
    B.discard(4) # si no está el elemento, no pasa nada.
    B.remove(2) # si no está el elemento, genera un error.
    B.add(5)

    print("\nA =", A)
    print("B =", B)

    B.clear()
    print("\nB =", B)
    print("A ^ B =", A & B)

    ################################################## MÓDULO 2 ###################################################
    from mi_paquete import modulo_archivos, modulo_estandar, modulo_io, modulo_operaciones

    modulo_io.conversar("Don Pepito", "Don José")
    print("El resultado de operar 2 con 3 es:", modulo_operaciones.operar(2, 3))

    # Función lambda ad hoc
    combinar = lambda x, y: 2*x + 3*y
    print("\nEl resultado de combinar 2 con 3 es:", combinar(2, 3))
    print("El resultado de combinar 4 con 6 es:", combinar(4, 6))
    print("El resultado de combinar 1 con 1.5 es:", combinar(1, 1.5))

    valores = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print("\nSean los valores", valores)
    print("- El resultado de map1 es:", modulo_operaciones.map1(valores))
    print("- El resultado de map2 es:", modulo_operaciones.map2(valores))
    print("\nEl promedio de (1, 5, 24) es:", modulo_operaciones.promedio(1, 5, 24))
    print("El promedio de (-4, 5, 7, 8, 9) es:", modulo_operaciones.promedio(-4, 5, 7, 8, 9))

    valores = (14, 16, 18, 21, 22, 25, 28, 20, 24, 28, 30)
    print("\nSean los valores:", valores)
    print("- El promedio es:", modulo_operaciones.promedio(*valores))
    print("- El máximo es:", max(valores))
    print("- El mínimo es:", min(valores), "\n")

    modulo_operaciones.dividir_y_sumar(4, 0)
    modulo_operaciones.dividir_y_sumar("4", 2)
    modulo_operaciones.dividir_y_sumar(5, 5)

    # modulo_io.try_ingresar_datos()

    # Lectura y escritura de archivos
    print(f"Se leyó: {modulo_archivos.leer_archivo("quote.txt")}")
    modulo_archivos.escribir_archivo("borrador.txt", "El amor y la afición con facilidad ciegan los ojos del entendimiento.")
    print(f"Se leyó: {modulo_archivos.leer_archivo("borrador.txt")}")

    modulo_archivos.mostrar_header("imagen.png")
    modulo_archivos.mostrar_header("quote.txt")
    modulo_archivos.mostrar_header("practica.py")

    modulo_archivos.copiar("quote.txt", "borrador.txt")

    modulo_estandar.imprimir_operaciones()
    modulo_estandar.imprimir_aleatorios()
    modulo_estandar.imprimir_fecha_y_hora_actual()

    print("\nFin del programa.")

if __name__ == "__main__":
    main()