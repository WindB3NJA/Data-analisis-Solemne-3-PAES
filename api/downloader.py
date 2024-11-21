from urllib import request
import os, pathlib

# URL del archivo.
url = "https://datosabiertos.mineduc.cl/wp-content/uploads/2024/05/PAES-2024-Inscritos-Puntajes.rar"
# Descargar el archivo.
request.urlretrieve(url, "api/Dataframe.rar")

# Ruta del archivo.
ROOT = pathlib.Path(os.getcwd())
# Listar los archivos.
Folder_images = os.listdir(ROOT)
