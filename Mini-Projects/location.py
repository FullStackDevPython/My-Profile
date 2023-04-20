import requests

API_KEY = 'your-key'
address = input('Please enter the address to find lattitude and longitude : ')

params = {
  'key': API_KEY,
  'address': address
}
base_url = "https://maps.googleapis.com/maps/api/geocode/json?"

response = requests.get(base_url, params=params).json()
if response['status'] == 'OK':
  geometry = response['results'][0]['geometry']
  lattitude = geometry['location']['lat']
  longitude = geometry['location']['lng']
  address_comp= response['results'][0]['formatted_address']
  print(f'The Lattitude and Longitude for the above address : "{address_comp}" is ({lattitude} , {longitude})')

# OUTPUT : On google maps this lat, long gives the exact location of the address given above
"""
OUTPUT :
Please enter the address to find lattitude and longitude : Sachin Layout Zingabai Takli Nagpur
The Lattitude and Longitude for the above address : "Sachin Layout, Nagpur, Maharashtra 440030, India" is (21.2014228 , 79.0714055)
"""

