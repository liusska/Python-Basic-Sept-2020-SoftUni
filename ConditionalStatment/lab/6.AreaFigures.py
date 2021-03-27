from math import pi

figures = input()

if figures == "square":
    side = float(input())
    result = side * side
    print(result)
elif figures == "rectangle":
    side1 = float(input())
    side2 = float(input())
    result = side2 * side1
    print(result)
elif figures == "circle":
    radius = float(input())
    result = pi*radius*radius
    print(result)
elif figures == "triangle":
    side1 = float(input())
    side2 = float(input())
    result = (side1 * side2) / 2
    print(result)