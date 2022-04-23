import pandas as pd
df = pd.read_csv("calles_de_medellin_con_acoso.csv", sep=';')
print(df)

def EvDistanciasEntreCalles(puntoA, puntoB):
    i = 2
    j = 2
    k = 2
    l = 2
    for name in df:
        if puntoA != name[i]:
            i = i+1
        else:
            puntoA = name[i]

        if puntoB != name[j]:
            j = j+1
        else:
            puntoA = name[j]      #Encontrar las calles definida por el usuario en el mapa de Medellín

        Ruta = list
        while k != puntoB:
            Ruta.append(name[k])  #Sumar calles a la ruta hasta llegar al punto B(No encontré manera de decirle a la ruta que la
            k+1                   #Calle va en dirección al punto B así que lo hice consecutivamente en las calles del mapa, es provicional)
        print(f"Su ruta es {Ruta}.")

        for length in df:
            distancia = 0
            while l != puntoB:
                distancia = length[k] + length[k+1]
        print(f"La distancia desde puntoA a punto B es: {Distancia}")

def main():
    puntoA = int(input)("Ingrese su punto de partida: ")
    puntoB = int(input("Ingrese su lugar de llegada: "))

    EvDistanciasEntreCalles(puntoA, puntoB)