import phonenumbers
import opencage
import folium
from phonenumbers import geocoder

number =input("Enter your num:")

newnumber="+234-" + number
pnumber=phonenumbers.parse(newnumber)

print(pnumber)

location =geocoder.description_for_number(pnumber,"en")

print(location)

from phonenumbers import carrier

network=carrier.name_for_number(pnumber,"en")

print(network)

from phonenumbers import timezone

time=timezone.time_zones_for_number(pnumber)

print(time)

from opencage.geocoder import OpenCageGeocode
key ="4b3148dbec7c4f80a3d75f152ee4f132"

geocoder=OpenCageGeocode(key)
 
query =str(location)

results =geocoder.geocode(query)

print(results)

lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']

print(lat,lng)

# myMap=folium.Map(location=[lat,lng],zoom_start=20)

# folium.Marker([lat,lng],popup=location).add_to(myMap)

# myMap.save("mylocation.html")


