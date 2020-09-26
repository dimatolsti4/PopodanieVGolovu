import pygame
from pygame.draw import *

# Смайлик получился очень злой

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

x1 = 200; y1 = 200
x2 = 150; y2 = 170
x3 = 250; y3 = 170
color_yellow = (255, 255, 0)
color_red = (255, 0, 0)
color_black = (0, 0, 0)

circle(screen, color_yellow, (x1, y1), 100)
circle(screen, color_red, (x2,y2), 20)
circle(screen, color_red, (x3,y3), 15)
circle(screen, color_black, (x2,y2), 10)
circle(screen, color_black, (x3,y3), 10)

rect(screen, color_red, (150, 250, 100, 20))

polygon(screen, color_red, [(100, 130), (120,120), (205, 160), (180, 170)])
polygon(screen, color_red, [(300, 50), (290, 70), (215, 200), (205, 190)])
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
