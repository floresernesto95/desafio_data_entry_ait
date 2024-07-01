from models.descargar_listas_precios import DescargarListasPrecios
from models.procesador import Procesador
from models.subir_archivos import SubirArchivos

def main():
    # Instalar el archivo "requirements.txt".
    # Crear en el directorio root, el directorio resources con los directorios processed y unprocessed.
    # Cambiar en el método "DescargarListasPrecios" el "default_directory" path por tu absolute path.
    DescargarListasPrecios.iniciar()
    Procesador.iniciar()

    # Nota: La API devuelve "missing columns" cuando cada archivo .xlsx contiene las columnas pedidas.
    SubirArchivos.iniciar()

if __name__ == "__main__":
    main()



