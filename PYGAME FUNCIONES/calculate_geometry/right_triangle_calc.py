def calculate_area_and_perimeter_right_triangle(cathetusA: float, cathetusB: float) -> tuple:
    if type(cathetusA) in (int, float) and type(cathetusB) in (int, float):
        from math import sqrt

        hypotenuse = sqrt(cathetusA**2 + cathetusB**2)
        area = (cathetusA * cathetusB) / 2 # altura es area / base; base es perimetro / 2
        perimeter = cathetusA + cathetusB + hypotenuse

        triangle_area_and_perimeter = (area, perimeter)
        return triangle_area_and_perimeter
    else:
        return ValueError("Datos inválidos")
