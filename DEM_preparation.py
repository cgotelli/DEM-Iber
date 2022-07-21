#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 09:00:18 2022

@author: cgotelli
"""

import functions as f

ortoPath = "/mnt/data2/IBER/Ortophotos/"
rasterPath = "/mnt/data2/IBER/DEMs/"

f.scaleOrto(ortoPath)
f.scaleRaster(rasterPath)

