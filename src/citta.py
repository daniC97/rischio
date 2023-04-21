import reverse_geocode as rg
import csv

with open('temperature.csv', 'r') as temperature_r:
  temperature = csv.reader(temperature_r)
  temperature = list(temperature_r)[1:]

l = []
coordinate = []
q = []
for i in range(0,len(temperature)):
    temperature[i] = temperature[i].split(',')
    coordinate.append(temperature[i][:2])

citta = rg.search(coordinate)

for i in range(0,len(citta)):
    if citta[i]["country"] == 'Greece':
        if citta[i]["city"] not in q:
            print(citta[i]["country"],citta[i]["city"],temperature[i][2:])
            q.append(citta[i]["city"])