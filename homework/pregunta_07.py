"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """

    lista = list()

    with open('files/input/data.csv', 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            subLista = list(linea.strip().split('\t'))
            lista.append((int(subLista[1]), subLista[0]))

    lista_nums = set(x[0] for x in lista)    

    tuplas = list()
    for num in lista_nums:
        lista_letras = list()
        for tupla in lista:
            if tupla[0]==num:
                lista_letras.append(tupla[1])
    
        tuplas.append((num, lista_letras))

    tuplas.sort()  
    return tuplas