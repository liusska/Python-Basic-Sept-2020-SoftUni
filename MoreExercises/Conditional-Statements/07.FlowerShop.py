from math import floor, ceil

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cactus = int(input())
present_price = float(input())

magnolias_price = magnolias * 3.25
hyacinths_price = hyacinths * 4
roses_price = roses * 3.50
cactus_price = cactus * 8

total_money = 0.95 * (magnolias_price + hyacinths_price + roses_price + cactus_price)

if total_money >= present_price:
    print(f"She is left with {floor(total_money - present_price)} leva.")
else:
    print(f"She will have to borrow {ceil(present_price - total_money)} leva.")
