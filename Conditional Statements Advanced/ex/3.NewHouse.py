flowers = input()
count = int(input())
money = int(input())
price = 0

if flowers == "Roses":
    price = 5
    total = count * price
    if count > 80:
        total *= 0.90
elif flowers == "Dahlias":
    price = 3.80
    total = count * price
    if count > 90:
        total *= 0.85
elif flowers == "Tulips":
    price = 2.80
    total = count * price
    if count > 80:
        total *= 0.85
elif flowers == "Narcissus":
    price = 3
    total = count * price
    if count < 120:
        total *= 1.15
elif flowers == "Gladiolus":
    price = 2.50
    total = count * price
    if count < 80:
        total *= 1.20

if total > money:
    needed_money = total - money
    print(f"Not enough money, you need {needed_money:.2f} leva more.")
else:
    extra_money = money - total
    print(f"Hey, you have a great garden with {count} {flowers} and {extra_money:.2f} leva left.")



