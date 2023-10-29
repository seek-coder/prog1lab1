def calculate_area_and_perimeter_circle(radio: float) -> tuple:
    if type(radio) in (int, float):
        from math import pi

        area = pi * radio**2
        perimeter = pi * 2 * radio # el diámetro es radio * 2

        circle_area_and_perimeter = (area, perimeter)
        return circle_area_and_perimeter
    else:
        return ValueError("Datos inválidos")
