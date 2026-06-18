"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    lista = list()

    with open('files/input/data.csv', 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            subLista = list(linea.strip().split('\t'))
            diccionarios = subLista[4].split(",")
            for dic in diccionarios:
                lista.append((dic[0:3], int(dic[4:])))

    lista_dics = set(x[0] for x in lista)    

    tuplas = list()
    for dic in lista_dics:
        Max = None
        Min = None
        for tupla in lista:
            if tupla[0]==dic:
                if Min is None or tupla[1]<Min:
                    Min = tupla[1]
                if Max is None or tupla[1]>Max:
                    Max = tupla[1]
    
        tuplas.append((dic, Min, Max))

    tuplas.sort()  
    return tuplas