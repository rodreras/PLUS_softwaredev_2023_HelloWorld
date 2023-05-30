# Spacesense

## Geospatial Data Exploration Task for Remote Sensing Internship 2023

Task: Use a provided Sentinel-2 data cube with only raw bands, then post-process
a new layer of NDVI to achieve a map and time series visualization

- Materials:
    - netCDF of data cube 
    - Geojson of sub-AOI 

## Deliverables:

1. A Jupyter notebook from start to finish, opening, exploring, visualizing, and
modifying the geospatial data, specifically including the following:

    a. Calculation of the Normalized Difference Vegetation Index (NDVI)
over the entire AOI for each date given in the data cube and added as
a separate data layer in the same provided data cube

    b. A visual RGB image of one date

    c. Distribution (histogram) of NDVI pixels

    d. Time series of NDVI averaged over the AOI

2. A brief description of your interpretation of the spatial distribution and
evolution of the NDVI/vegetation

3. A visualization of NDVI (colormap here) clipped to the provided sub-AOI

## Additional instructions:

 1. Development is to be done using Python. Any frameworks/libraries are
accepted.

2. Any additional data exploration (i.e. not explicitly required for the
deliverables) can be kept in the notebook if displayed in a clean and
organized manner