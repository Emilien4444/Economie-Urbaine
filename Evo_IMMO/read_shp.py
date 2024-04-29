import geopandas as gpd
import matplotlib.pyplot as plt

# Read the shapefile into a GeoDataFrame
gdf = gpd.read_file("sh_communes.shp")

# Plot the GeoDataFrame
gdf.plot()
plt.show()