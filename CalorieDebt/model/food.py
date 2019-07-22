#!/usr/bin/env python


#   Food	metadata elements for the food being reported
# 	ndbno	NDB food number
# 	name	food name
# 	sd	    short description
# 	group 	food group
# 	sn	    scientific name
# 	cn 	    commercial name
# 	manu 	manufacturer
# 	nf	    nitrogen to protein conversion factor
# 	cf	    carbohydrate factor
# 	ff	    fat factor
# 	pf	    protein factor
# 	r	    refuse %
# 	rd	    refuse description
# 	ds	    database source: 'Branded Food Products' or 'Standard Reference'
# 	ru	    reporting unit: nutrient values are reported in this unit, usually gram (g) or milliliter (ml)

class food:

    ndbno = 0
    name = ''
    shortDesc = ''
    group = ''
    scienceName = ''
    commercialName = ''
    manufacturer = '',
    nitroFactor = ''
    carbFactor
