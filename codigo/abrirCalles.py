import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from shapely import wkt
import networkx as nx

edges = pd.read_csv('calles_de_medellin_con_acoso.csv',sep=';')
edges['geometry'] = edges['geometry'].apply(wkt.loads)
tr = nx.from_pandas_edgelist(edges, source='origin', target='destination', edge_attr='length')
edges = gpd.GeoDataFrame(edges)

area = pd.read_csv('poligono_de_medellin.csv',sep=';')
area['geometry'] = area['geometry'].apply(wkt.loads)
area = gpd.GeoDataFrame(area)

fig, ax = plt.subplots(figsize=(12,8))

area.plot(ax=ax, facecolor='green')
edges.plot(ax=ax, linewidth=1, edgecolor='black')

plt.tight_layout()
plt.show()

origen = input('Ingrese la coordenada del origen >> ')
destino = input('Ingrese la coordenada del destino >> ')
djk_path = nx.dijkstra_path(tr, source=origen, target=destino, weight='length')
print(djk_path)