#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 09:00:18 2022

@author: cgotelli
"""

import functions as f


# -------------- Files' paths ---------------
ortoPath = "C:\\Users\\cleme\\Desktop\\Iber_Files\\Ortophotos\\" 		# Path where ortophotos are stored
rasterPath = "C:\\Users\\cleme\\Desktop\\Iber_Files\\Rasters\\"	# Path where rasters are stored

# ---------- Scaling parameters -------------
lengthScale = 40								# Length scale for transforming from experiment size to prototype size
resolutionScale = 1 / 2							# Resolution scale for changing number of pixels keeping the total length of the Raster/Ortophoto

# --------------- Booleans ------------------
processRaster = False							# True if want to scale Rasters
processOrtophoto = True						# True if want to scale Ortophotos
filterRasters = False							# True if want to filter Rasters


# ---- DO NOT MODIFY FROM THIS POINT DOWN ---
# ---------------- Process ------------------
if processOrtophoto:
    f.scaleOrto(ortoPath, lengthScale, resolutionScale)
if processRaster:
    f.scaleRaster(rasterPath, lengthScale, resolutionScale)
    if filterRasters:
    	print("In the making")
