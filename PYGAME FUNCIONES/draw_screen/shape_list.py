from settings.config import *

data_shape_list =\
[
    {
        "shape_name": "right triangle",
        "cathetusA": 300,
        "cathetusB": 200,
        "initial_pos": (WIDTH // 2, HEIGHT // 2),
        "color": RED
    },
    {
        "shape_name": "circle",
        "radio" : 120.25,
        "initial_pos": (WIDTH // 1.5, HEIGHT // 2.5),
        "color": BLUE
    },
    {
        "shape_name": "rectangle",
        "base": 300,
        "height": 150,
        "initial_pos": (WIDTH // 2, HEIGHT - 450),
        "color": GREEN
    },
    {
        "shape_name": "square",
        "base": 300,
        "height": 300,
        "initial_pos": (WIDTH // 2, HEIGHT - 450),
        "color": YELLOW
    }
]