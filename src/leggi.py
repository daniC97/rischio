import netCDF4 as nc
import pandas as pd
import reverse_geocode as rg
import numpy as np
import numpy.ma as ma

fn = 'tg_ens_mean_0.25deg_reg_2011-2022_v27.0e.nc'
ds = nc.Dataset(fn)


"""
print("\n------ VARIABILI --------\n")
for var in ds.variables.values():
    print(var)
"""

tg = ds.variables['tg']
latitude = ds.variables['latitude']
longitude = ds.variables['longitude']
time = ds.variables['time']

lat = latitude[:]
long = longitude[:] 
temp = tg[1]
k = len(lat)


#print(temp)
print(ma.getdata(latitude))
"""
coordinates = []

for i in range(0,k):
    c = (lat[i],long[i])
    coordinates.append(c) 

#citta = rg.search(coordinates)


#for i in range(0,len(citta)):
#    print(citta[i]["country"])

"""

