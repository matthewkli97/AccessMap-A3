import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import sys
import argparse
import json
import overpass
import math
from lxml import etree
import xml.etree.ElementTree as ET
from shapely.geometry import Polygon

# Group A3 AccessMaps
# CrappySidewalks
# Script maps outside data source to OpenStreetMap
# sidewalks. Intended use is for person scouted data
# to be transfered into the OpenStreetMap database. 


# Arguments :

# 1 : Outside data file --> format = ShapeFile or GeoJson
# 2 : Mapping file --> format = JSON (must be in predefined format)
# 3 : (Optional) OSM data --> GeoJson, if not provided, data will be sourced from Overpass API

observations = gpd.read_file(sys.argv[1])
json1_file = open(sys.argv[2])
json1_str = json1_file.read()
mapping = json.loads(json1_str)


if len(sys.argv) > 3:
    OSM = gpd.read_file(sys.argv[3])
    sidewalks = OSM[OSM.geometry.type == 'LineString']


# Build bounding box around Observation data
bounds = observations.total_bounds
   
# Split box into managable sizes for Overpass API
maxX = 0.1
xChop = math.ceil((bounds[2] - bounds [0])/maxX)
maxY = .1
yChop = math.ceil((bounds[3] - bounds [1])/maxY)

xSize = ((bounds[2] - bounds [0]) / xChop)
ySize = ((bounds[3] - bounds [1]) / yChop)
api = overpass.API()

# Maximum distance tolerance between point and sidewalk to be added to
MAX_TOL = .003

pointDataFrame = gpd.GeoDataFrame()
ref = -1
f = open('UnMappedRows.txt','w')

for x in range(0, 1):
    for y in range(0, 4):    
        xmin = bounds[0] + (xSize * x)
        xmax = xmin + xSize
        ymin = bounds[1] + (ySize * y)
        ymax = ymin + ySize
        
        polygon = Polygon([(xmin, ymin), (xmin, ymax), (xmax, ymin), (xmax, ymax)])

        currentPoints = observations[observations.geometry.within(polygon)]

        if len(sys.argv) <= 3:
            map_query = overpass.MapQuery(ymin, xmin, ymax, xmax)
            query = 'way [highway=footway] ('+str(ymin)+','+str(xmin)+','+str(ymax)+','+str(xmax)+');<;>;'
            response = api.Get(query)
            OSM = gpd.GeoDataFrame.from_features(response)
        
        if(len(OSM.index) > 0):
            
            if len(sys.argv) <= 3:
                sidewalks = OSM[OSM.geometry.type == 'LineString']
            
            if(len(sidewalks.index) > 0):
        
                for index, row in currentPoints.iterrows(): 

                    point = row.geometry

                    mylist = [x.object for x in sidewalks.sindex.nearest(point.bounds, 10, objects=True)]
                    distances = sidewalks.loc[mylist].distance(point)

                    if distances.min() < MAX_TOL:
                        nearestIndex = distances.idxmin()
                        sidewalk_geom = sidewalks.loc[nearestIndex].geometry
                        distance_along = sidewalk_geom.project(point)
                        sidewalk_point = sidewalk_geom.interpolate(distance_along)

                        keys = row.keys()

                        mappingDict = {}

                        for key in keys:
                            if key in mapping:
                                if 'categoryMap' in mapping[key]:
                                    value = row[key]
                                    if value in mapping[key]["categoryMap"]:
                                        mappedValue = mapping[key]["categoryMap"][value]
                                        mappingDict[mapping[key]["target"]] = [mappedValue]
                                else:
                                    value = row[key]
                                    if len(value) > 0:
                                        mappingDict[mapping[key]["target"]] = [value]

                        if(len(mappingDict.keys()) > 0):
                            mappingDict['id'] = ref
                            mappingDict['geometry'] = [sidewalk_point]
                            ref = ref - 1

                            pdf = gpd.GeoDataFrame(mappingDict) 

                            pointDataFrame = gpd.GeoDataFrame(pd.concat([pointDataFrame, 
                                            gpd.GeoDataFrame(mappingDict)
                                            ], ignore_index=True))
                    else:
                        f.write(str(index) + "\n")
f.close()
                
root = etree.Element("osm")
root.attrib['generator']='CrappySidewalks'

boundsElement = etree.Element('bounds')
boundsElement.attrib['minlat'] = str(bounds[1])
boundsElement.attrib['minlon'] = str(bounds[0])
boundsElement.attrib['maxlat'] = str(bounds[3])
boundsElement.attrib['maxlon'] = str(bounds[2])
boundsElement.attrib['origin'] = "Overpass API"

root.append(boundsElement)

for index, row in pointDataFrame.iterrows(): 
    node = etree.Element("node")
    
    for colName in pointDataFrame.keys():
        if colName == 'id':
            node.attrib['id'] = str(row['id'])
        elif colName == 'geometry':
            node.attrib['lon'] = str(row['geometry'].x)
            node.attrib['lat'] = str(row['geometry'].y)
        else:
            tag = etree.Element("tag")
            tag.attrib['k'] = colName
            tag.attrib['v'] = str(row[colName])
            node.append(tag)
            
    root.append(node)
xmlString = etree.tostring(root, pretty_print=True)

et = etree.ElementTree(root)
et.write('output.osm', pretty_print=True)