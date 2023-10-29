import pygame
from .shape_list import data_shape_list
from calculate_geometry import circle_calc, rect_calc, right_triangle_calc
from settings.config import *

quantity = len(data_shape_list)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def create_shape_triangle():
    for element in range(quantity):
        shape_data = data_shape_list[element]

        if shape_data["shape_name"] == "right triangle":
            area_and_perimeter_triangle = right_triangle_calc.calculate_area_and_perimeter_right_triangle(shape_data["cathetusA"], shape_data["cathetusB"]) # me da un tupla (area, perimetro)

            triangle_vertex2 = (shape_data["initial_pos"][0] + shape_data["cathetusA"], shape_data["initial_pos"][1])
            triangle_vertex3 = (shape_data["initial_pos"][0], shape_data["initial_pos"][1] - shape_data["cathetusB"])
            triangle_vertex1 = shape_data["initial_pos"]
            triangle_color = shape_data["color"]

            triangle_vertices = [triangle_vertex1, triangle_vertex2, triangle_vertex3]

    return area_and_perimeter_triangle, triangle_color, triangle_vertices

def create_shape_circle():
    for element in range(quantity):
        shape_data = data_shape_list[element]

        if shape_data["shape_name"] == "circle":
            area_and_perimeter_circle = circle_calc.calculate_area_and_perimeter_circle(shape_data["radio"])

            circle_center = shape_data["initial_pos"]
            circle_radio = shape_data["radio"]
            circle_color = shape_data["color"]
        
    return area_and_perimeter_circle, circle_center, circle_radio, circle_color

def create_shape_rect():
    for element in range(quantity):
        shape_data = data_shape_list[element]

        if shape_data["shape_name"] == "rectangle":
            area_and_perimeter_rect = rect_calc.calculate_area_and_perimeter_rect(shape_data["base"], shape_data["height"])

            rectangle = pygame.Rect(shape_data["initial_pos"][0], shape_data["initial_pos"][1], shape_data["base"], shape_data["height"])
            rectangle_color = shape_data["color"]

    return area_and_perimeter_rect, rectangle, rectangle_color

def create_shape_square():
    for element in range(quantity):
        shape_data = data_shape_list[element]

        if shape_data["shape_name"] == "square":
            area_and_perimeter_square = rect_calc.calculate_area_and_perimeter_rect(shape_data["base"], shape_data["height"])

            square = pygame.Rect(shape_data["initial_pos"][0], shape_data["initial_pos"][1], shape_data["base"], shape_data["height"])
            square_color = shape_data["color"]

    return area_and_perimeter_square, square, square_color
        