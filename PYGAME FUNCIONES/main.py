import pygame
from settings.config import *
from calculate_geometry import circle_calc, rect_calc, right_triangle_calc
from draw_screen import create_button_func, shape_list
from draw_screen.create_shape_func import create_shape_triangle, create_shape_circle, create_shape_rect, create_shape_square

# CONFIGURACIÓN GENERAL
pygame.init()

clock = pygame.time.Clock() # controlador del FRAMERATE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ejercicio de Pygame y funciones")

background = pygame.image.load("img/bg_geometry.png")

# VARIABLES
perimeter_text = None
area_text = None

# FLAGS
triangle_flag = False
circle_flag = False
rectangle_flag = False
square_flag = False

# BOTONES
button_triangle = create_button_func.create_button(20, 20, 230, 70, BLUE, DARK_CYAN, 30, "Dibujar triángulo", WHITE)
button_circle = create_button_func.create_button(20, 100, 230, 70, BLUE, DARK_CYAN, 30, "Dibujar círculo", WHITE)
button_rectangle = create_button_func.create_button(20, 180, 230, 70, BLUE, DARK_CYAN, 30, "Dibujar rectángulo", WHITE)
button_square = create_button_func.create_button(20, 260, 230, 70, BLUE, DARK_CYAN, 30, "Dibujar cuadrado", WHITE)

# FUNCIÓN PRINCIPAL
running = True
while running:
    clock.tick(FPS)

    mouse_x, mouse_y = pygame.mouse.get_pos() # obtener posición del cursor

    # 1 - DETECTAR EVENTOS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 2 - ACTUALIZAR EVENTOS / IMAGENES
    if button_triangle["button"].collidepoint(mouse_x, mouse_y):
        button_triangle["color"] = button_triangle["color_hover"]
        if pygame.mouse.get_pressed()[0]: # 0 es el click izquierdo
            print("CLICK TRIÁNGULO")
            triangle_flag = True
            circle_flag = False
            rectangle_flag = False
            square_flag = False
            area_and_perimeter, triangle_color, triangle_vertices = create_shape_triangle()
            print(area_and_perimeter, triangle_color, triangle_vertices)
            pygame.time.delay(200) # para evitar un ad infinitum
    else:
        button_triangle["color"] = BLUE  

    if button_circle["button"].collidepoint(mouse_x, mouse_y):
        button_circle["color"] = button_circle["color_hover"]  
        if pygame.mouse.get_pressed()[0]: # 0 es el click izquierdo
            print("CLICK CÍRCULO")  
            triangle_flag = False
            circle_flag = True
            rectangle_flag = False
            square_flag = False
            area_and_perimeter_circle, circle_center, circle_radio, circle_color = create_shape_circle()
            pygame.time.delay(200)
            
    else:
        button_circle["color"] = BLUE  

    if button_rectangle["button"].collidepoint(mouse_x, mouse_y):
        button_rectangle["color"] = button_rectangle["color_hover"]   
        if pygame.mouse.get_pressed()[0]: # 0 es el click izquierdo
            print("CLICK RECTÁNGULO") 
            triangle_flag = False
            circle_flag = False
            rectangle_flag = True
            square_flag = False
            area_and_perimeter_rect, rectangle, rectangle_color = create_shape_rect()
            pygame.time.delay(200)
    else:
        button_rectangle["color"] = BLUE  
    
    if button_square["button"].collidepoint(mouse_x, mouse_y):
        button_square["color"] = button_square["color_hover"]  
        if pygame.mouse.get_pressed()[0]: # 0 es el click izquierdo
            print("CLICK CUADRADO")  
            triangle_flag = False
            circle_flag = False
            rectangle_flag = False
            square_flag = True
            area_and_perimeter_square, square, square_color = create_shape_square()
            pygame.time.delay(200)
    else:
        button_square["color"] = BLUE  

    # 3 - DIBUJAR PANTALLA (RENDERIZAR)
    screen.blit(background, (0, 0))

    pygame.draw.rect(screen, button_triangle["color"], button_triangle["button"], 0, button_triangle["border"])
    pygame.draw.rect(screen, button_circle["color"], button_circle["button"], 0, button_circle["border"])
    pygame.draw.rect(screen, button_rectangle["color"], button_rectangle["button"], 0, button_rectangle["border"])
    pygame.draw.rect(screen, button_square["color"], button_square["button"], 0, button_square["border"])

    # texto de los botones
    font = pygame.font.Font(None, 26)

    button_triangle_text = font.render(button_triangle["text"], True, button_triangle["text_color"])
    button_circle_text = font.render(button_circle["text"], True, button_circle["text_color"])
    button_rectangle_text = font.render(button_rectangle["text"], True, button_rectangle["text_color"])
    button_square_text = font.render(button_square["text"], True, button_square["text_color"])

    rect_button_triangle_text = button_triangle_text.get_rect()
    rect_button_circle_text = button_circle_text.get_rect()
    rect_button_rectangle_text = button_rectangle_text.get_rect()
    rect_button_square_text = button_square_text.get_rect()

    rect_button_triangle_text.center = (button_triangle["button"].centerx, button_triangle["button"].centery)
    rect_button_circle_text.center = (button_circle["button"].centerx, button_circle["button"].centery)
    rect_button_rectangle_text.center = (button_rectangle["button"].centerx, button_rectangle["button"].centery)
    rect_button_square_text.center = (button_square["button"].centerx, button_square["button"].centery)

    screen.blit(button_triangle_text, rect_button_triangle_text)
    screen.blit(button_circle_text, rect_button_circle_text)
    screen.blit(button_rectangle_text, rect_button_rectangle_text)
    screen.blit(button_square_text, rect_button_square_text)


    # figuras geométricas
    if triangle_flag:
        pygame.draw.polygon(screen, triangle_color, triangle_vertices)
        # textos de las figuras
        area_text = area_and_perimeter[0]
        perimeter_text = area_and_perimeter[1]

        perimeter_text = font.render(f"El perímetro es de {perimeter_text:.6}px", True, BLACK)
        area_text = font.render(f"El área es de {area_text:.6}px", True, BLACK)

        rect_perimeter_text = perimeter_text.get_rect()
        rect_area_text = area_text.get_rect()

        rect_perimeter_text.center = (WIDTH // 1.5, HEIGHT - 80)
        rect_area_text.center = (WIDTH // 1.5, HEIGHT - 40)

        screen.blit(perimeter_text, rect_perimeter_text)
        screen.blit(area_text, rect_area_text)
    
    elif circle_flag:
        pygame.draw.circle(screen, circle_color, circle_center, circle_radio)

        area_text = area_and_perimeter_circle[0]
        perimeter_text = area_and_perimeter_circle[1]

        perimeter_text = font.render(f"El perímetro es de {perimeter_text:.6}px", True, BLACK)
        area_text = font.render(f"El área es de {area_text:.6}px", True, BLACK)

        rect_perimeter_text = perimeter_text.get_rect()
        rect_area_text = area_text.get_rect()

        rect_perimeter_text.center = (WIDTH // 1.5, HEIGHT - 80)
        rect_area_text.center = (WIDTH // 1.5, HEIGHT - 40)

        screen.blit(perimeter_text, rect_perimeter_text)
        screen.blit(area_text, rect_area_text)

    elif rectangle_flag:

        pygame.draw.rect(screen, rectangle_color, rectangle)

        area_text = area_and_perimeter_rect[0]
        perimeter_text = area_and_perimeter_rect[1]

        perimeter_text = font.render(f"El perímetro es de {float(perimeter_text):.6}px", True, BLACK)
        area_text = font.render(f"El área es de {float(area_text):.6}px", True, BLACK)

        rect_perimeter_text = perimeter_text.get_rect()
        rect_area_text = area_text.get_rect()

        rect_perimeter_text.center = (WIDTH // 1.5, HEIGHT - 80)
        rect_area_text.center = (WIDTH // 1.5, HEIGHT - 40)

        screen.blit(perimeter_text, rect_perimeter_text)
        screen.blit(area_text, rect_area_text)

    elif square_flag:

        pygame.draw.rect(screen, square_color, square)

        area_text = area_and_perimeter_square[0]
        perimeter_text = area_and_perimeter_square[1]

        perimeter_text = font.render(f"El perímetro es de {float(perimeter_text):.6}px", True, BLACK)
        area_text = font.render(f"El área es de {float(area_text):.6}px", True, BLACK)

        rect_perimeter_text = perimeter_text.get_rect()
        rect_area_text = area_text.get_rect()

        rect_perimeter_text.center = (WIDTH // 1.5, HEIGHT - 80)
        rect_area_text.center = (WIDTH // 1.5, HEIGHT - 40)

        screen.blit(perimeter_text, rect_perimeter_text)
        screen.blit(area_text, rect_area_text)

    # 4 - ACTUALIZAR PANTALLA
    pygame.display.flip()
pygame.quit() # termina el init()

