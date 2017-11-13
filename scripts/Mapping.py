#%%
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

%matplotlib inline

#%%
observations = gpd.read_file('./data/SidewalkObservations/SidewalkObservations.shp')

#%%
sidewalks = gpd.read_file('./data/map.geojson')

print(sidewalks)

#%%
lines = sidewalks[sidewalks.geometry.type == 'LineString']
lines.plot()

#%%
print(observations)