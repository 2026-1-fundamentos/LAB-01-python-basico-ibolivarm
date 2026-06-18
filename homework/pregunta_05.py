"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    lista = list()

    with open('files/input/data.csv', 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            subLista = list(linea.strip().split('\t'))
            lista.append((subLista[0], int(subLista[1])))

    lista_letras = set(x[0] for x in lista)    

    tuplas = list()
    for letra in lista_letras:
        Max = None
        Min = None
        for tupla in lista:
            if tupla[0]==letra:
                if Min is None or tupla[1]<Min:
                    Min = tupla[1]
                if Max is None or tupla[1]>Max:
                    Max = tupla[1]
    
        tuplas.append((letra, Max, Min))

    tuplas.sort()  
    return tuplas
