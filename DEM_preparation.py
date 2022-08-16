#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 09:00:18 2022

@author: cgotelli
"""

import functions as f


# -------------- Files' paths ---------------
ortoPath = "/mnt/data2/TEST/ortophotos/" 		# Path where ortophotos are stored
rasterPath = "/mnt/data2/TEST/rasters/"	# Path where rasters are stored

# ---------- Scaling parameters -------------
lengthScale = 40								# Length scale for transforming from experiment size to prototype size
resolutionScale = 1 / 2							# Resolution scale for changing number of pixels keeping the total length of the Raster/Ortophoto

# --------------- Booleans ------------------
processRaster = True							# True if want to scale Rasters
filterRasters = True						    # True if want to filter Rasters

processOrtophoto = True						    # True if want to scale Ortophotos

# ==================================================================================================
# -------------------------- DO NOT MODIFY FROM THIS POINT DOWN ------------------------------------
# -------------------------------------- Process ---------------------------------------------------

if processOrtophoto:
    f.scaleOrto(ortoPath, lengthScale, resolutionScale)
if processRaster:
    f.scaleRaster(rasterPath, lengthScale, resolutionScale, filterRasters)
    