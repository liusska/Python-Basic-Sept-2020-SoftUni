budget = float(input())
fuel = float(input())
day = input()
guide = 100
fuel_per_liter = 2.10

price = fuel * fuel_per_liter + guide
if day == "Saturday":
    price *= 0.90
elif day == "Sunday":
    price *= 0.80
diff = abs(budget - price)
if budget >= price:
    print(f"Safari time! Money left: {diff:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")