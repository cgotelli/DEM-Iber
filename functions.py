#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 14:27:02 2022

@author: cgotelli
"""

from rasterio import Affine, open
from rasterio.enums import Resampling
import numpy as np
from os.path import join
from os import listdir


def resample_raster(raster, name, lengthScale=40, resolutionScale=1 / 2):
    """
    Function that resamples a given raster after defining a new scale that will be applied to
    height and resolution.

    Parameters
    ----------
    raster : RASTER object from RASTERIO
        
    name : STRING
        Path with the name of the output ortophoto.
    lengthScale : FLOAT, optional
        DESCRIPTION. Length scale for converting distances fro laboratory size to real size. The default is 40.
    resolutionScale : FLOAT, optional
        DESCRIPTION. Resolution scale factor for reducing/increasing the number of pixels in the Raster. The default is 1 / 2 (50% less pixels per side).

    Returns
    -------
    None.

    """

    # Get the transformation parameters of the raster
    t = raster.transform

    # Rescale the metadata according to the length scale and the resolution scale.
    transform = Affine(
        t.a * lengthScale / resolutionScale,
        t.b,
        t.c,
        t.d,
        t.e * lengthScale / resolutionScale,
        t.f,
    )

    # New height and width for the output Raster
    height = int(raster.height * resolutionScale)
    width = int(raster.width * resolutionScale)

    # Update the profile of the raster with the new height and width.
    profile = raster.profile
    profile.update(transform=transform, driver="GTiff", height=height, width=width)

    # It reads the raster information (shape) and defines the resampling method to bilinear.
    data = raster.read(
        out_shape=(raster.count, height, width), resampling=Resampling.bilinear,
    )
    # Replaces all nodata values (-32767 in Metashape) for a given value
    data[data == -32767] = np.float32(0.2)

    # Now multiplies the altitude of each point by the height scale factor (40 by default)
    data = data * lengthScale

    # New file's name
    newFile = str(name[:-4] + "-ScaledResampled.tif")

    # Writes the new file with the new width, height and altitudes.
    with open(
        newFile,
        "w",
        driver=raster.driver,
        height=height,
        width=width,
        count=raster.count,
        crs=raster.crs,
        nodata=raster.nodata,
        transform=transform,
        dtype=np.float32,
    ) as dest_file:
        dest_file.write(data)
    dest_file.close()


def resample_orto(ortophoto, name, lengthScale=40, resolutionScale=1):
    """
    Function that resamples the ortophoto by a lenght and scale resolution factors.
    
    Parameters
    ----------
    ortophoto : TIFF ORTOPHOTO IMAGE
        DESCRIPTION.
    name : STRING.
        Path with the name of the output ortophoto.
    lengthScale : FLOAT, optional
        DESCRIPTION. Scale for rescaling the ortophoto to a real size river. The default is 40.
    resolutionScale : FLOAT, optional
        DESCRIPTION. Resolution scale for reducing/increasing the number of pixels. The default is 1.

    Returns
    -------
    None.

    """
    # Get the transformation parameters of the ortophoto
    t = ortophoto.transform

    # Rescale the metadata according to the length scale and the resolution scale.
    transform = Affine(
        t.a * lengthScale / resolutionScale,
        t.b,
        t.c,
        t.d,
        t.e * lengthScale / resolutionScale,
        t.f,
    )

    # New height and width for the output Raster
    height = int(ortophoto.height * resolutionScale)
    width = int(ortophoto.width * resolutionScale)

    # Update the profile of the raster with the new height and width.
    profile = ortophoto.profile
    profile.update(transform=transform, driver="GTiff", height=height, width=width)

    # It reads the raster information (shape) and defines the resampling method to bilinear.
    data = ortophoto.read(  # Note changed order of indexes, arrays are band, row, col order not row, col, band
        out_shape=(ortophoto.count, height, width), resampling=Resampling.bilinear,
    )

    # New file's name
    newFile = str(name[:-4] + "-scaled.tif")

    # Writes the new file with the new width and height.
    with open(
        newFile,
        "w",
        driver=ortophoto.driver,
        height=height,
        width=width,
        count=ortophoto.count,
        crs=ortophoto.crs,
        nodata=ortophoto.nodata,
        transform=transform,
        dtype=np.float32,
    ) as dest_file:
        dest_file.write(data)
    dest_file.close()


def scaleOrto(ortoPath, lengthScale, resolutionScale):
    """
    This function takes all the ortophotos inside a directory and applies the same function for rescaling the dimensions of each pixel.
    
    Parameters
    ----------
    rasterPath : String
        Folder where ortophotos are stored.

    Returns
    -------
    None.

    """

    ortoFiles = sorted(listdir(ortoPath))
    for file in ortoFiles:

        if file.endswith(".tif"):
            ortoName = join(ortoPath, file)
            ortoFile = open(ortoName)
            resample_orto(ortoFile, ortoName, lengthScale, resolutionScale)
            print(file)


def scaleRaster(rasterPath, lengthScale, resolutionScale, filterRasters):
    """
    This function takes all the rasters inside a directory and applies the same function for rescaling the dimensions of each pixel.

    Parameters
    ----------
    rasterPath : String
        Folder where rasters are stored.

    Returns
    -------
    None.

    """
    rasterFiles = sorted(listdir(rasterPath))

    for file in rasterFiles:

        if file.endswith(".tif"):
            rasterName = join(rasterPath, file)
            rasterFile = open(rasterName)
            if filterRasters:
                print("In the making")
                filterRaster() 
            resample_raster(rasterFile, rasterName, lengthScale, resolutionScale)
            print(file)


def filterRaster():
    """
    Function for filtering Raster files and remove sudden discontinuities 

    Returns
    -------
    None.

    """
    print('filtrando')

