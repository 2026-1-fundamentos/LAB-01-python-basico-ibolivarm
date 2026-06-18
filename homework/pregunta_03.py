"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

    lista = list()

    with open('files/input/data.csv', 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            subLista = list(linea.strip().split('\t'))
            lista.append((subLista[0], int(subLista[1])))

    lista_letras = set(x[0] for x in lista)    

    tuplas = list()
    for letra in lista_letras:
        suma = 0
        for tupla in lista:
            if tupla[0] == letra:
                suma += tupla[1]
        tuplas.append((letra, suma))

    tuplas.sort()  
    return tuplas
