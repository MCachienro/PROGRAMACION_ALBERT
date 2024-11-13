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
YELLOW = (255,255,0)
pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')

window_size = { 
    "width": 0, 
    "height": 0, 
    "center": {
        "x": 0,
        "y": 0
    } 
}
mouse_pos = { "x": -1, "y": -1 }

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
    global mouse_pos
    mouse_inside = pygame.mouse.get_focused()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
        elif event.type == pygame.MOUSEMOTION:
            if mouse_inside:
                mouse_pos["x"] = event.pos[0]
                mouse_pos["y"] = event.pos[1]
            else:
                mouse_pos["x"] = -1
                mouse_pos["y"] = -1
    return True


# Fer càlculs
def app_run():
    global window_size

    window_size["width"] = screen.get_width()
    window_size["height"] = screen.get_height()
    window_size["center"]["x"] = int(screen.get_width() / 2)
    window_size["center"]["y"] = int(screen.get_height() / 2)

# Dibuixar
def app_draw():
    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Dibuixar la graella de coordenades (llibreria utils)
    utils.draw_grid(pygame, screen, 50)

    pygame.draw.rect(screen, BLACK, (50,50,540, 425),5)

    pygame.draw.line(screen,BLACK,(320,0),(320,500),5)

    pygame.draw.line(screen,BLACK,(0,240),(700,240),5)


    q_x = mouse_pos["x"] - 20
    q_y = mouse_pos["y"] - 20

    color = cambiar_color(q_x, q_y)

    rect = (q_x, q_y, 40, 40)
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, BLACK, rect, 2)

    # Actualitzar el dibuix a la finestra
    pygame.display.update()


def cambiar_color(x,y):
    if 0 <= x < 300 and 0 <= y < 200:
        color = RED
    elif 300 <= x < 600 and 0 <= y < 200:
        color = GREEN
    elif 0 <= x < 300 and 200 <= y < 400:
        color = BLUE
    elif 300 <= x < 600 and 0 <= y < 400:
        color = YELLOW 
    else:
        color = BLACK
    return color
if __name__ == "__main__":
    main()
