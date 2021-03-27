money = float(input())
people = int(input())
price_clothes_per_one = float(input())

decor = float(money * 0.10)

if people > 150:
    price_clothes_per_one *= 0.90

price_clothes = people * price_clothes_per_one
result = decor + price_clothes

if result > money:
    print("Not enough money!")
    print(f"Wingard needs {(result - money):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {(money - result):.2f} leva left.")



