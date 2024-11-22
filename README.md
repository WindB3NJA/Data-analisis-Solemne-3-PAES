# Análisis de Datos 📊

Este repositorio contiene el análisis de datos del conjunto de **Puntajes PAES** registrados en 2024, adaptado para la evaluación **Solemne 3**. Los datos se procesan desde una base más pequeña generada a partir del archivo original, facilitando su análisis y visualización.

## Requisitos 🛠️

- **Python 3.6+**
- Librerías:
  - `streamlit`
  - `pandas`
  - `matplotlib`
  - `gdown` (para descargar los datos desde Google Drive)

## Sobre los datos 📂

Los datos originales provienen de una base del gobierno que contiene un volumen considerable de información sobre los puntajes PAES. Dado el tamaño del archivo original, se decidió delimitarlo y modificarlo a **100 filas** para hacer el análisis más manejable y comprensible.

- **Archivo Original:** Puedes acceder al archivo original de los datos PAES 2024 en este [enlace](https://datosabiertos.mineduc.cl/wp-content/uploads/2024/05/PAES-2024-Inscritos-Puntajes.rar).
- **Archivo en Google Drive:** El archivo procesado se encuentra disponible en [Google Drive](https://drive.google.com/open?id=16_mpkujb2sXBAdEC2BV652lWDr7hjMsQ&authuser=1).

La base de datos original fue replicada en un archivo de Google Drive, desde donde se descarga automáticamente utilizando una API implementada en este proyecto.

---

## Instalación 🔧

### 1. Clona este repositorio:
   ```bash
   git clone https://github.com/WindB3NJA/Solemne-3--Data-Analisis-.git
   ```
### 2. Instala las dependencias:
Asegúrate de tener pip actualizado y luego instala las dependencias con:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Descarga el archivo de datos:
La API descargará automáticamente la base de datos al directorio correcto cuando ejecutes el programa. Sin embargo, si necesitas descargarla manualmente, ejecuta el siguiente 
  ```bash
  python api_download.py
  ```

## Uso 🚀
Ejecuta la aplicación:
Para ejecutar la aplicación de análisis de datos y ver los gráficos interactivos, corre el siguiente comando:
  ```bash
  streamlit run main.py
  ```

## Gráficos 🎨

El proyecto incluye diversos gráficos que permiten explorar la distribución y comparación de los puntajes PAES de los estudiantes. Los usuarios pueden seleccionar entre las siguientes opciones de gráficos:

- **Competencia Matemática 1 vs. Competencia Lectora** (Gráfico de barras)
- **Prueba Historia y Ciencias Sociales vs. Prueba Ciencias** (Gráfico de líneas)
- **Relación entre Puntaje NEM y Máximo Puntaje de Competencia Lectora** (Gráfico de dispersión)
- **Comparación de Puntaje NEM por Modalidad Educacional** (Gráfico de caja)
- **Distribución de Estudiantes por Rama Educacional** (Gráfico de torta)
- **Distribución de Puntajes Promedio, NEM y Ranking** (Gráfico de histograma)

Cada gráfico proporciona una visualización única para entender mejor cómo se distribuyen y comparan los puntajes entre las distintas pruebas y modalidades educacionales.

## Contribuciones 🤝
¡Las contribuciones son bienvenidas! Por favor, abre un issue o un pull request para contribuir.
