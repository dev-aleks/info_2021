def main():
    x, y = 300, 400
    width, height = 200, 300

    draw_house(x, y, width, height)

def draw_house(x, y, width, height):
    '''
    Функция рисует домик
    :param x: координата x у низа фундамента
    :param y: координата y у низа фундамента
    :param width: полная ширина домика (фундамент или вылеты крыши включены)
    :param height: полная высота домика
    :return: None
    '''
    print('drawing house', x, y, width, height)
    foundation_height = 0.05 * height
    walls_height = 0.9 * width
    walls_weight = 0.5 * height
    roof_height = height - foundation_height - walls_height

    draw_house_foundation(x, y, width, foundation_height)
    draw_house_walls(x, y - foundation_height, walls_weight, walls_height)
    draw_house_roof(x, y - foundation_height - walls_height, width, roof_height)

def draw_house_foundation(x, y, width, foundation_height):
    """
    Нарисовать фундамент
    """
    pass

def draw_house_walls(x, y - foundation_height, walls_weight, walls_height):
    """
    Нарисовать стены
    """
    pass

def draw_house_roof(x, y - foundation_height - walls_height, width, roof_height):
    """
    Нарисовать крышу
    """
    pass

main()
