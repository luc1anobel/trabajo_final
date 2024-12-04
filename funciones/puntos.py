from funciones.constantes import *
from os import system 
system("cls")

def puntos_truco(estado_actual:int)->int:
    '''
    Calcula los puntos correspondientes a una jugada de Truco según el estado actual.
    '''
    if estado_actual == 1:
        return 2
    elif estado_actual == 2:
        return 3
    elif estado_actual == 3:
        return 4 
    return 0


def cantar_envido(estado_actual:list, tipo:str)->list:
    '''
    Agrega un tipo de "Envido" a la lista de estado actual.
    '''
    estado_actual.append(tipo)
    return estado_actual

def puntos_envido(estado_actual:list,puntos_para_ganar:int):
    '''
    Calcula los puntos envido en función del estado actual del juego.

    '''
    for canto in estado_actual:
        if canto == "Envido":
            puntos += 2
        elif canto == "Real Envido":
            puntos += 3
        elif canto == "Falta Envido":
            return puntos_para_ganar
    return puntos

def actualizar_puntos(puntos_equipo_1:int, puntos_equipo_2:int, puntos:int,equipo_ganador:str )->tuple:
    '''
    Actualiza los puntos de los equipos según el ganador de la ronda.
    '''
    if equipo_ganador == "1":
        puntos_equipo_1 += puntos
        print("sume")
    else:
        puntos_equipo_2 += puntos
    pygame.display.flip()
    return puntos_equipo_1, puntos_equipo_2

def guardar_puntos_ronda(puntos_equipo_1:int, puntos_equipo_2:int, archivo:str=r"codigo principal\funciones\puntaje.txt"):
    '''
    Guarda los puntos de los equipos en el archivo de puntaje de la ronda.
    '''
    with open(archivo, "w") as file:
        file.write(f"persona: {puntos_equipo_1} // IA: {puntos_equipo_2}\n")

def leer_puntos_rondas(archivo:str=r"codigo principal\funciones\puntaje.txt"):
    '''
     Lee el archivo de puntaje de rondas y devuelve las líneas que contiene.
    '''
    try:
        with open(archivo, "r") as file:
            pygame.display.flip()
            return file.readlines()
    except FileNotFoundError:
        return []
    
    

def enlazar_los_valores (carta_jugador:str, carta_ia:str, CARTAS:list)->tuple:
    '''
    Asocia las cartas jugadas por el jugador y la IA con su valor correspondiente 
    a partir de la lista de cartas.
    '''

    for i in range(len(CARTAS)):
        for carta in CARTAS[i][1:]:
            if carta_jugador == carta:
                valor_jugador = CARTAS[i][0]
            elif carta_ia == carta:
                valor_ia = CARTAS[i][0]

    return valor_jugador,valor_ia




def calcular_mejor_carta (carta_juagador:int, carta_ia:int)->str:#paradigma funcional :es inmutable,tiene recursividad
    '''
    Calcula qué carta gana la ronda comparando las cartas del jugador y la IA.
    '''

    if carta_juagador == carta_ia:
        return "empate"
    elif carta_juagador > carta_ia:
        return "jugador"
    elif carta_juagador < carta_ia:
        return "ia"



def mostrar_texto(pantalla, archivo):
    try:
        with open(archivo, "r") as file:
            pygame.display.flip()
            return file.readlines()
    except FileNotFoundError:
        return []