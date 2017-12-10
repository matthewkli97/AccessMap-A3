CSE 495 - Group A3
Matthew Li
Katherine Choi
Alex Pan
Yuqi Huang
9 December 2017

# Project A3: Linking outside data with OpenStreetMap

## Abstract

The main goal of our project was to evaluate and implement a one way data transfer process for importing outside data sources into the OpenStreetMaps platform.

The broad scope of the project is to create a completely generalized way of importing outside data into OpenStreetMaps. Such a process would allow any form of data to be processed and analyzed to be imported into OpenStreetMaps. 

To start however, our group will narrow the scope and prototype with the Seattle Sidewalk Observation data set. From the SDOT data set, we will create an automated process of importing and maintaining the data in OpenStreetMaps. After this initial scope, we will attempt to do the same process with data from Project Sidewalks in order to generalize the process.

## Project Context/Background:

As part of the OpenSidewalks project, we have been slowly adding sidewalk data to OpenStreetMap, using the Seattle DOT’s Sidewalks dataset as a first approximation. The sidewalk inventory has recently been updated, which raises a question: how do we use the new data, and put some of the most-valuable information in OSM? And how do we handle this process in general going forward? A single sidewalk in the Seattle DOT’s dataset may be represented by several separate lines in OpenStreetMap, and vice versa. There is also a sister project, Project Sidewalk, which automates the gathering of data but we need to be able to stage that data and enter it into OSM.

This project would tackle both the specific challenge of updating Seattle’s OpenStreetMap sidewalk data, as well as the general issue of linking and resolving constantly-updating datasets (such as Project Sidewalk Washington DC inventory) with OpenStreetMap.

## Quarterly Objectives

### Learning the technologies.

A large part of our quarter was spent learning the technologies that would be required to solve our problem. Since this was our group’s first time working with geospatial data, we were required to learn the technologies from scratch. One of the first aspects of the project that we had to learn was the fundamentals of GIS. This step comprised of learning what exactly GIS is, how it is used, and how we can utilize our data to solve our problem. As a result of this primary step, we gained familiarity with how geographical data was stored (ie. points, linestrings, relations etc) and a foundation to build upon. 

Working from a better understanding of GIS fundamentals, our group then needed to learn the technologies to work with such data. Our first step was to decide what programming language would be suitable for achieving our goal. We chose python due to its expansive library collection and ability to experiment and prototype on the jupyter notebook platform. Choosing python, however, also had its disadvantages since none of our group members has worked with python or it’s syntax. As a result of this, a large portion of the quarter was spent getting our foundational knowledge and properly getting our machines installed with all the software. 

After learning some of the basics of python, our group then worked to learning the libraries that would be be helpful for solving the problem. These packages included: Geopandas, Pandas, libspatialindex, MatPlotLib, Json, Overpass API. 

Processing data from data.seattle.gov

With a new familiarity in GIS, the next step was to work towards achieving our main objective. Working with the Sidewalk Observations data set from data.seattle.gov we set out by doing simple data manipulation to gain a familiarity with our eventual prototype algorithm. Our first step in this process was to compare Seattle Sidewalk Observations data and data from OSM. During this step, we needed to learn how to process and manipulate Shapefile data as well as OSM data. Utilizing Geopandas, we were able to work and manipulate our data and create relations between the two sets. In addition, we were required to create geospatial relations which we achieved by utilizing libspatialindex. 

Our algorithm takes advantage of the spatial indexing of each of the data frames to make relations between the data. From the spatial indexing, we are able to make  


A large subsection of our quarter was spent learning new technologies and methods for working with geospatial data. 
(1)   Learn GeoPandas (eScience tutorials)
Introduction to SQL and Geospatial Data Processing
Visualization in Python
Vector Data Processing
(2)   Learn data manipulation in Python
(3)   Import data from SDOT
Convert into proper projections (WGS84)

Importing data from OSM, mapping the data from SDOT to OpenStreetMap
(1)   Design algorithm to compare SDOT data and OSM
Figure out best approximation of SDOT endpoints → OSM endpoints
Figure out how to identify differences in data points and calculate maximum error bounds
(2)   Design algorithms to mark the altered data points
Figure out how to label existing changed data
Figure out how to label new data
Determine output data format for front end to read

## How to Use
1) Install the following:
Install python
Install geopandas
Install matplotlib.pyplot
Install pandas
Install overpass
Install lxml
2) Supply the Sidewalk data
We designed the program specifically for point shape files.
3) Create a JSON mapping schema in this specified format:
Must use “categoryMap” for tags in sidewalk data that require a mapping from its type (see “LEVEL_DIFF” below)

4) Run this python script: python CrappySidewalks.py [*OUTSIDE-DATA] [**MAPPING] 
*OUTSIDE-DATA should be in the form of GeoJSON or Shapefile
**MAPPING should be in the form of JSON (see above)
Future Developments
Although we have a good start to linking outside data with OpenStreetMap, there are still a lot of things left to be done. One of our stretch goals was to create a completely generalized way to import outside data into OpenStreetMap. 
Updating/Editing already contained nodes
Implementing way inclusion? Put nodes in the way at the correct location/order
Front end implementation 
Let client choose the mapping format they want rather than use our format

## Conclusion
	In this project, we tackled both the challenges of importing sidewalk data and mapping data from shapefiles to OSM datasets for future updating. 
At the beginning, we took a lot of time to set up our machines and learn python, geopandas, and GIS. Matthew helped other three teammates a lot about setting everything up. Also, with the help of weekly meeting with instructors and various tutorials, we were able to make progress every week. Once we started doing prototyping, we met a bunch of other challenges. Since this is a real-world project, we have to deal with huge datasets. We discussed a lot about how to fetch data from OpenStreetMap and which is the most efficient way to find the closest sidewalk to a given node.
Now, if the users provide the sidewalk datasets (GeoJSON or Shapefile) and a JSON file with mapping schemas in a specific format, by running our Python script, they will get an OSM file with all the new nodes. Therefore, people can easily add these new nodes to OpenStreetMap.
In the future, we plan to find a generalized way to import outside data into OpenStreetMap, figure out how to edit/update the nodes that already exist and solve the issue of linking and resolving constantly-updating datasets.
In conclusion, this was a great learning experience. Professor Caspi and Nick are really nice, and they helped us a lot in our project. Our teammates always help each other and grow with each other. We are really thankful for this project, from which we learned a lot of skills and knowledge that academic study cannot provide. Meanwhile, we are also happy that we contributed a little to AccessMap development.


