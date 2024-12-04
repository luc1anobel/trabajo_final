import pygame
pygame.init()

#colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
MORADO = (87,35,100)
GRIS = (68,68,68)
ROJO_OSCURO = (160,49,58)
TURQUESA = (0,247,255)
VERDE = (0,76,69)

#tamaños de algo
ANCHO_PANTALLA = 1200
ALTO_PANTALLA = 700
ANCHO_CARTAS = 200
ALTO_CARTAS = 100

#tuplas y diccionario
DESTINO = (600, 100)
posiciones_cartas = {}
imagenes = {}
PALOS = ('Espada', 'Basto', 'Oro', 'Copa')
VALORES = ('1', '2', '3', '4', '5', '6', '7', '10', '11', '12')
CARPETA_IMAGENES = r"C:\Users\luciano\Desktop\proyectos\pygame\truco\cartas"
estado_botones = "principal"
archivo_ranking = r'C:\Users\luciano\Desktop\proyectos\pygame\truco\aa\codigo principal\funciones\ranking.txt'
ganador = ""
rect_imagenes = {}
posiciones_cartas_original = {}

#valores
equipo_ganador = 0
puntos = 0
puntos_equipo_1 = 0
puntos_equipo_2 = 0
estado_truco = 0
puntos_maximos = 15
jugador_index = 0
aparicion_carta = 0
velocidad_movimiento = 10  
contador = 0
ia = 1
turno_jugador = 1
contador_cartas = 0
indicador = 0
ronda_ganada_ia = 0
ronda_ganada_jugador = 0

#true o false
re_truco_cantado = False
truco_cantado = False
x = True
juego1 = True
moviendose = False  
bandera_inicial= True
mostrar_inicio = True
imprimir_botones = True
inicio_de_ronda = True
envido_tocado = False
truco_tocado = False
bandera_1 = True
ganador_cartas= None


#listas
estado_envido = [] 
llego_carta_jugador_1 = [False, False, False]
lista = []
cartas_seleccionadas = []
cartas_moviendose = []
carta_seleccionadas = []

#fuentes
fuente_inicio = pygame.font.Font(None, 70)
fuente_textos_50 = pygame.font.Font(None, 50)
fuente_textos_40 = pygame.font.Font(None,40)
fuente_textos_30 = pygame.font.Font(None,30)
fuente_textos_25= pygame.font.Font(None,25)
fuente_titulo = pygame.font.Font(None, 120)
fuente_36 = pygame.font.SysFont("Arial", 30)

                        #textos
#puntos
text_puntos = fuente_textos_30.render(f"Puntos Equipo 1: {puntos_equipo_1} | Puntos Equipo 2: {puntos_equipo_2}", True, NEGRO)
#titulo
titulo_texto = fuente_titulo.render("TRUCO", True,NEGRO)
#jugar
texto_jugar = fuente_inicio.render("jugar", True,BLANCO)
#ia
texto_ia_1 = fuente_inicio.render("IA 1", True, BLANCO)
texto_ia_2 = fuente_inicio.render("IA 2", True, BLANCO)
#salir
texto_salir = fuente_inicio.render("salir", True,BLANCO)
#puntos
texto_15 = fuente_textos_30.render("se jugara a 15 puntos", True, BLANCO)
texto_30 = fuente_textos_30.render("se jugara a 30 puntos", True, BLANCO)
#truco
texto_truco = fuente_textos_50.render("TRUCO", True,NEGRO)
texto_truco2 = fuente_textos_40.render("RETRUCO", True,NEGRO)
texto_truco3 = fuente_textos_30.render("VALE CUATRO", True,NEGRO)
#envido
texto_envido = fuente_textos_50.render("ENVIDO", True,NEGRO)
texto_envido2 = fuente_textos_30.render("REAL ENVIDO", True,NEGRO)
texto_envido3 = fuente_textos_30.render("FALTA ENVIDO", True,NEGRO)
#mazo
texto_mazo = fuente_textos_25.render("ME VOY AL MAZO", True,NEGRO)
#volver
texto_volver = fuente_textos_50.render("VOLVER", True,NEGRO)


#botones
boton_jugar = pygame.Rect(ANCHO_PANTALLA/2 + 250,
                          ALTO_PANTALLA/2-100 , 250, 90)
boton_salir = pygame.Rect(ANCHO_PANTALLA/2 + 250,
                          ALTO_PANTALLA/2+200 , 250, 90)
boton_puntos = pygame.Rect(ANCHO_PANTALLA/2 + 250,
                          ALTO_PANTALLA/2 , 250, 90)
boton_ia = pygame.Rect(ANCHO_PANTALLA/2 + 250,
                          ALTO_PANTALLA/2+100 , 250, 90)
#truco
boton_truco1 = pygame.Rect(ANCHO_PANTALLA/2 - 320, ALTO_PANTALLA/2 + 270 , 150, 70)
boton_truco2 = pygame.Rect(ANCHO_PANTALLA/2- 160 , ALTO_PANTALLA/2 +270 , 150, 70)
boton_truco3 = pygame.Rect(ANCHO_PANTALLA/2 , ALTO_PANTALLA/2 + 270 , 150, 70)
boton_volver = pygame.Rect(ANCHO_PANTALLA/2 +160 , ALTO_PANTALLA/2 + 270 , 150, 70)
#envido
boton_envido1 = pygame.Rect(ANCHO_PANTALLA/2 - 320, ALTO_PANTALLA/2 + 270 , 150, 70)
boton_envido2 = pygame.Rect(ANCHO_PANTALLA/2- 160 , ALTO_PANTALLA/2 +270 , 150, 70)
boton_envido3 = pygame.Rect(ANCHO_PANTALLA/2 , ALTO_PANTALLA/2 + 270 , 150, 70)
boton_volver = pygame.Rect(ANCHO_PANTALLA/2 +160 , ALTO_PANTALLA/2 + 270 , 150, 70)

#principal
boton_truco = pygame.Rect(ANCHO_PANTALLA/2 - 235,
                          ALTO_PANTALLA/2 + 270 , 150, 70)
boton_envido = pygame.Rect(ANCHO_PANTALLA/2- 75 ,
                          ALTO_PANTALLA/2 +270 , 150, 70)
boton_mazo = pygame.Rect(ANCHO_PANTALLA/2 + 85 ,
                        ALTO_PANTALLA/2 + 270 , 150, 70)


#-----
carta_seleccionada = None
rect_seleccionado = None



#sonidos
me_voy_al_mazo = pygame.mixer.Sound(r"C:\Users\luciano\Desktop\proyectos\pygame\truco\cartas\me voy al mazo.mp3")
quiero = pygame.mixer.Sound(r"C:\Users\luciano\Desktop\proyectos\pygame\truco\cartas\quiero.mp3")
no_quiero = pygame.mixer.Sound(r"C:\Users\luciano\Desktop\proyectos\pygame\truco\cartas\no quiero.mp3")
truco = pygame.mixer.Sound(r"C:\Users\luciano\Desktop\proyectos\pygame\truco\cartas\truco.mp3")
re_truco = pygame.mixer.Sound(r"C:\Users\luciano\Desktop\proyectos\pygame\truco\cartas\re truco.mp3")
vale_4 = pygame.mixer.Sound(r"C:\Users\luciano\Desktop\proyectos\pygame\truco\cartas\vale 4.mp3")
envido = pygame.mixer.Sound(r"C:\Users\luciano\Desktop\proyectos\pygame\truco\cartas\envido.mp3")
real_envido = pygame.mixer.Sound(r"C:\Users\luciano\Desktop\proyectos\pygame\truco\cartas\real envido.mp3")
falta_envido = pygame.mixer.Sound(r"C:\Users\luciano\Desktop\proyectos\pygame\truco\cartas\falta envido.mp3")




CARTAS = [
    [14 , "1 de espada"],
    [13 , "1 de basto"],
    [12 , "7 de espada"],
    [11 , "7 de oro"] ,
    [10 , "3 de espada","3 de oro","3 de copa","3 de basto"],
    [9 , "2 de espada","2 de oro","2 de copa","2 de basto"],
    [8 , "1 de oro","1 de copa"],
    [7 ,"12 de espada","12 de oro","12 de copa","12 de basto"],
    [6 , "11 de espada","11 de oro","11 de copa","11 de basto"],
    [5, "10 de espada","10 de oro","10 de copa","10 de basto"],
    [4, "7 de copa","7 de basto"],
    [3, "6 de espada","6 de oro","6 de copa","6 de basto"],
    [2,"5 de espada","5 de oro","5 de copa","5 de basto"],
    [1,"4 de espada","4 de oro","4 de copa","4 de basto"]]
    
pygame.quit()