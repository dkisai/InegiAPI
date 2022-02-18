import json
import requests
import pandas as pd
import folium
from folium import plugins

# url con token
# Ejemplo: todos los bares en celaya en un radio de 5km del centro
token = "token"
rango = "5000"
latit = "20.522188"
longi = "-100.814037"
url = "https://www.inegi.org.mx/app/api/denue/v1/consulta/Buscar/bar/"+latit+","+longi+"/"+rango+"/"+token
# Respuesta de la consulta a la API
respuesta = requests.get(url)
respuesta = respuesta.text
data = json.loads(respuesta)
df = pd.DataFrame(data)
#Seleccionamos solo la latitud y longitud
df = df[["Latitud", "Longitud"]]
#Convertimos nuestra df a un array
df = df.values
#Mapa en Folium
mapa = folium.Map(
    location = [latit,longi],
    titles = 'OpenStreetMap',
    zoom_start=13
)
#Heatmap
mapa.add_child(plugins.HeatMap(df, radius=20))
mapa.save("mapa.html")