# Да се напише програма, в която потребителят въвежда вида и размерите на геометрична фигура и пресмята лицето й. Фигурите са четири вида: квадрат (square), правоъгълник (rectangle), кръг (circle) и триъгълник (triangle). На първия ред на входа се чете вида на фигурата (текст със следните възможности: square, rectangle, circle или triangle).

# · Ако фигурата е квадрат (square): на следващия ред се чете едно дробно число - дължина на страната му

# · Ако фигурата е правоъгълник (rectangle): на следващите два реда четат две дробни числа - дължините на страните му

# · Ако фигурата е кръг (circle): на следващия ред чете едно дробно число - радиусът на кръга

# · Ако фигурата е триъгълник (triangle): на следващите два реда четат две дробни числа - дължината на страната му и дължината на височината към нея

# Резултатът да се закръгли до 3 цифри след десетичната запетая. 

import math

shape = input()

if shape == 'square':
    length = float(input())
    result = length ** 2
    print(f"{result:.3f}")
elif shape == 'rectangle':
    side1 = float(input())
    side2 = float(input())
    result = side1 * side2
    print(f"{result:.3f}")
elif shape == 'circle':
    radius = float(input())
    area = math.pi * (radius ** 2)
    print(f"{area:.3f}")
elif shape == 'triangle':
    side = float(input())
    height = float(input())
    area = (side * height) / 2
    print(f"{area:.3f}")