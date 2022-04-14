import pandas as pd
import numpy
import csv

with open('poligono_de_medellin.csv') as csvfile:
    archivo = pd.read_csv(csvfile, delimiter=";")
    print(archivo)