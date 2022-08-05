# DEM-Iber  
Preparation of the laboratory flume's Rasters and Ortophotos for being used with Iber for simulate the flow of water and sediment inside the experiment.  

The idea of the code is basically:  

1. To be able to use a Raster with less pixels than the original, but keeping the size. For that we use a bilinear resampling method.
2. To be able to scale up the dimensions from the experiment to a real prototype scale. By doing this, a flume of 10m length can represent a river of 10m times the chosen scale (e.g. for a scale of 40 the flume would represents a river of 400m length).

Normally, when you scale up the dimensions of a Raster keeping the pixel representative length (e.g., 1 pixel = 1 cm), you will have an image that will greatly increase the number of pixels after the scaling. This method produces images of huge resolutions and disk size, so we added the option of changing the length that 1 pixel represents. Combining both tools it is possible to scale up the dimensions of the flume and keep -or even reduce- the number of pixels.


### Explanation of the main code  

The main code to run is file ```DEM_preparation.py```. To use this file some parameters must be provided:

- **ortoPath**: Path of the folder where the ortophotos are stored,
- **rasterPath**: Path of the folder where the rasters are stored,
- **lengthScale**: Scale that will be used to scale the flume to a real size,
- **resolutionScale**: Scale to reduce or increase the length represented by one pixel,
- **processRaster**: Boolean to indicate whether you want to process Raster files or not,
- **processOrtophoto**: Boolean to indicate whether you want to process Ortophoto files or not,
- **filterRasters**: Boolean to indicate if you want to filter the noise in the Rasters.

More details about these parameters can be found in detail inside the code, in file ```functions.py```.

### Explanation of the filter function code  

If you wish to filter possible noise present in the Raster coming from Metashape, you can use the function ```rasterFilter.py```. To do it, you need to set the boolean **filterRasters** to *True*.  

## General worflow for run a simulation:  

1. Get the Raster and Ortophoto from Metashape,
2. Put them in different folders: Rasters and Ortophotos,
3. (Optional) Filter Raster to remove noisy pixels. Use file ```rasterFilter.py``` following the instructions given below,
4. Use file ```DEM_preparation.py``` for scaling up both Raster and Ortophoto. It needs both paths of the Raster and Ortophoto folders,
5. With QGis load the Ortophoto and *Project > Import/Export > Export Map to Image*. This process will save the Ortophoto as a PNG image with coordinates,
6. Open Iber and load the PNG-format Ortophoto as Background image,
7. After creating the mesh with the boundary and initial conditions, and the roughness coefficient, 
8. Use the Raster image as elevation data source in Iber to gove height to mesh nodes,
9. Run the simulation.
```
> :heavy_exclamation_mark: **Important** You can repeat steps 1 to 9 the process for the next couple Raster-Ortophoto without going through number 7. As conditions are the same for every scan, you can reuse the mesh and change only the height with the Raster as source of data elevation.
```

