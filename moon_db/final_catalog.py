#!/usr/bin/python

# This script will handle creating the actual catalog database for the 
# Lunar information

# Variables that get the fields from the shape file.
# Feature name without diacritical marks
CLEAN_NAME = 1
# Feature diameter
DIAMETER = 4
# Feature center longitude
CENTER_LONG = 5
# Feature center latitude
CENTER_LAT = 6
# Feature type
FEATURE_TYPE = 7
# Minimum and maximum longitude
MIN_LONG = 10
MAX_LONG = 11
# Minimum and maximum latitude
MIN_LAT = 12
MAX_LAT = 13
# Quadrant name and code
QUAD_NAME = 16
QUAD_CODE = 17
# Files for database creation
SHAPEFILE = "MOON_nomenclature.shp"
INITIAL_CAT = "initial_cat.txt"
OUTPUT_DB = "moon.db"
# Lunar club codes: 1 - Lunar, 2 - Lunar II, 3 - Both
LUNAR_CODES = (1, 2, 3)

# Get the required list of feature from the initial catalog
cat_file = open(INITIAL_CAT, "r")
feature_dict = {}
for line in cat_file:
    values = line.split('|')
    if int(values[0]) in LUNAR_CODES:
        feature_list[values[1]] = int(values[0])
cat_file.close()
