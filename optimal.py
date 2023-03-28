import pandas as pd
from geopy.distance import distance

# define function to get nearest unvisited neighbor
def get_nearest_unvisited(curr_location, visited_locations, locations):
    min_distance = float("inf")
    nearest_neighbor = None
    for index, row in locations.iterrows():
        if row["Title"] not in visited_locations:
            dist = distance((curr_location["Latitude"], curr_location["Longitude"]), (row["Latitude"], row["Longitude"])).km
            if dist < min_distance:
                min_distance = dist
                nearest_neighbor = row
    return nearest_neighbor

# define function to get optimal route
def get_optimal_route(locations):
    visited_locations = []
    curr_location = locations.iloc[0]
    visited_locations.append(curr_location["Title"])
    order = [curr_location["Title"]]
    while len(visited_locations) < len(locations):
        nearest_neighbor = get_nearest_unvisited(curr_location, visited_locations, locations)
        visited_locations.append(nearest_neighbor["Title"])
        curr_location = nearest_neighbor
        order.append(curr_location["Title"])
    return order

# create sample dataframe with location names and coordinates
#df = pd.DataFrame({
#    "Name": ["New York, NY", "San Francisco, CA", "Austin, TX", "Miami, FL", "Seattle, WA"],
#    "latitude": [40.7128, 37.7749, 30.2672, 25.7617, 47.6062],
#    "longitude": [-74.0060, -122.4194, -97.7431, -80.1918, -122.3321]
#})
df = pd.read_csv('updated_addresses.csv') 

# get optimal route and add order column to dataframe
order = get_optimal_route(df[['Title', 'Latitude', 'Longitude']])
df['order'] = pd.Series(order)

# print dataframe with order column
df.to_csv('updated_addresses_optimized.csv')