#!/usr/bin/env python

#   nutrient 	    metadata elements for each nutrient included in the food report
# 	nutrient_id 	nutrient number (nutrient_no) for the nutrient
# 	name 	        nutrient name
# 	sourcecode	    list of source id's in the sources list referenced for this nutrient
# 	unit	        unit of measure for this nutrient
# 	value	        100 g equivalent value of the nutrient
# 	dp	            # of data points
# 	se	            standard error
# 	derivation	    Indicator of how the value was derived

class nutrient:
    nutrient = ''
    nutrient_id = 0
    name = ''
    sourcecode = ''
    unit = ''
    value = 0
    dataPoints = 0
    standardError = 0
    derivation = ''