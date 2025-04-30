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
        raise ValueError("error: hay valores nan en la vector")
    if vector.ndim != 1: #verificacion si es UNIDIMENSIONAL
        raise TypeError("error: no es un vector")


# Propiedades Aritmeticas

def propiedad_conmutativa(A, B, operacion = "suma"):
    validar_vector(A)
    validar_vector(B)

    operacion = operacion.lower()

    if operacion == "multiplicacion":
        izq = A * B
        der = B * A
    else:
        izq = A + B
        der = B + A

    return np.array_equal(izq, der)

def propiedad_asociativa(A, B, C, operacion = "suma"):
    validar_vector(A)
    validar_vector(B)
    validar_vector(C)

    operacion = operacion.lower()

    if operacion == "multiplicacion":
        izq = (A * B) * C
        der = A * (B * C)
    else:
        izq = (A + B) + C
        der = A + (B + C)

    return np.array_equal(izq, der)

def propiedad_distributiva(A, B, C):
    validar_vector(A)
    validar_vector(B)
    validar_vector(C)

    izq = A * (B + C)
    der = A * B + A * C

    return np.array_equal(izq, der)

def propiedad_identidad(A, operacion = "suma"):
    validar_vector(A)

    if operacion == "multiplicacion":
       identidad = np.ones_like(A)
       resultado = A * identidad
    else:
        identidad = np.zeros_like(A)
        resultado = A + identidad

    return np.array_equal(resultado, A)

def propiedad_inversa(A, operacion = "suma"):
    validar_vector(A)

    if operacion == "multiplicacion":
        if np.any(A == 0): return False
        inverso = 1 / A
        resultado = A * inverso
        return np.array_equal(resultado, np.ones_like(A))
    else:
        inverso = -A
        resultado = A + inverso
        return np.array_equal(resultado, np.zeros_like(A))

# ---------------------------
# USO Y PRUEBA
# ---------------------------
A = generar_matriz(3, 1)
B = generar_matriz(3, 1)
C = generar_matriz(3, 1)

print("Matriz A:\n", A)
print("Matriz B:\n", B)
print("Matriz C:\n", C)

print("Conmutativa suma:", propiedad_conmutativa(A, B))
print("Conmutativa multiplicacion:", propiedad_conmutativa(A, B, "multiplicacion"))
print("Asociativa suma:", propiedad_asociativa(A, B, C))
print("Asociativa multiplicacion:", propiedad_asociativa(A, B, C, "multiplicacion"))
print("Distributiva:", propiedad_distributiva(A, B, C))
print("Identidad aditiva:", propiedad_identidad(A))
print("Identidad multiplicativa:", propiedad_identidad(A, "multiplicacion"))
print("Inverso aditivo:", propiedad_inversa(A))
print("Inverso multiplicativo:", propiedad_inversa(A, "multiplicacion"))