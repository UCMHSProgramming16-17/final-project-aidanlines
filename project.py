# import the module
import requests
import csv
import math
import bokeh

#create a file
csvfile = open('file.csv')
#create csv writer
csvwriter = csv.writer(csvfile, delimiter = ',')
#write info
csvwriter.writerow(['Date', 'Temperature'])
#import requests
import requests
import json

url = "https://maps.googlesapis.com/maps/api/geocode/json"
key = 'AIzaSyCn3211IW7eTGhTJMyzmo_Pg5DcU44y7Zk'

address = input("Enter an address")
payload = {'key':'', 'address': address}
#make a request
r = requests.get(url, params=payload)
#print r.url
#process the data given
data = r.json()
# print data
location = data['results'][0]

geometry = location['geometry']['location']
#print data
lat = str(geometry['lat'])
lon = str(geometry['lng']) 

#creating url for requests

endpoint = 'https://api.darksky.net/forecast/'
key1 = '6082702572cc4f7ca09810632e2ec8b8'
payload1 = {'units' : 'us'}
year = int(input("pick a year"))

for year in range(year-50, year):
    time = str(year) + "-04-30T12:00:00Z"
    
    #assemble the full url
    url1 = endpoint + key1 + '/' + lat + ',' + lon + ',' + time
    
    #make a request
    rl = requests.get(url1, params = payload1)
    #print(rl)
    
    #process/get info together and deal w/ it
    
    weather = rl.json()
    
    Temperature = weather['currently']['Temperature']
    csvwriter.writerow([year, Temperature])
    
#close writer
csvfile.close()

import bokeh

import pandas as pd

from bokeh.charts import Scatter, output_file, save

df = pd.read_csv('file.csv')

p = Scatter(df, x='Date', y='Temperature', color='red', title="Date vs. Temperature", legend='top_right', xlabel="Date", ylabel="Temperature")

#p = Scatter(df, x='Date', y='Temperature', color='red', title="Date vs. Temperature", legend='top_right', xlabel="Date", ylabel="Temperature")

output_file('')

save(p)
