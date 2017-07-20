# -*- coding: utf-8 -*-


import requests
import json
import time
import datetime
import pandas as pd

# parameters
origin = 'SAN'
destination = 'OGG'
departure_date = '2018-01-13'
return_date = '2018-01-21'


data = {
  "request": {
    "passengers": {
      "adultCount": 2
    },
    "slice": [
      {
        "origin": origin,
        "destination": destination,
        "date": departure_date,
      },
      {
        "origin": destination,
        "destination": origin,
        "date": return_date,
      }
    ]
  }
}

headers = {'Content-Type': 'application/json'}
url = "https://www.googleapis.com/qpxExpress/v1/trips/search"
api_key = open("C:\\Users\charles.wiles\Desktop\Google Air API.txt", 'r').read().rstrip()
url = url + '?key=' + api_key

r = requests.post(url, headers=headers, data=json.dumps(data))
response = r.json()

ts = int(time.time())


results = {}
for index, item in enumerate(response['trips']['tripOption'], start=0):
    thisResult = results[index] = {}
    thisResult['saleTotal'] = item['saleTotal']
    for item in item['slice']:
            for index, item in enumerate(item['segment'], start=0):
                thisResult[index] = {}
                thisResult[index]['carrier'] = item['flight']['carrier']
                thisResult[index]['flightNumber'] = item['flight']['number']
results['timestamp'] = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")

flights = pd.DataFrame.from_dict(results)

flights.to_csv('C:\\Users\charles.wiles\Desktop\Hawaii Flights.csv')
   
