import folium
from geopy.geocoders import Nominatim
import pandas as pd

import math

def calculate_angle(point1, point2):
    # Calculate angle between two points in degrees
    lat1, lon1 = point1
    lat2, lon2 = point2
    dLon = lon2 - lon1
    y = math.sin(dLon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dLon)
    brng = math.atan2(y, x)
    brng = math.degrees(brng)
    brng = (brng + 360) % 360
    return brng

# create map centered on Syracuse
syracuse_map = folium.Map(location=[43.0481, -76.1474], zoom_start=13)

# define dataframe with locations, nearby restaurants, and nearby art pieces
#df = pd.DataFrame({'Latitude': [43.050482, 43.052019, 43.046626, 43.042141],
#                   'Longitude': [-76.154533, -76.150847, -76.133434, -76.124616],
#                   'Restaurant': ["Empire Brewing Company", "Burger Joint", "Pastabilities", "Dinosaur Bar-B-Que"],
#                   'Art Piece': ["LeMoyne College Dolphin Statue", "Erie Canal Horse statue", "La Casita Mural", "Poster of historic Clinton Square"]})

df = pd.read_csv('updated_addresses_optimized.csv') 

# add markers and tooltips for each point in the route
prev_point = None
for i, row in df.iterrows():
    point = [row['Latitude'], row['Longitude']]
    tooltip_text = f"Nearby restaurant: {row['restaurant']} \n Nearby order: {row['order']}"
    marker = folium.Marker(point, icon=folium.Icon(icon='arrow-up', prefix='fa', color='red', icon_color='white'), popup=f'Point {i+1}', tooltip=tooltip_text)
    if prev_point:
        angle = calculate_angle(prev_point, point)
        marker.angle = angle
    marker.add_to(syracuse_map)
    prev_point = point

# create ordered lines with arrows connecting the points
locations = df[['Latitude', 'Longitude']].values.tolist()
for i in range(len(locations)-1):
    folium.PolyLine([locations[i], locations[i+1]], color='blue', weight=2.5, opacity=0.7, arrow_style='-|>', line_cap='round').add_to(syracuse_map)

# display the map
syracuse_map.save('syracuse_route.html')