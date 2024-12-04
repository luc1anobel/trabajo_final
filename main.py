import pygame
import time 
from os import system 
from funciones.funciones import *
from funciones.constantes import *
from funciones.puntos import *
system("cls")
pygame.init()

#inicializar la pantalla
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
#fondo de pantalla
fondo = pygame.image.load(r'C:\Users\luciano\Desktop\proyectos\pygame\truco\cartas\mesa.png')  # Asegúrate de tener la imagen en la ruta correcta
fondo = pygame.transform.scale(fondo, (1200, 700))  # Opcional: cambiar el tamaño del fondo si es necesario
fondo_menu = pygame.image.load(r'C:\Users\luciano\Desktop\proyectos\pygame\truco\cartas\fondo de menu.jpg') 
fondo_menu = pygame.transform.scale(fondo_menu, (1200, 700))
#cambiar el nombre de la ventana
pygame.display.set_caption("truco")

a = True
while a:
    if mostrar_inicio == True:
        pantalla.blit(fondo_menu,(0,0))
        pantalla_inicio(pantalla,puntos_maximos,ia)
        for i in range(2):
            texto = mostrar_texto(pantalla,archivo_ranking)
            y = 500
            for linea in texto:
                fuente_textos_70= pygame.font.Font(None,40)
                texto_a = fuente_textos_70.render(linea.strip(), True, BLANCO)
                pantalla.blit(texto_a, (50, y))
                y += 50
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                a = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.collidepoint(evento.pos):
                    mostrar_inicio = False
                elif boton_puntos.collidepoint(evento.pos):
                    if puntos_maximos == 15:
                        puntos_maximos = 30
                    elif puntos_maximos == 30:
                        puntos_maximos = 15
                elif boton_ia.collidepoint(evento.pos):
                    if ia == 1:
                        ia = 2  
                    elif ia == 2:
                        ia = 1
                elif boton_salir.collidepoint(evento.pos):
                    a = False
    else:
        puntos_para_ganar = puntos_maximos
        pantalla.blit(fondo, (0, 0))
        if inicio_de_ronda:
            partida = Juego(VALORES, PALOS, CARPETA_IMAGENES,imagenes)
            partida.mostrar_cartas(pantalla,rect_imagenes,jugador_index)
            inicio_de_ronda = False
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                a = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                for carta, rect in partida.mostrar_cartas(pantalla,rect_imagenes,jugador_index).items():
                    if rect.collidepoint(evento.pos):
                        carta_seleccionada = carta
                        rect_seleccionado = rect
                        print(f"Clic en la carta: {carta}")
                        if contador == 0:
                            destino = (200, 250)
                            contador += 1
                            indicador = 0
                        elif contador == 1:
                            destino = (500, 250)
                            contador += 1
                            indicador = 1
                        elif contador == 2:
                            destino = (800, 250)
                            indicador = 2
                        cartas_moviendose.append(carta)
                        moviendose = True
                mouse_pos = evento.pos
                #principal
                if estado_botones == "principal":
                    partida.dibujar_truco_envido_mazo

                    if boton_truco.collidepoint(mouse_pos):
                        estado_botones = "truco"
                        print("Truco seleccionado")

                    elif boton_envido.collidepoint(mouse_pos):
                        estado_botones = "envido"
                        print("Envido seleccionado")

                    elif boton_mazo.collidepoint(mouse_pos):
                        print("Me voy al mazo")
                        me_voy_al_mazo.play()
                #truco
                elif estado_botones == "truco":
                    partida.dibujar_truco

                    if truco_cantado == False:
                        if boton_truco1.collidepoint(mouse_pos):
                            print("Truco básico")
                            puntos_equipo_1 += 2
                            truco.play()
                            truco_cantado = True
                            puntos_equipo_1 += puntos_truco(1)

                    if truco_cantado:
                        if re_truco_cantado == False:
                            if boton_truco2.collidepoint(mouse_pos):
                                print("Retruco")
                                re_truco.play()
                                re_truco_cantado = True

                        if re_truco_cantado:
                            if boton_truco3.collidepoint(mouse_pos):
                                print("Vale Cuatro")
                                vale_4.play()

                            elif boton_volver.collidepoint(mouse_pos):
                                estado_botones = "principal"  
                                print("Volver a principal")

                    elif boton_volver.collidepoint(mouse_pos):
                        estado_botones = "principal"  
                        print("Volver a principal")

                #envido
                if estado_botones == "envido":
                    if x:
                        partida.dibujar_envido(pantalla)
                        x = False
                    else:
                        if boton_envido1.collidepoint(mouse_pos):
                            print("envido")
                            puntos_equipo_1 += puntos_truco(1)
                            envido.play()


                        elif boton_envido2.collidepoint(mouse_pos):
                            print("real envido")
                            real_envido.play()

                        elif boton_envido3.collidepoint(mouse_pos):
                            print("falta envido")
                            falta_envido.play()

                        elif boton_volver.collidepoint(mouse_pos):
                            estado_botones = "principal"  
                            print("Volver a principal")
                            x = True

        if moviendose and rect_seleccionado:
            dx = destino[0] - rect_seleccionado.x
            dy = destino[1] - rect_seleccionado.y

            if abs(dx) > velocidad_movimiento or abs(dy) > velocidad_movimiento:
                # Mover en pequeños pasos
                rect_seleccionado.x += velocidad_movimiento if dx > 0 else -velocidad_movimiento
                rect_seleccionado.y += velocidad_movimiento if dy > 0 else -velocidad_movimiento
            else:
                # Si la carta ha llegado al destino, detener el movimiento
                rect_seleccionado.topleft = destino
                moviendose = False
                posiciones_cartas[carta_seleccionada] = rect_seleccionado.copy()
                cartas_moviendose.remove(carta_seleccionada)
                llego_carta_jugador_1[indicador] = True



        pantalla.blit(fondo, (0, 0))

        # Mostrar las cartas del jugador 1 y las cartas en movimiento
        if bandera_inicial:
            cartas = partida.mostrar_cartas(pantalla,rect_imagenes,jugador_index)
            bandera_inicial = False

        for carta, rect in cartas.items():
            imagen = partida.imagen[carta]
            imagen_redimensionada = pygame.transform.scale(imagen, (100, 160))


            if carta in posiciones_cartas:
                rect = posiciones_cartas[carta]
            

            if carta == carta_seleccionada and moviendose:
                pantalla.blit(imagen_redimensionada, rect_seleccionado.topleft)

            elif carta not in cartas_moviendose:
                pantalla.blit(imagen_redimensionada, rect.topleft)
        
        for i in range(3):
            if llego_carta_jugador_1[i]:
                cartas_ia = partida.cartas_jugador_2(pantalla, i)
        

        if carta_seleccionada == None:
            pass
        else:
            if moviendose == True:
                pass
            else:
                carta_seleccionada = carta_seleccionada.lower()
                cartas_ia = cartas_ia.lower()
                carta_jugador,cartas_ia = enlazar_los_valores(carta_seleccionada,cartas_ia,CARTAS)
                ganador_cartas = calcular_mejor_carta(carta_jugador,cartas_ia)
                carta_seleccionada = None
    
        if ganador_cartas == "jugador":
            ronda_ganada_jugador += 1
            ganador_cartas = None
        elif ganador_cartas == "ia":
            ronda_ganada_ia += 1
            ganador_cartas = None
        elif ganador_cartas == "empate":
            ronda_ganada_jugador += 1
            ronda_ganada_ia += 1
            ganador_cartas = None
        if ronda_ganada_jugador == 2:
            print("el ganador es el jugador \n¡Fin del juego!")
            jugador = 1
            a = False
        elif ronda_ganada_ia == 2:
            print("el gamador es la ia\n¡Fin del juego!")
            ia = 1
            a = False


        if estado_botones == "principal":
            partida.dibujar_truco_envido_mazo(pantalla)
        elif estado_botones == "truco":
            partida.dibujar_truco(pantalla)
        elif contador == 0:
            if estado_botones == "envido":
                partida.dibujar_envido(pantalla)
        else:
            x = True
            estado_botones = "principal"
                    #puntos
        puntos_equipo_1, puntos_equipo_2 = actualizar_puntos(puntos_equipo_1, puntos_equipo_2, puntos,equipo_ganador)
        guardar_puntos_ronda(puntos_equipo_1, puntos_equipo_2)
        puntos_rondas = leer_puntos_rondas()
        y = 50
        for linea in puntos_rondas:
            fuente_textos_70= pygame.font.Font(None,40)
            texto_a = fuente_textos_70.render(linea.strip(), True, NEGRO)
            pantalla.blit(texto_a, (50, y))
            y += 30 
            pygame.display.flip()

        if puntos_equipo_1 >= puntos_para_ganar or puntos_equipo_2 >= puntos_para_ganar:
            print("¡Fin del juego!")
            a = False
    
    if a == False:
        time.sleep(1)
    pygame.display.flip()
pygame.quit()
