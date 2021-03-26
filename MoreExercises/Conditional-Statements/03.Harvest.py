from math import floor, ceil

vineyard = int(input())
grapes = float(input())
wine_needed = int(input())
workers = int(input())

total_grapes = vineyard * grapes
wine = 0.4 * total_grapes / 2.5

if wine < wine_needed:
    print(f"It will be a tough winter! More {floor(wine_needed - wine)} liters wine needed.")
else:
    left_wine = abs(wine_needed - wine)
    print(f"Good harvest this year! Total wine: {floor(wine)} liters.")
    print(f"{ceil(left_wine)} liters left -> {ceil(left_wine / workers)} liters per person.")