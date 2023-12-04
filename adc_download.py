import cubo
import datetime
import pathlib
import numpy as np
import json
'''
Descripción de adc_download:
    Este paquete permite descargar imágenes satelitales utilizando la API de descarga de Planetary Computer,
    luego los apila con STAC stack y los guarda en un cubo de datos.
    La diferencia entre este paquete y y cubo.create es que lo guarda de forma estructurada en carpetas separado
    por id, sensores (de cada plataforma), data y metadata, etc. Además, permite descargar imágenes de varios sensores a la vez.    
    La estructura es la siguiente:
    - id
        - sensor1 (MSS)
            - data
                -.npy
            - metadata
                -.json
        - sensor2 (TM)
            - data
                -.npy
            - metadata
                -.json
        ...
        - sensorN (OLI)
            - data
                -.npy
            - metadata
                -.json
    Args:
        id (str): Identificador del cubo.
        lat (float): Latitud central del cubo.
        lon (float): Longitud central del cubo.
        collection (str): Lista de colecciones a descargar. Por defecto ["modis", "landsat", "sentinel-2"]
        bands (list): Bandas a descargar.
        start_date (str): Fecha de inicio del cubo.
        end_date (str): Fecha de fin del cubo.
        edge_size (int): Tamaño del borde del cubo (px).
        resolution (int): Tamaño del pixel del cubo (m).
        chunk (int): Periodo de tiempo para la descarga de las imágenes.
Principales dificultades:
    - El chunk debe ser dinámico, es decir, que para un periodo dado se debe descargar un numero igual de imágenes.
    - Si el token de PC caduca, se debe iniciar desde donde se detuvo la descarga.
'''

### Estructura ------------
def adc_download(
    id: str,
    lat: float,
    lon: float,
    collection: list = ["modis-43A4-061", "landsat-c2-l2", "sentinel-2-l2a"],
    bands: list = None,
    start_date: str = "2021-04-01",
    end_date: str = "2021-06-10",
    edge_size: int = 512,
    resolution: int = 500,
    chunk: str = "auto"
    ):
    return None
### -----------------------

### Prueba con un collection ---------------------------------------
collection_dict = {"modis-43A4-061": ["Nadir_Reflectance_Band4","Nadir_Reflectance_Band3","Nadir_Reflectance_Band2",
                                      "BRDF_Albedo_Band_Mandatory_Quality_Band1"],
                   "landsat-c2-l2": ["red","green","blue","cloud_qa"],
                   "sentinel-2-l2a": ["B02","B03","B04","SCL"]
                   }
### ----------------------------------------------------------------

# Convertir el valor de tiempo a un objeto datetime ----------------
def get_time_value(time_value):
# Convertir el valor de tiempo a un objeto datetime
    # Dividimos por 1e9 para convertir nanosegundos a segundos
    date_time = datetime.datetime.utcfromtimestamp(time_value / 1e9)  
    return date_time.strftime('%Y-%m-%d %H:%M:%S')
# ------------------------------------------------------------------

# Crear el cubo de datos ------------------------------------------
# Convert items to dictionary
# Create a dictionary to store all the data
path = "./adc_download"
id = "test"

# Create the folder structure
(pathlib.Path(path)/id).mkdir(parents=True, exist_ok=True)

# Download the data (as .npy) and metadata (as .json) for each collection
for key in collection_dict.keys():
    dc = cubo.create(
        lat=4.31,  # Central latitude of the cube
        lon=-76.2,  # Central longitude of the cube
        collection=key,  # Name of the STAC collection
        bands=collection_dict[key],  # Bands to retrieve
        start_date="2021-04-01",  # Start date of the cube
        end_date="2021-06-10",  # End date of the cube
        edge_size=4,  # Edge size of the cube (px)
    )
    
    # Convert items to a dictionary
    meta_dict = {}
    
    # Convert xarray.DataArrayCoordinates to a dictionary
    for meta_name, meta_data in dc.coords.items():
        meta_dict[meta_name] = meta_data.values.tolist()
    
    # Change the time values to a dictionary of datetime
    meta_dict['time'] = [get_time_value(time_val) for time_val in meta_dict['time']]

    # Get the data in a numpy array
    array = dc.to_numpy()

    for sensor in meta_dict['instruments']:
        sensor = '_'.join(sensor)

    # Create a subfolder for each sensor
    subfolder = (pathlib.Path(path)/id/sensor)
    subfolder.mkdir(parents=True, exist_ok=True)

    # Save the data in a numpy array
    np.save(subfolder/"test.npy", array)
    # Save the metadata in a json file
    with open(subfolder/"test.json", 'w') as f:
        json.dump(meta_dict, f) ## Se guarda todo el diccionario, y no los que representan al sensor

### ------------------------















