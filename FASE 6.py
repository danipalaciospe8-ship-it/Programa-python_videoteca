# ==========================================
# Videoteca Digital
# Autor: Daniel Palacios
# ==========================================

# Matriz con la información de los títulos

videoteca = [
    ["Avatar", 2009, 8, "Ciencia Ficción"],
    ["Interestelar", 2014, 10, "Ciencia Ficción"],
    ["Frozen", 2013, 7, "Animación"],
    ["Rápidos y Furiosos 5", 2011, 8, "Acción"],
    ["Minions", 2015, 7, "Animación"],
    ["Cars 3", 2017, 8, "Animación"],
    ["Matrix", 1999, 9, "Ciencia Ficción"]
]

# Función para contar títulos que cumplen criterios


def contar_titulos(matriz, calificacion_minima, año_limite):
    contador = 0

    for titulo in matriz:
        nombre = titulo[0]
        año = titulo[1]
        calificacion = titulo[2]
        genero = titulo[3]

        # Condición combinada con AND
        if calificacion >= calificacion_minima and año >= año_limite:
            contador += 1

    return contador

# Parámetros de búsqueda

calificacion_minima = 8
año_limite = 2010

resultado = contar_titulos(videoteca, calificacion_minima, año_limite)

print("Cantidad de títulos que cumplen los criterios:", resultado)