import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt", sep=",")
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

def color_producer():
    return "green"

html = """<h4>Volcano information:</h4>
Height: %s m
"""

map = folium.Map(location=[38.58,-99.09],zoom_start=6, tiles = 'Stamen Terrain')

fg = folium.FeatureGroup(name = "My Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt,ln], popup=html % str(el), icon=folium.Icon(color=color_producer())))


map.add_child(fg)

map.save("Map1.html")



