import csv

Nombre_archivo = 'calles_de_medellin_con_acoso.csv'
with open(Nombre_archivo, newline='') as f:
    datos = csv.reader(f)

    Medellin = list(datos)

print(Medellin)