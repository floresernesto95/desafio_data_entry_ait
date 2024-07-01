import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Aquí no utilice "undetected_chromedriver", ya que, la página no presentaba problemas para la
# implementación del bot.
class DescargarListasPrecios:
    @staticmethod
    def iniciar():
        # Configuración de las opciones para el navegador Chrome.
        chrome_options = Options()

        # Añade opciones experimentales al navegador. En este caso, se configura el directorio
        # predeterminado de descargas, deshabilita la ventana de descarga automática,
        # permite actualizaciones en el directorio de descargas y habilita la protección de navegación segura.
        chrome_options.add_experimental_option('prefs', {
            "download.default_directory": r'D:\IT\.Proyectos\Ciencia de datos\Automatizador de ingreso de datos jr\Desafio-Data-Entry\resources\unprocessed',
            "download.prompt_for_download": False, # Para descargar archivos automáticamente sin preguntar.
            "download.directory_upgrade": True, # Permite mejoras en el directorio de descargas.
            "safebrowsing.enabled": True # Activa la navegación segura.
        })

        # Crea y retorna una nueva instancia del driver de Chrome, configurado con las opciones anteriores.
        # Esto permite controlar el navegador de forma programática con estas configuraciones específicas.
        driver = webdriver.Chrome(options=chrome_options)

        try:
            # Navega al sitio web especificado.
            driver.get('https://desafiodataentryfront.vercel.app/')
            # Espera implícita de hasta 10 segundos para que los elementos de la página se carguen antes de lanzar una excepción por tiempo de espera.
            driver.implicitly_wait(10)

            # AUTOREPUESTOS EXPRESS
            # Busca el botón de descarga por ID y haz clic en él.
            download_button = driver.find_element(By.ID, 'download-button-autorepuestos-express')
            download_button.click()

            # Espera de 5 segundos para manejar dinámicas de la página que podrían demorar en cargarse.
            time.sleep(5)

            # AUTOFIX
            # Encuentra y haz clic en el segundo botón de descarga.
            second_download_button = driver.find_element(By.ID, 'download-button-autofix')
            second_download_button.click()

            # Espera 5 segundos para que la nueva página se cargue.
            time.sleep(5)

            # Localiza los campos de usuario y contraseña e introduce las credenciales.
            user_field = driver.find_element(By.ID, 'username')
            password_field = driver.find_element(By.ID, 'password')
            user_field.send_keys('desafiodataentry')
            password_field.send_keys('desafiodataentrypass')

            # Busca el botón de descarga por ID y haz clic en él.
            download_button = driver.find_element(By.ID, 'login-button')
            download_button.click()

            # Espera a que la nueva página se cargue.
            time.sleep(5)

            # Itera sobre los botones de marca del 1 al 7.
            for i in range(1, 8):
                # Construye el ID para la marca actual.
                marca_id = f'marca-{i}'

                # Encuentra y haz clic en el botón de la marca actual.
                marca_button = driver.find_element(By.ID, marca_id)
                marca_button.click()

                # Espera para manejar dinámicas potenciales de la página.
                time.sleep(5)

                # Encuentra y haz clic en el botón de descarga.
                download_button = driver.find_element(By.ID, 'download-button')
                download_button.click()

                # Espera a que la descarga finalice.
                time.sleep(20)

                # Desactiva el botón de la marca actual (si se comporta como un interruptor).
                marca_button.click()

                # Opcionalmente espera un poco antes de proceder al siguiente botón.
                time.sleep(5)

            # Navega dos páginas hacia atrás.
            driver.back()
            time.sleep(5) # Espera un poco para que la página se cargue.
            driver.back()
            time.sleep(5) # Espera un poco para que la página se cargue.

            # MUNDO REPCAR
            # Encuentra el botón de descarga por ID y haz clic en él.
            download_button = driver.find_element(By.ID, 'download-button-mundo-repcar')
            download_button.click()

            # Espera a que la nueva página se cargue.
            time.sleep(5)

            # Encuentra y haz clic en el botón de descarga.
            download_button = driver.find_element(By.ID, 'download-link')
            download_button.click()

            # Espera a que la descarga finalice.
            time.sleep(5)  # Ajusta el tiempo según la velocidad de conexión y el tamaño del archivo.

        finally:
            # Cierra el navegador.
            driver.quit()