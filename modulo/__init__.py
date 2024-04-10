def top_scorer(diccionario): 
    goles_max=-1
    nombre_max=" "
    for name_, goals_ in diccionario.items():
        if (goals_['goals'] > goles_max):
            goles_max= goals_['goals']
            nombre_max= name_ 
    print (f"El goleador/a es {nombre_max}, la cantidad de goles es {goles_max}")
    return  nombre_max


def most_influential_player(diccionario):
    #calcular el promedio de cada jugador
    promedio = map(lambda jugador: (jugador["goals"] * 1.5 + jugador["goals_avoided"] * 1.25 + jugador["assists"]), diccionario.values())

    #paso los promedios a una lista
    promedio = list(promedio) 

    #busco el promedio maximo almacenado y guardo su indice
    indice_maximo = promedio.index(max(promedio)) 

    # con ese indice, busco el nombre del jugador en el diccionario original
    nombre_maximo = list(diccionario.keys())[indice_maximo]

    return f"El jugador/a más influyente es {nombre_maximo}"

def team_goals_average(goals):
    promedio= sum(goals)/ 25
    return (f"El promedio de goles por partido del equipo es {promedio}") 

def player_average(name_top_scorer,diccionario):
   goles_goleador=  diccionario[name_top_scorer]['goals']
   promedio= goles_goleador / 25
   print(f"El promedio de goles del goleador/a es {promedio}")