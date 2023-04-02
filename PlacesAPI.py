#import libraries
import pandas as pd
import requests

# Get your own Google Places Key 
api_key = 'YOUR API KEY'

def get_place_id(address):
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    params = {
        "key": api_key,
        "input": address,
        "inputtype": "textquery",
        "fields": "place_id"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == "OK":
            return data['candidates'][0]['place_id']
    return None

def get_nearest_restaurant(lat, lng):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "key": api_key,
        "location": f"{lat},{lng}",
        "rankby": "distance",
        "type": "restaurant"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == "OK":
            return data['results'][0]['name']
    return None

# Read Data frame 
#df = pd.DataFrame({'address': ['1600 Amphitheatre Parkway, Mountain View, CA 94043', '1 Infinite Loop, Cupertino, CA 95014']})
df = pd.read_csv('data\Syracuse_Public_Art.csv') 

#Get the places ID 
df['place_id'] = df['Address'].apply(get_place_id)

#this code snippet illustrates how you can parse the Google Place API to get extra information 
df[['lat', 'lng']] = pd.DataFrame(df['place_id'].apply(lambda x: 
                                                       requests.get(f"https://maps.googleapis.com/maps/api/place/details/json?key={api_key}&place_id={x}").json().get('result', {}).get('geometry', {}).get('location', {})).tolist())

#Get the nearest restaurant - Use the current Latitude and Longitude provided by the contest 
df['restaurant'] = df.apply(lambda x: get_nearest_restaurant(x['Latitude'], x['Longitude']), axis=1)

#write the file into a CSV 
df.to_csv('updated_addresses.csv', index=False)