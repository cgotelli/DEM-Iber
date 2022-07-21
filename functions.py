#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 14:27:02 2022

@author: cgotelli
"""

from rasterio.plot import show
from rasterio import Affine, open
from rasterio.enums import Resampling
import numpy as np


def resample_raster(raster, scaleHeight=40, scaleResolution = 1/2):
    t = raster.transform

    # rescale the metadata
    transform = Affine(t.a * scaleHeight/scaleResolution, t.b, t.c, t.d, t.e * scaleHeight/scaleResolution, t.f)
    height = int(raster.height * scaleResolution)
    width = int(raster.width * scaleResolution)

    profile = raster.profile
    profile.update(transform=transform, driver='GTiff', height=height, width=width)

    data = raster.read( # Note changed order of indexes, arrays are band, row, col order not row, col, band
            out_shape=(raster.count, height, width),
            resampling=Resampling.bilinear,
        )
    data[data == -32767] = np.float32(0.2)
    data = data*scaleHeight
    with open(
        r'/mnt/data2/20220719/halle_water_20220719-01_20220719T1546_dsm-rescaled.tif',
        'w',
        driver=raster.driver,
        height=height,
        width=width,
        count=raster.count,
        crs = raster.crs,
        nodata = raster.nodata,
        transform = transform,
        dtype = np.float32,
    ) as dest_file:
        dest_file.write(data)
    dest_file.close()
    
    return data

def resample_orto(raster, scaleHeight=40, scaleResolution = 1):
    t = raster.transform

    # rescale the metadata
    transform = Affine(t.a * scaleHeight/scaleResolution, t.b, t.c, t.d, t.e * scaleHeight/scaleResolution, t.f)
    height = int(raster.height * scaleResolution)
    width = int(raster.width * scaleResolution)

    profile = raster.profile
    profile.update(transform=transform, driver='GTiff', height=height, width=width)

    data = raster.read( # Note changed order of indexes, arrays are band, row, col order not row, col, band
            out_shape=(raster.count, height, width),
            resampling=Resampling.bilinear,
        )
        
    with open(
        r'/mnt/data2/20220719/halle_water_20220719-01_20220719T1546_dsm-rescaled-orto.tif',
        'w',
        driver=raster.driver,
        height=height,
        width=width,
        count=raster.count,
        crs = raster.crs,
        nodata = raster.nodata,
        transform = transform,
        dtype = np.float32,
    ) as dest_file:
        dest_file.write(data)
    dest_file.close()
    
 

    return data