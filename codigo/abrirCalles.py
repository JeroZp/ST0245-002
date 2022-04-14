import pandas as pd
import numpy
import csv

with open('calles_de_medellin_con_acoso.csv') as csvfile:
    archivo = pd.read_csv(csvfile, delimiter=";")
    print(archivo)