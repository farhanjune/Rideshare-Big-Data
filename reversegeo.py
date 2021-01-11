import urllib.request
import urllib.parse
import os
import csv
import json
import time
url = 'https://search.mapzen.com/v1/search?text='
csvfilew = open('enrichedLocations1.csv', 'w', newline='')
fieldnames = ['LATITUDE', 'LONGITUDE', 'ADDRESS','CITY','POSTALCODE','NEIGHBOURHOOD']
cwriter = csv.DictWriter(csvfilew, fieldnames=fieldnames)
cwriter.writeheader()
#cwriter.writerow(['STORE', 'ADDRESS', 'LATITUDE','LONGITUDE'])
with open('locations1.csv', newline='') as csvfile:
reader = csv.DictReader(csvfile)
for row in reader:
# url = 'https://search.mapzen.com/v1/search?text='+row['ADDRESS'].replace(',',',+').replace(' ','+')+'&key='+key+'&size=1'
url = 'https://api.geocode.earth/v1/reverse?api_key='+key+'&point.lat='+ row['lat']+'&point.lon='+ row['lon']+'&sources=osm&layers=address&size=1'
time.sleep(0.20)
try:
response = urllib.request.urlopen(url).read().decode('utf-8')
r = json.loads(response)
if r['features']:
name = r['features'][0]['properties']['name']
localadmin = r['features'][0]['properties']['localadmin']
postalcode = r['features'][0]['properties']['postalcode']
neighbourhood = r['features'][0]['properties']['neighbourhood']
latitude = r["features"][0]["geometry"]["coordinates"][1]
longitude = r["features"][0]["geometry"]["coordinates"][0]
cwriter.writerow({'LATITUDE':latitude,'LONGITUDE':longitude,'ADDRESS':name,'CITY':localadmin, 'POSTALCODE':postalcode,'NEIGHBOURHOOD':neighbourhood})
except urllib.error.HTTPError as e:
print (e.code)
print (e.read())
print (e.geturl())
