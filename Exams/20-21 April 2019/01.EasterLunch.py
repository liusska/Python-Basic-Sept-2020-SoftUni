easter_bread = int(input())
eggs_twelve = int(input())
biscuits_kg = int(input())

easter_bread_price = 3.20
eggs_twelve_price = 4.35
biscuits_per_kg = 5.40
color_for_one_egg = 0.15

price = easter_bread * easter_bread_price + eggs_twelve * eggs_twelve_price + biscuits_kg * biscuits_per_kg
color_for_eggs = eggs_twelve * color_for_one_egg * 12
total_price = price + color_for_eggs

print(f"{total_price:.2f}")
