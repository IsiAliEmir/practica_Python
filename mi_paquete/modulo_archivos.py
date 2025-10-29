# modulo_archivos.py

# Abre un archivo en modo lectura y devuelve su contenido
def leer_archivo(ruta):
    try:
        print(f"\nAbriendo archivo {ruta} en modo lectura...")
        with open(ruta, "r") as archivo: # with open hace el close.archivo() automáticamente.
            print("Lectura exitosa.")
            return archivo.read()
    except FileNotFoundError:
        print("Error: el archivo no existe.")
    except PermissionError:
        print("Error: faltan permisos para leer el archivo.")

# Abre un archivo en modo escritura y le escribe lo ingresado por parámetro
def escribir_archivo(ruta, cadena):
    try:
        print(f"\nAbriendo archivo {ruta} en modo escritura...")
        with open(ruta, "w") as archivo: # si no existe lo crea, y si ya existe lo sobrescribe.
            archivo.write(cadena)
        print("Escritura exitosa.")
    except PermissionError:
        print("Error: faltan permisos para escribir el archivo.")
    except OSError as e:
        print(f"Error del sistema al escribir el archivo: {e}")

# Lee los primeros 16 bytes en hex de un archivo pasado por parámetro
def mostrar_header(ruta, n=16):
    try:
        print(f"\nAbriendo archivo '{ruta}' en modo lectura binaria...")
        with open(ruta, "rb") as f:
            header = f.read(n)
        print("Header bytes:", header)
        print("Hex:", " ".join(f"{b:02X}" for b in header))
    except FileNotFoundError:
        print("Error: el archivo no existe.")
    except PermissionError:
        print("Error: faltan permisos para leer el archivo.")

# Copia el contenido << EN BYTES >> de un archivo a otro
def copiar(fuente, recipiente):
    try:
        print(f"\nAbriendo archivo {fuente} en modo lectura binaria...")
        with open(fuente, "rb") as f:
            datos = f.read()
            print("Lectura exitosa.")    
    except FileNotFoundError:
        print("Error: el archivo no existe.")
    except PermissionError:
        print("Error: faltan permisos para leer el archivo.")
    try:
        print(f"\nAbriendo archivo {recipiente} en modo escritura binaria...")
        with open(recipiente, "wb") as f: # si no existe lo crea, y si ya existe lo sobrescribe.
            f.write(datos) # escribo lo que había leído del anterior. Es decir, hago una copia exacta.
            print("Copia exitosa.")
    except PermissionError:
        print("Error: faltan permisos para escribir el archivo.")