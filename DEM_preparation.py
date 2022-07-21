#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 09:00:18 2022

@author: cgotelli
"""


import functions as f


src  = open('/mnt/data2/20220719/halle_water_20220719-01_20220719T1546_dsm.tif')
orto = open('/mnt/data2/20220719/orto_grande.tif')
data = f.resample_raster(src)
ortoscaled = f.resample_orto(orto)

