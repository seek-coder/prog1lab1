import pygame
from sys import exit

def main():
    pygame.init()

    WIDTH = 600
    HEIGHT = 800

    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pew-Pew! Paper Plane")
    CLOCK = pygame.time.Clock() #controlador del FRAMERATE

    BACKGROUND_LEVEL_ONE = pygame.image.load("data/assets/bg_first_level.png").convert() #convierte la imagen en un formato ideal en el que pueda trabajar pygame, para mejorar el rendimiento (tiene que ver con los colores y los pixeles)
    PLAYER = pygame.image.load("data/assets/player_48x48.png").convert_alpha() #en este caso, además, le agregamos la capacidad de modificar la opacidad (alpha)
    player_x_pos = 276
    # (WIDTH - LARGO DE IMAGEN) / 2 = CENTRAR HORIZONTALMENTE => (600px - 48px) / 2 = 276px
    player_y_pos = 712
    # HEIGHT - ANCHO DE IMAGEN = ALINEAR HACIA ABAJO => 800px - 48px = 752px. Pero dejo 40px de margen, => 712px

    player_hitbox = PLAYER.get_rect

    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                exit()

        SCREEN.blit(BACKGROUND_LEVEL_ONE,(0,0))
        player_y_pos -= 1
        SCREEN.blit(PLAYER,(player_x_pos,player_y_pos))

        pygame.display.update()
        CLOCK.tick(60)

main()
