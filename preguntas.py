"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.

"""
x = open("data.csv", "r").readlines()
x=[z.replace("\n","") for z in x]
x=[z.replace("\t"," ") for z in x]
x=[z.split(" ") for z in x]

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    lista=[int(z[1]) for z in x]
    resultado=sum(lista)
    
    return resultado


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    letras=['A','B','C','D','E']
    cantidad=[(letter,sum(1 for z in x if z[0]==letter)) for letter in letras]
      
    return cantidad


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    letras=['A','B','C','D','E']
    cantidad=[(letter,sum(int(z[1]) for z in x if z[0]==letter)) for letter in letras]
    
    return cantidad


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    from collections import Counter
    lista=[(z[2].split("-"))[1] for z in x]
    dicc=Counter(lista)
    result=[(key,value) for key, value in dicc.items()]
    result=sorted(result)
    
    return result


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    letras=['A','B','C','D','E']
    lista=[(letra,int(max(z[1] for z in x if z[0]==letra)),int(min(z[1] for z in x if z[0]==letra))) for letra in letras]
    return lista


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    
    codigos=['aaa','bbb','ccc','ddd','eee','fff','ggg','hhh','iii','jjj']

    lista=[    
        z[4].split(",")[i] for z in x for i in range(len(z[4].split(","))) 
    ]

    lista2=[
        (codigo,
         min(int(z.split(":")[1]) for z in lista if z.split(":")[0]==codigo),
         max(int(z.split(":")[1]) for z in lista if z.split(":")[0]==codigo))
         for codigo  in codigos
         ]
    
    return lista2


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    values=set(z[1] for z in x)
    lista=[(int(value),list(z[0] for z in x if z[1]==value)) for value in values]
    lista2=sorted(lista)
    
    return lista2


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    values=set(z[1] for z in x)
    lista=[(int(value),sorted(list(set(z[0] for z in x if z[1]==value)))) for value in values]
    lista2=sorted(lista)
    
    return lista2


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    codigos=['aaa','bbb','ccc','ddd','eee','fff','ggg','hhh','iii','jjj']

    lista=[    
        z[4].split(",")[i] for z in x for i in range(len(z[4].split(","))) 
    ]

    lista2={codigo:sum(1 for z in lista if z.split(":")[0]==codigo) for codigo  in codigos}
    
    return lista2


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    lista=[(z[0],len(z[3].split(",")),len(z[4].split(","))) for z in x]
    
    return lista


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    letras=set(z[3].split(",")[i] for z in x for i in range(len(z[3].split(","))))
    tuplas=[(z[3].split(",")[i],z[1]) for z in x for i in range(len(z[3].split(",")))]
    lista=[(letra,sum(int(tupla[1]) for tupla in tuplas if tupla[0]==letra)) for letra in letras]
    lista=sorted(lista)
    direc=dict(lista)
    
    return direc


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    letras=set(z[0].split(",")[i] for z in x for i in range(len(z[0].split(","))))
    tuplas=[(z[0],z[4].split(",")[i]) for z in x for i in range(len(z[4].split(",")))]
    lista1=[(tupla[0],tupla[1].split(":")[1]) for tupla in tuplas]
    lista2=[(letra,sum(int(tupla[1]) for tupla in lista1 if tupla[0]==letra)) for letra in letras]
    lista2=sorted(lista2)
    direc=dict(lista2)
    
    return direc
