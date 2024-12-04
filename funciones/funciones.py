import random
import pygame
import sys
from os import system 
from funciones.constantes import *
system("cls")

class Cartas:
    '''
    Cada carta tiene un valor y un palo, que se combinan para identificarla de forma única.
    Esta clase también define cómo se muestra una carta al imprimirla.
    '''
    def __init__ (self, valor:str , palos:str)->None:
        '''
        Inicializa una carta con un valor y un palo.
        '''
        self.valor = valor
        self.palo = palos   

    def __repr__(self)->str:
        '''
         Representación textual de la carta.
         '''
        return f"{self.valor} de {self.palo}"   
    

def crear_mazo (valores:tuple, palos:tuple)->list: 
    '''
    Combina los valores y palos proporcionados para crear un mazo de cartas, 
    y luego lo mezcla de forma aleatoria.
    '''
    mazo_ordenado = [Cartas(valor, palo) for palo in palos for valor in valores]
    mazo = random.sample(mazo_ordenado, len(mazo_ordenado))
    return mazo

def repartir_cartas(mazo: list, num_jugadores: int = 2) -> set:
    '''
    La función distribuye un total de 3 cartas a cada jugador, extrayéndolas del 
    final del mazo proporcionado. Las cartas se eliminan del mazo original.
    '''

    manos = {f'Jugador {i+1}': [] for i in range(num_jugadores)}
    for i in range(3):  # Cada jugador recibe 3 cartas
        for jugador in manos:
            manos[jugador].append(mazo.pop())
    for jugador, cartas in manos.items():
        cartas_str = ', '.join([str(carta) for carta in cartas])  # Usar str() para objetos
        print(f'{jugador} tiene las siguientes cartas: {cartas_str}')
    return manos

def cargar_imagen_cartas(palos: list, valores: list, CARPETA_IMAGENES: str, imagenes: dict) -> dict:
    '''
    Para cada combinación de valor y palo, la función busca la imagen correspondiente
    en la carpeta indicada, y la carga en un diccionario.
    '''
    for palo in palos:
        for valor in valores:
            # Crear el nombre de la imagen que se espera en la carpeta
            nombre_imagen = f'{valor} de {palo}.jpg'
            # Construir la ruta completa de la imagen
            ruta_imagen = (fr"{CARPETA_IMAGENES}\{nombre_imagen}")

            try:
                # Intentar cargar la imagen
                imagenes[f"{valor} de {palo}"] = pygame.image.load(ruta_imagen)
            except pygame.error:
                print(f"Error al cargar la imagen: {ruta_imagen}")

    return imagenes

class Juego :
    '''
    Esta clase maneja la creación de jugadores, el reparto de cartas y la
    visualización de las cartas en la pantalla para cada jugador.
    '''
    def __init__(self, VALORES: tuple, PALOS: tuple, CARPETA_IMAGENES: str,imagenes:str)->None:
        '''
        Inicializa un nuevo juego.
        '''
        self.jugadores = ["jugador 1", "jugador 2"]
        self.cartas = repartir_cartas(crear_mazo(VALORES,PALOS))
        self.imagen = cargar_imagen_cartas(PALOS,VALORES,CARPETA_IMAGENES,imagenes)
        self.turno = 1
    
    def repartir_nuevas_cartas(self)->None:
        '''
        Reparte un nuevo conjunto de cartas al juego.
        '''
        self.cartas = repartir_cartas(crear_mazo(VALORES, PALOS))
    
    def mostrar_cartas(self, pantalla:any,rect_imagen:dict, jugador_index: int, x_pos: int = 450, y_pos: int = 450)->dict:
        '''
        Muestra las cartas de un jugador en la pantalla.
        '''
        # Asegurarse de acceder a las cartas del jugador
        jugador_cartas = self.cartas.get(f'Jugador {jugador_index + 1}', [])

        # Mostrar las cartas del jugador
        for j, carta in enumerate(jugador_cartas):
            carta_str = f'{carta.valor} de {carta.palo}'
            
            if carta_str in self.imagen:
                # Mostrar la carta en la pantalla en la posición adecuada
                imagen = self.imagen[carta_str]
                imagen_redimensionada = pygame.transform.scale(imagen, (100, 160))
                rect_carta = imagen_redimensionada.get_rect()
                rect_carta.topleft = (x_pos + j * 97, y_pos)
                pantalla.blit(imagen_redimensionada , (rect_carta.topleft))
                rect_imagenes[carta_str] = rect_carta
        return rect_imagenes
    

    def cartas_jugador_2(self, pantalla:any, contador: int, x_pos: int = 250, y_pos: int = 200)->str:

        '''
        Muestra las cartas del jugador 2 en la pantalla, basado en el contador.
        '''
        jugador_cartas = self.cartas.get(f'Jugador 2', [])

        cartas_jugadas = ""

        if contador >= 0:
            carta = jugador_cartas[0]
            carta_str = f'{carta.valor} de {carta.palo}'
            if carta_str in self.imagen:
                imagen = self.imagen[carta_str]
                imagen_redimensionada1 = pygame.transform.scale(imagen, (100, 160))
                pantalla.blit(imagen_redimensionada1, (250, 200))
                cartas_jugadas = carta_str

        if contador >= 1:
            carta = jugador_cartas[1]
            carta_str = f'{carta.valor} de {carta.palo}'
            if carta_str in self.imagen:
                imagen = self.imagen[carta_str]
                cartas_jugadas = carta_str
                imagen_redimensionada2 = pygame.transform.scale(imagen, (100, 160))
                pantalla.blit(imagen_redimensionada2, (550, 200))

        if contador >= 2:
            carta = jugador_cartas[2]
            carta_str = f'{carta.valor} de {carta.palo}'
            if carta_str in self.imagen:
                imagen = self.imagen[carta_str]
                cartas_jugadas = carta_str
                imagen_redimensionada3 = pygame.transform.scale(imagen, (100, 160))
                pantalla.blit(imagen_redimensionada3, (850, 200))

        return cartas_jugadas
    


    def dibujar_truco_envido_mazo(self, pantalla: any) -> None:
        '''
        Dibuja los botones de truco, envido y me voy al mazo
        '''
        botones = [
            (boton_truco, texto_truco),
            (boton_envido, texto_envido),
            (boton_mazo, texto_mazo)
        ]
        obtener_color_borde = lambda boton: TURQUESA if boton.collidepoint(pygame.mouse.get_pos()) else NEGRO

        for boton, texto in botones:
            marco_color = obtener_color_borde(boton)
            pygame.draw.rect(pantalla, marco_color, boton.inflate(10, 10), border_radius=5)
            pygame.draw.rect(pantalla, VERDE, boton)
            pantalla.blit(texto, (boton.x + 7, boton.y + 20))

        pygame.display.update()

    def dibujar_truco (self,pantalla:any)->None:
        '''
        dibuja todas las opciones del truco: truco,retruco,vale 4
        y tambien la opcion de volver al principal
        '''
        for boton in [boton_truco1, boton_truco2, boton_truco3,boton_volver]:
            mouse_pos = pygame.mouse.get_pos()
            if boton_truco1.collidepoint(mouse_pos):
                marco_color1 = TURQUESA
            else:
                marco_color1 = NEGRO

            if boton_truco2.collidepoint(mouse_pos):
                marco_color2 = TURQUESA
            else:
                marco_color2 = NEGRO

            if boton_truco3.collidepoint(mouse_pos):
                marco_color3 = TURQUESA
            else:
                marco_color3 = NEGRO
            if boton_volver.collidepoint(mouse_pos):
                marco_colorv = TURQUESA
            else:
                marco_colorv = NEGRO
            pygame.draw.rect(pantalla, marco_color1, boton_truco1.inflate(10, 10), border_radius=5)
            truco1 = pygame.draw.rect(pantalla,VERDE,boton_truco1)
            pygame.draw.rect(pantalla, marco_color2, boton_truco2.inflate(10, 10), border_radius=5)
            truco2 = pygame.draw.rect(pantalla,VERDE,boton_truco2)
            pygame.draw.rect(pantalla, marco_color3, boton_truco3.inflate(10, 10), border_radius=5)
            truco3 = pygame.draw.rect(pantalla,VERDE,boton_truco3)
            pygame.draw.rect(pantalla, marco_colorv, boton_volver.inflate(10, 10), border_radius=5)
            volver = pygame.draw.rect(pantalla,VERDE,boton_volver)
        pantalla.blit(texto_truco,(boton_truco1.x+10,boton_truco1.y+20))
        pantalla.blit(texto_truco2,(boton_truco2.x+5,boton_truco2.y+25))
        pantalla.blit(texto_truco3,(boton_truco3.x+5,boton_truco3.y+27))
        pantalla.blit(texto_volver,(boton_volver.x+7,boton_volver.y+20))
        pygame.display.update()
    
    def dibujar_envido (self,pantalla:any)->None:
        '''
        dibuja todas las opciones del envido: envido,real envido, falta envido
        y tambien la opcion de volver al principal
        '''
        for boton in [boton_envido1, boton_envido2, boton_envido3,boton_volver]:
            mouse_pos = pygame.mouse.get_pos()
            if boton_envido1.collidepoint(mouse_pos):
                marco_color1 = TURQUESA
            else:
                marco_color1 = NEGRO

            if boton_envido2.collidepoint(mouse_pos):
                marco_color2 = TURQUESA
            else:
                marco_color2 = NEGRO

            if boton_envido3.collidepoint(mouse_pos):
                marco_color3 = TURQUESA
            else:
                marco_color3 = NEGRO
            if boton_volver.collidepoint(mouse_pos):
                marco_colorv = TURQUESA
            else:
                marco_colorv = NEGRO
            pygame.draw.rect(pantalla, marco_color1, boton_envido1.inflate(10, 10), border_radius=5)
            envido1 = pygame.draw.rect(pantalla,VERDE,boton_envido1)
            pygame.draw.rect(pantalla, marco_color2, boton_envido2.inflate(10, 10), border_radius=5)
            envido2 = pygame.draw.rect(pantalla,VERDE,boton_envido2)
            pygame.draw.rect(pantalla, marco_color3, boton_envido3.inflate(10, 10), border_radius=5)
            envido3 = pygame.draw.rect(pantalla,VERDE,boton_envido3)
            pygame.draw.rect(pantalla, marco_colorv, boton_volver.inflate(10, 10), border_radius=5)
            volver = pygame.draw.rect(pantalla,VERDE,boton_volver)
        pantalla.blit(texto_envido,(boton_envido1.x+10,boton_envido1.y+20))
        pantalla.blit(texto_envido2,(boton_envido2.x+5,boton_envido2.y+27))
        pantalla.blit(texto_envido3,(boton_envido3.x+5,boton_envido3.y+27))
        pantalla.blit(texto_volver,(boton_volver.x+7,boton_volver.y+20))
        pygame.display.update()


#pantalla inicio
def pantalla_inicio (pantalla:any,puntos_maximos:int,ia:int)->None:
    '''
    Dibuja la pantalla de inicio del juego con los botones y textos.
    '''
    text_rect = titulo_texto.get_rect(center =(ANCHO_PANTALLA/2+370,ALTO_PANTALLA/2-150) ) 
    pantalla.blit(titulo_texto,text_rect)
    pygame.draw.rect(pantalla,GRIS,boton_jugar)
    pygame.draw.rect(pantalla,ROJO_OSCURO,boton_salir)
    pygame.draw.rect(pantalla,GRIS,boton_puntos)
    pygame.draw.rect(pantalla,GRIS,boton_ia)
    pantalla.blit(texto_jugar,(boton_jugar.x+25,boton_jugar.y+25))
    pantalla.blit(texto_salir,(boton_salir.x+25,boton_salir.y+25))
    if puntos_maximos == 15:
        pantalla.blit(texto_15, (boton_puntos.x + 25, boton_puntos.y + 35))
    elif puntos_maximos == 30:
        pantalla.blit(texto_30, (boton_puntos.x + 25, boton_puntos.y + 35))
    if ia == 1:  
        pantalla.blit(texto_ia_1,(boton_ia.x+30,boton_ia.y+25))
    elif ia == 2:
        pantalla.blit(texto_ia_2,(boton_ia.x+30,boton_ia.y+25))
    pygame.display.update()


    '''
    un boton de ranking
    paradigma funcional
    '''