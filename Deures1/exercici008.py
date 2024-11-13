#!/usr/bin/env python3

import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0) 

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')

font = pygame.font.SysFont("Arial",14)
mouse_data = {"x":-1,"y":-1,"pressed":False,"released": False}
buttons = [
    { "value": "up",   "x": 25, "y": 25, "width": 25, "height": 25, "pressed": False },
    { "value": "down", "x": 25, "y": 50, "width": 25, "height": 25, "pressed": False },
]

direction = "up"
position_y = 250
radius = 25

# Bucle de l'aplicació
def main():
    is_looping = True

    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()

        clock.tick(60) # Limitar a 60 FPS

    # Fora del bucle, tancar l'aplicació
    pygame.quit()
    sys.exit()

# Gestionar events
def app_events():
    global mouse_data, direction

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for button in buttons:
                if is_point_in_rect(mouse_pos, button):
                    direction = button["value"]  # Actualizar dirección según el botón presionado
    return True

# Función de cálculo de la aplicación
def app_run():
    global position_y, radius

    # Actualizar posición del círculo en función de la dirección
    delta_time = clock.get_time() / 1000.0  # Convertir a segundos
    speed = 150

    if direction == "up":
        position_y -= speed * delta_time
    else:
        position_y += speed * delta_time

    # Limitar la posición del círculo a los bordes de la pantalla
    position_y = max(radius, min(position_y, screen.get_height() - radius))


# Dibuixar
def app_draw():
    global position_y
    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Dibuixar la graella de coordenades (llibreria utils)
    for button in buttons:
        draw_button(button)

    cerce = (500,position_y)
    pygame.draw.circle(screen,BLUE,cerce,radius)
    # Actualitzar el dibuix a la finestra
    pygame.display.update()

def draw_button(button):
    color = WHITE
    if button["pressed"]:
        color = ORANGE
    elif direction == button["value"]:
        color = BLUE
    rect_tuple = button["x"],button["y"],button["width"],button["height"]
    pygame.draw.rect(screen,color,rect_tuple)
    pygame.draw.rect(screen,BLACK,rect_tuple,2)

def is_point_in_rect(point, rect):
    x, y = point
    return rect["x"] <= x <= rect["x"] + rect["width"] and rect["y"] <= y <= rect["y"] + rect["height"]
if __name__ == "__main__":
    main()
