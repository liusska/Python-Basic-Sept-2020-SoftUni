from math import ceil, floor

days = int(input())
food_in_kilos = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day_gr = float(input())

dog_food = days * dog_food_per_day
cat_food = days * cat_food_per_day
turtle_food = days * (turtle_food_per_day_gr / 1000)
food_needed = dog_food + cat_food + turtle_food

if food_needed <= food_in_kilos:
    print(f"{floor(food_in_kilos - food_needed)} kilos of food left.")
else:
    print(f"{ceil(food_needed - food_in_kilos)} more kilos of food are needed.")