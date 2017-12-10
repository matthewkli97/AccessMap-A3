#%%
import geopandas as gpd
import matplotlib.pyplot as plt

fp = "/Users/matthewli/workspaces/CSE495/AccessMap-A3/data/map.geojson"

data = gpd.read_file(fp)

#%%
print(data.head())

#%%
print(type(data))

data.plot()
plt.show()

#%%
# print(data.dtypes)

df1 = data['geometry']
print(df1.head())

df1.loc[df1['geometry'].dtypes == 'Linestring']
