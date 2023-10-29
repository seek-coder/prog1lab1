def calculate_area_and_perimeter_rect(base: float, height: float) -> tuple:
    if type(base) in (int, float) and type(height) in (int, float):

        area = base * height  
        perimeter = 2 * base + 2 * height 

        rectangle_area_and_perimeter = (area, perimeter)
        return rectangle_area_and_perimeter
    else:
        return ValueError("Datos inválidos")
