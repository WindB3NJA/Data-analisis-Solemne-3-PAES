import gdown,os,zipfile,shutil, pathlib

# Obtener el directorio raíz del proyecto
ROOT = pathlib.Path(__file__).resolve().parent.parent
# Ruta donde guardarás el archivo descargado
ROOT_API = ROOT / "api"
# Ruta donde se guardaran los csv
ROOT_DATASET = ROOT / "database"
# Ruta en donde se guardaran que no son csv
ROOT_OTHER = ROOT / "other"

# ID del archivo de Google Drive
file_id = '16_mpkujb2sXBAdEC2BV652lWDr7hjMsQ'

# URL para descargar el archivo
url = f'https://drive.google.com/uc?id={file_id}'

# Descargar el archivo
output_path = ROOT_API / "dataset.zip"
gdown.download(url, str(output_path), quiet=False)

# Extraer el archivo
with zipfile.ZipFile(output_path, 'r') as zip_ref:
    zip_ref.extractall(ROOT_API)

# Eliminar el archivo zip después de extraerlo
output_path.unlink()

# Retroalimentacion de la extraccion
print(f"Archivo descargado y extraído en: {ROOT_API}")


archivos = os.listdir(ROOT_API)
print(archivos)

# Mover los archivos que no son csv a la carpeta other
for archivo in archivos:
    if archivo.endswith('.csv'):
        shutil.move(ROOT_API / archivo, ROOT_DATASET / archivo)
    if archivo.endswith('.py'):
        print("Este es el archivo de python XDD")
    else:
        shutil.move(ROOT_API / archivo, ROOT_OTHER / archivo)