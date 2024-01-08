import re

# Función para verificar si una cadena es una dirección de correo válida
def es_direccion_correo(cadena):
    # Utilizamos una expresión regular simple para verificar si la cadena tiene el formato de una dirección de correo electrónico
    patron_correo = re.compile(r"[^@]+@[^@]+\.[^@]+")
    return bool(re.match(patron_correo, cadena))

# Lista para almacenar las líneas modificadas
lineas_modificadas = []

# Abrir el archivo en modo lectura con codificación UTF-8
with open("HBO1.txt", "r", encoding="utf-8") as archivo:
    # Leer todas las líneas del archivo
    lineas = archivo.readlines()

# Iterar sobre cada línea
for linea in lineas:
    # Dividir la línea en conjuntos de datos usando "|"
    conjuntos = linea.split("|")

    # Iterar sobre cada conjunto de datos
    for conjunto in conjuntos:
        # Verificar si hay una dirección de correo y una contraseña en el conjunto
        if ":" in conjunto:
            # Dividir el conjunto en dirección de correo y contraseña usando ":"
            datos_divididos = conjunto.split(":")
            
            # Extraer la dirección de correo y la contraseña
            correo = datos_divididos[0].strip()  # Eliminar espacios al inicio y al final
            contrasena = datos_divididos[1].strip()  # Eliminar espacios al inicio y al final
            
            # Verificar si la cadena extraída es una dirección de correo válida antes de modificar el conjunto
            if es_direccion_correo(correo):
                # Agregar la línea con correo y contraseña separados a la lista de líneas modificadas
                linea_modificada = f"{correo}:{contrasena}\n"
                lineas_modificadas.append(linea_modificada)

# Abrir el archivo en modo escritura con codificación UTF-8
with open("CREDENCIALES_ORDENADAS.txt", "w", encoding="utf-8") as archivo_modificado:
    # Escribir las líneas modificadas en el nuevo archivo
    archivo_modificado.writelines(lineas_modificadas)
