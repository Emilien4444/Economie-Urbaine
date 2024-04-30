import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import matplotlib.colors
import matplotlib.cm as cm

file = "prix_immo2022.xlsx"
geo = "sh_communes.shp"

df_pi_m = pd.read.excel(file, sheet_name="Ensemble des maisons", header = [0, 1])
df_pi_a = pd.read.excel(file, sheet_name="Ensemble des appartements", header = [0, 1])

df_pi = pd.merge(df_pi_m, df_pi_a, left_on="pxm2_median_cod111", right_on="pxm2_median_cod121", suffixes=("_maison", " _appartement"))
df_pi["pxm2_median_all"] = (df_pi[pxm2_median_cod111] + df_pi[pxm2_median_cod121])/2

geo_df = gpd.read_file(geo)

final_df = geo_df.merge(df_pi, left_on="INSEE_COM", right_on="codgeo") #?


fig, ax = plt.subplots(1, 1, figsize=(30, 15))
cmap = cm.veridis

commune = final_df.plot(column="pxm2_median_all", ax=ax, legend=false, linewidth=1, alpha=0.9, edgecolor='black')

plt.title("carte des prix médians de la moyenne entre prix par m2 pour appartement et maisons par communes de France.")
plt.show()

