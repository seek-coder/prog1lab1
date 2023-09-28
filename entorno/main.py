import pygame, sys

pygame.init()

VENTANA = pygame.display.set_mode((600, 800))

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT: #QUIT = 256
            sys.exit()
