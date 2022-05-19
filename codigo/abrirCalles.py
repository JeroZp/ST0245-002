import geopandas as gpd
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from shapely import wkt

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

def caminoMasCorto(graph, source, target, weight="length"):
    dijks_path = nx.dijkstra_path(graph, source=source, target=target, weight= "length")
    
    listaCamino = []
    for i in range(len(dijks_path) -2):
        listaCamino.append(dijks_path[i])

    listaDestinos = []
    for i in range(1, len(dijks_path) -1):
        listaDestinos.append(dijks_path[i])

    fig,ax = plt.subplots(figsize = (9,5))

    area.plot(ax=ax, facecolor= 'lightcyan')
    edges.plot(ax=ax, linewidth=1, edgecolor= 'black')
    longitud = 0
    for i in range(len(listaCamino)):
        distancia = edges[(edges['origin'] == listaCamino[i]) & (edges['destination'] == listaDestinos[i])]
        distancia.plot(ax = ax, linewidth=4, edgecolor= 'mediumvioletred')
        longitud+= float(distancia['length'].values)
    print("la longitud de la ruta es: ")
    print(longitud)
    plt.tight_layout()
    plt.show()
