#%%
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import sys
import argparse
import overpass


#filename = sys.argv[-1]

# observations = gpd.read_file(filename);

# Read in file via command line

#%%
observations = gpd.read_file('./data/SidewalkObservations/SidewalkObservations.shp')



#%%
sidewalks = gpd.read_file('./data/map.geojson')


api = overpass.API()
response = api.Get('node["name"="Salt Lake City"]')

#%% 
print(response)

#%%
map_query = overpass.MapQuery(50.746,7.154,50.748,7.157)
response = api.Get(map_query)

# print(sidewalks)

# #%%
# lines = sidewalks[sidewalks.geometry.type == 'LineString']
# lines.plot()

# #%%
# print(observations)