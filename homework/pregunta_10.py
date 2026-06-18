"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """

    lista = list()

    with open('files/input/data.csv', 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            subLista = list(linea.strip().split('\t'))
            lista.append((subLista[0], len(subLista[3].split(",")), len(subLista[4].split(","))))

    return lista

print(pregunta_10())