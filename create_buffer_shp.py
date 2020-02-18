# Geoffrey Hughes
# Earth and Space Lab
# Chapman University
# 2/4/2020

# This file takes existing shapefiles and creates a new shapefile which
# includes buffers. The user will input the radius of the buffer.

# pip install shapefile
import shapefile

# Read in the shapefile
sf = shapefile.Reader("points.shp")

# Get a list of all the shapes
shapes = sf.shapes()

# Get the number of shapes / attributes (should all be points)
num_points = len(shapes)

for point in num_points:
    if shapes[point].shapeTypeName == 'POINT':
        ['%.3f' % coord for coord in shape]






#>>> shape = shapes[3].points[7]
#>>> ['%.3f' % coord for coord in shape]
#['-122.471', '37.787']
