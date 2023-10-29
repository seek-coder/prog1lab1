from pygame import Rect

def create_button(left: float = 0, top: float = 0, width: float = 100, height: float = 50, color: tuple = (255, 255, 255), color_hover: tuple = (180, 180, 180), border = 0, text: str = "", text_color: tuple = (50, 50, 50)):
    return {
        "button": Rect(left, top, width, height),
        "color": color,
        "color_hover": color_hover,
        "border": border,
        "text": text,
        "text_color": text_color
    }


