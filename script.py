import numpy as np

# Generacion

def generar_matriz(filas, columnas, random=True):
    if filas <= 0 or columnas <= 0:
        raise ValueError("Filas o Columnas NO VALIDOS")
    
    if filas == 1 or columnas == 1: #CONVERSION DIRECTA A VECTOR
        tamaño = filas * columnas
        if random:
            matriz = np.random.randint(0, 10, size = tamaño)
        else:
            matriz = np.zeros(tamaño)
    else:
        if random:
            matriz = np.random.randint(0, 10, size = (filas, columnas))
        else:
            matriz = np.zeros((filas, columnas))

    return matriz

# Validacion

def validar_matriz(matriz):
    if matriz is None:
        raise ValueError("error: la matriz es de tipo None")
    if not isinstance(matriz, np.ndarray):
        raise TypeError("error: no es un arreglo de numpy")
    if matriz.size == 0:
        raise ValueError("error: el arreglo esta vacio")
    if np.isnan(matriz).any():
        raise ValueError("error: hay valores nan en la matriz")

def validar_vector(vector):
    if vector is None:
        raise ValueError("error: el vector es de tipo None")
    if not isinstance(vector, np.ndarray):
        raise TypeError("error: no es un arreglo de numpy")
    if vector.size == 0:
        raise ValueError("error: el vector esta vacio")
    if np.isnan(vector).any():
        raise ValueError("error: hay valores nan en el vector")
    if vector.ndim != 1: #verificacion si es UNIDIMENSIONAL
        raise TypeError("error: no es un vector")


# Propiedades Aritmeticas

def propiedad_conmutativa(A, B, operacion = "suma"):
    validar_matriz(A)
    validar_matriz(B)

    if A.shape != B.shape:
        raise ValueError("Las matrices no tienen la misma forma")

    operacion = operacion.lower()

    if operacion == "multiplicacion":
        izq = A * B
        der = B * A
    else:
        izq = A + B
        der = B + A

    return np.array_equal(izq, der)

def propiedad_asociativa(A, B, C, operacion = "suma"):
    validar_matriz(A)
    validar_matriz(B)
    validar_matriz(C)
    
    if A.shape != B.shape or B.shape != C.shape:
        raise ValueError("Las matrices no tienen la misma forma")

    operacion = operacion.lower()

    if operacion == "multiplicacion":
        izq = (A * B) * C
        der = A * (B * C)
    else:
        izq = (A + B) + C
        der = A + (B + C)

    return np.array_equal(izq, der)

def propiedad_distributiva(A, B, C):
    validar_matriz(A)
    validar_matriz(B)
    validar_matriz(C)

    if A.shape != B.shape or B.shape != C.shape:
        raise ValueError("Las matrices no tienen la misma forma")

    izq = A * (B + C)
    der = A * B + A * C

    return np.array_equal(izq, der)

def propiedad_identidad(A, operacion = "suma"):
    validar_matriz(A)

    if operacion == "multiplicacion":
       identidad = np.ones_like(A)
       resultado = A * identidad
    else:
        identidad = np.zeros_like(A)
        resultado = A + identidad

    return np.array_equal(resultado, A)

def propiedad_inversa(A, operacion = "suma"):
    validar_matriz(A)

    if operacion == "multiplicacion":
        if np.any(A == 0): return False
        inverso = 1 / A
        resultado = A * inverso
        return np.array_equal(resultado, np.ones_like(A))
    else:
        inverso = -A
        resultado = A + inverso
        return np.array_equal(resultado, np.zeros_like(A))
    

# interaccion

def mostrar_menu():
    print("\nElige una propiedad para probar:")
    print("1. Conmutativa suma")
    print("2. Conmutativa multiplicacion")
    print("3. Asociativa suma")
    print("4. Asociativa multiplicacion")
    print("5. Distributiva")
    print("6. Identidad aditiva")
    print("7. Identidad multiplicativa")
    print("8. Inverso aditivo")
    print("9. Inverso multiplicativo")
    print("0. Salir")

def ejecutar_opcion(opcion, A, B, C):
    if opcion == "1":
        print("Conmutativa suma:", propiedad_conmutativa(A, B))
    elif opcion == "2":
        print("Conmutativa multiplicacion:", propiedad_conmutativa(A, B, "multiplicacion"))
    elif opcion == "3":
        print("Asociativa suma:", propiedad_asociativa(A, B, C))
    elif opcion == "4":
        print("Asociativa multiplicacion:", propiedad_asociativa(A, B, C, "multiplicacion"))
    elif opcion == "5":
        print("Distributiva:", propiedad_distributiva(A, B, C))
    elif opcion == "6":
        print("Identidad aditiva:", propiedad_identidad(A))
    elif opcion == "7":
        print("Identidad multiplicativa:", propiedad_identidad(A, "multiplicacion"))
    elif opcion == "8":
        print("Inverso aditivo:", propiedad_inversa(A))
    elif opcion == "9":
        print("Inverso multiplicativo:", propiedad_inversa(A, "multiplicacion"))
    elif opcion == "0":
        print("Saliendo")
    else:
        print("Opcion Invalida")

def creacion_matriz(nombre="matriz"):
    try:
        filas = int(input(f"Ingrese numero de filas para {nombre}: "))
        columnas = int(input(f"Ingrese numero de columnas para {nombre}: "))
        rand = input("TIPO DE CREACION (random/zero): ").strip().lower()
        aleatorio = rand == 'random'
        vec = generar_matriz(filas, columnas, aleatorio)
        print(f"{nombre} generado:\n{vec}")
        return vec
    except Exception as e:
        print("error:", e)
        return creacion_matriz(nombre)

# ejecucion
A = creacion_matriz("A")
B = creacion_matriz("B")
C = creacion_matriz("C")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")
    if opcion == "0":
        break
    try:
        ejecutar_opcion(opcion, A, B, C)
    except Exception as e:
        print("SE ENCONTRO UN ERROR:", e)
