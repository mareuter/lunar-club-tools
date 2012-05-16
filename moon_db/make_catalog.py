#!/usr/bin/python

import shapefile
r = shapefile.Reader("MOON_nomenclature.shp")
#sr = r.shapeRecords()
#print sr[0].shape.points
#print sr[0].record

ofile = open("initial_cat.txt", "w+")
for sr in r.shapeRecords():
	vals = (str(0), sr.record[0], sr.record[7])
	ofile.write("\t".join(vals)+"\n")
	
ofile.close()


