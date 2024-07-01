import os
import requests

class SubirArchivos:
    @staticmethod
    def iniciar():
        directory = r'resources/processed' # Ruta al directorio 'processed'.
        url = 'https://desafio.somosait.com/api/upload/' # URL del API para subir archivos.

        # Itera sobre todos los archivos en el directorio
        for filename in os.listdir(directory):
            if filename.endswith('.xlsx'): # Selecciona solo archivos con extensión ".xlsx".
                file_path = os.path.join(directory, filename) # Construye el camino completo del archivo.

                # Abre y sube cada archivo Excel
                with open(file_path, 'rb') as file:
                    files = {'file': file}
                    response = requests.post(url, files=files) # Realiza la petición POST al API.

                    # Imprime el nombre del archivo y la respuesta del API.
                    print(f"File: {filename}")
                    print(f"Response Status Code: {response.status_code}")
                    print(f"Response Text: {response.text}")
                    print("\n")