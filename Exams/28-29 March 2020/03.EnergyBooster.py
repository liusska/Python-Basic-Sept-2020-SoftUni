fruit = input()
size = input()
count = int(input())

price = 0

if size == "small":
    if fruit == "Watermelon":
        price = 56 * 2
    elif fruit == "Mango":
        price = 36.66 * 2
    elif fruit == "Pineapple":
        price = 42.10 * 2
    elif fruit == "Raspberry":
        price = 20 * 2
elif size == "big":
    if fruit == "Watermelon":
        price = 28.70 * 5
    elif fruit == "Mango":
        price = 19.60 * 5
    elif fruit == "Pineapple":
        price = 24.80 * 5
    elif fruit == "Raspberry":
        price = 15.20 * 5

price_fruits = count * price

if 400 <= price_fruits <= 1000:
    total_price = price_fruits * 0.85
elif price_fruits > 1000:
    total_price = price_fruits * 0.50
else:
    total_price = price_fruits

print(f"{total_price:.2f} lv.")