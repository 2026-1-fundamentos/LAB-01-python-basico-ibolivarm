"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    lista = list()

    with open('files/input/data.csv', 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            subLista = list(linea.strip().split('\t'))
            diccionarios = subLista[4].split(",")
            suma = 0
            for dic in diccionarios:
                suma += int(dic[4:])
            lista.append((subLista[0], suma))

    lista_letras = list(set(x[0] for x in lista))
    lista_letras.sort()

    tuplas = dict()
    for letra in lista_letras:
        suma = 0
        for tupla in lista:
            if tupla[0]==letra:
                suma += tupla[1]
    

        tuplas[letra] =  suma
 
    return tuplas
