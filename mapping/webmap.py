import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt", sep=",")
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red" 
    

html = """<h4>Volcano information:</h4>
Height: %s m
"""

map = folium.Map(location=[38.58,-99.09],zoom_start=6, tiles = 'Stamen Terrain')

fgv = folium.FeatureGroup(name = "Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], popup=html % str(el), 
    fill_color=color_producer(el), color="grey", radius=6, fill_opacity=0.7, fill=True))

style_function=lambda x: {"fillColor":"green" if x['properties']['POP2005'] < 10000000 
                            else "orange" if 10000000 <= x['properties']['POP2005'] < 20000000 else "red"}
fgp = folium.FeatureGroup(name = "Population")
fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),style_function=style_function))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())


map.save("Map1.html")



