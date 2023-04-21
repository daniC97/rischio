import xarray import as xr
ds = xr.open_dataset("tg_ens_mean_0.25deg_reg_2011-2022_v27.0e.nc")
ds.to_dataframe().to_csv("output_filename.csv")