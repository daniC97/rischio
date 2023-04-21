#import matplotlib.pyplot as plt
#import numpy as np
import xarray as xr
import pandas as pd
import reverse_geocode as rg

import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)

ds = xr.open_dataset("tg_ens_mean_0.25deg_reg_2011-2022_v27.0e.nc")
df = ds.to_dataframe()
ds = ds.sel(time = slice("2020-01-01", "2022-12-31"))



print(ds.tg[0][0][0])
#print(subset.tg)