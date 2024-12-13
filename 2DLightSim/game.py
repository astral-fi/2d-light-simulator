import pygame
import numpy as np
import math
from lights import Lights
from mirror import Mirror
from objects import Obj

pygame.init()
pygame.display.set_caption("Light")

width = 720
height = 720

screen = pygame.display.set_mode((width, height))

clock, fps = pygame.time.Clock(), 60

surface = pygame.Surface((720, 720), pygame.SRCALPHA)
surface.fill((0, 0, 0, 0))
# light = Lights(400, 300, 240, 500)
# light2 = Lights(500, 400, 240, 500)
brightness = np.zeros((width, height), dtype=np.float32)
# mirror1 = Mirror(200, 250, 75, surface)
# objects = [(300, 400, 20)]
objects = []
# mirrors = [mirror1]

running = True

def resetbutton(objects):
    objects.clear()
    return 

def addMirror(objects):
    newMirror = Mirror(360, 360, 50, surface)
    objects.append(newMirror)
    return

def addLight(objects):
    newLight = Lights(360, 360, (0, 0, 0), 500)
    objects.append(newLight)
    return 

def addObject(objects):
    newObj = Obj((110, 220, 110), 50, (360, 360), 360, 360)
    objects.append(newObj)
    return

def button(x, y, txt, fn, object):
    white = (255, 255, 255)
    gray = (150, 150, 150)
    black = (0, 0, 0)
    font = pygame.font.Font(None, 36)
    button_rect = pygame.Rect(x, y, 100, 60)  # x, y, width, height
    button_color = white
    button_text = txt
    button_hover_color = gray
    mouse_pos = pygame.mouse.get_pos()
    mouse_clicked = pygame.mouse.get_pressed()[0]
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, button_hover_color, button_rect)
        if mouse_clicked:
            fn(object)
             # call the funciton needed (fn)
    else:
        pygame.draw.rect(screen, button_color, button_rect)
    text_surface = font.render(button_text, True, black)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)


while running:
    screen.fill((0, 0, 0))
    brightness.fill(0)
    surface.fill((0, 0, 0))
    
    print(objects)
    for obj in objects:
        if obj.type == "Mirror":
            pygame.draw.line(surface, (120, 240, 120), (obj.x, obj.y + obj.length/2), (obj.x, obj.y - obj.length/2))
        elif obj.type == "Object":
            pygame.draw.circle(surface, obj.color, obj.pos, obj.radius)
        else:
            obj.lighting(screen, brightness, objects)

    screen.blit(surface, (0, 0))

    button(36, 620, 'Reset', resetbutton, objects)
    button(210, 620, 'Light', addLight, objects)
    button(384, 620, 'Object', addObject, objects)
    button(558, 620, 'Mirror', addMirror, objects)


    pygame.display.flip()

    clock.tick(60)

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
