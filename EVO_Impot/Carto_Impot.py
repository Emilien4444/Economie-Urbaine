# Importe les biblios
import requests
import os
import zipfile
import json
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)
#import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
#plt.style.use('seaborn')


#telechargement données et mise en biblio fichier 2020-22
#biblio 2020_21
df_impot_2021= pd.read_excel("ircom_communes_complet_revenus_2020.xlsx", skiprows=7)

#supp doublons
df_impot_2021= df_impot_2021.drop_duplicates()

#filtre ligne où revenue fiscale = total 
df_total_impot_2021 = df_impot_2021[df_impot_2021["Unnamed: 4"] == "Total"]


# Charger le fichier shapefile des communes françaises
communes_shapefile = r"C:\Users\paul4\OneDrive\Bureau\PREING 2\S2\ECO URBAINE S4\PROJET\COMMUNE.shp"
communes_gdf = gpd.read_file(communes_shapefile)

communes_gdf


# Fusionner le dataframe (DF_total_impot_2021) des revenus fiscaux avec le GeoDataFrame des communes (communes_GDF)
total_impot_2021_gdf = communes_gdf.merge(df_total_impot_2021, how='inner', left_on='NOM', right_on='Unnamed: 3')

#t'as juste merge sur les noms des communes (NOM et Unnamed: 3 ) Manque l'application sur rev Fiscaux 
# Trier le GeoDataFrame par la colonne 'Unnamed: 7'
#total_impot_2021_sorted = total_impot_2021_gdf.sort_values(by='Unnamed': 7)

# Tracer le GeoDataFrame trié
#total_impot_2021_sorted.plot(column='NOM', legend=True)


#Afficher carte 
total_impot_2021_gdf.plot()
plt.show()
