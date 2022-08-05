#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 09:00:18 2022

@author: cgotelli
"""

import functions as f


# -------------- Files' paths ---------------
ortoPath = "/mnt/data2/IBER/Ortophotos/"
rasterPath = "/mnt/data2/Metashape-outputs/"

# ---------- Scaling parameters -------------
lengthScale = 40
resolutionScale = 1 / 2

# --------------- Booleans ------------------
RasterScale = True
OrtophotoScale = False

# ---------------- Process ------------------
if OrtophotoScale:
    f.scaleOrto(ortoPath, lengthScale, resolutionScale)
if RasterScale:
    f.scaleRaster(rasterPath, lengthScale, resolutionScale)
