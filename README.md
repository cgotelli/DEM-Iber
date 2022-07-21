# DEM-Iber
Preparation of the laboratory flume's Raster and Ortophoto for being used with Iber. 

General worflow for run a simulation:  

1. Get the Raster and Ortophoto from Metashape,
2. Put them in different folders: DEMs and Ortophotos,
3. Filter Raster to remove noisy pixels. Use file ```rasterFilter.py``` following the instructions given below,
4. Use file ```DEM_preparation.py``` for scaling up both Raster and Ortophoto. It needs both paths of the Raster and Ortophoto folders,
5. With QGis load the Ortophoto and *Project > Import/Export > Export Map to Image*. This process will save the Ortophoto as a PNG image with coordinates,
6. Open Iber and load the PNG-format Ortophoto as Background image,
7. After creating the mesh with the boundary and initial conditions, and the roughness coefficient, use the Raster image as elevation data source,
8. Run the simulation.


## Parameters of the function

The 
