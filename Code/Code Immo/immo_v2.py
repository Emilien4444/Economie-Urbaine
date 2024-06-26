import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import matplotlib.colors
import matplotlib.cm as cm
import numpy as np

#on importe les fichiers
file = r"C:\Users\ewena\Documents\Ecole\Economie\macro\projet\dv3f_prix_volumes_communes_2020_2022.xlsx"  
geo = r"C:\Users\ewena\Documents\Ecole\Economie\macro\projet\COMMUNE.shp" 

df_pi_m = pd.read_excel(file, sheet_name="Ensemble des maisons")
#print(df_pi_m['pxm2_median_cod111'])
df_pi_a = pd.read_excel(file, sheet_name="Ensemble des appartements") #, header = [0, 1] ? 
#print(df_pi_a['pxm2_median_cod121'])
df_pi = df_pi_m.merge(df_pi_a, left_on="codgeo", right_on="codgeo") #pb merge
#print(df_pi.head(5))

cdt_1 = np.isnan(df_pi["pxm2_median_cod111"])
cdt_2 = np.isnan(df_pi["pxm2_median_cod121"])
df_pi["pxm2_median_all"] = np.where(cdt_1, np.where(cdt_2, np.nan,df_pi["pxm2_median_cod121"]), np.where(cdt_2,df_pi["pxm2_median_cod111"], (df_pi["pxm2_median_cod121"]+df_pi["pxm2_median_cod111"])/2))
#print(df_pi['pxm2_median_all'])

geo_df = gpd.read_file(geo) #g #avec tout fichiers dans un meme dossier

df_f = geo_df.merge(df_pi, left_on="INSEE_COM", right_on="codgeo")

nan_count = df_pi["pxm2_median_all"].isna().sum()

nan_count

#affichage
fig, ax = plt.subplots(1, 1, figsize=(30, 15))
cmap = cm.viridis

vmin = df_f["pxm2_median_all"].min()
vmax = df_f["pxm2_median_all"].max()

com_map = df_f.plot(column="pxm2_median_all", ax=ax, legend=True, legend_kwds={'label': "prix median par m2 en France", 'orientation':"horizontal"}, linewidth=1, alpha=0.9, edgecolor="black", cmap=cmap, vmin=vmin, vmax=vmax)


plt.title("carte des prix médians de la moyenne entre prix par m2 pour appartement et maisons par communes de France.")
plt.show()


tl.figure(figsize(10, 6))
plt.bar(df_m["libgeo_x"].head(20), df_m["pxm2_median_all"].head(20))
plt.xlabel("Prix median du m2 pour maisons & appartements")
plt.ylabel("Prix median par m2 pour les 20 premières villes les plus chères")
plt.title("Prix mediand du m2 pour les 20 villes les plus chères")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
