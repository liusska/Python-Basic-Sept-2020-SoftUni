from math import ceil

days = int(input())
total_food = float(input())
total_cat_food = 0
total_dog_food = 0
biscuits = 0

for day in range(1, days + 1):
    dog_food = int(input())
    cat_food = int(input())
    total_dog_food += dog_food
    total_cat_food += cat_food
    if day % 3 == 0:
        pets_food = (cat_food + dog_food) * 0.10
        biscuits += pets_food

total_food_eaten = total_cat_food + total_dog_food
print(f"Total eaten biscuits: {int(biscuits)}gr.")

food_eaten_percent = (total_food_eaten / total_food) * 100
print(f"{food_eaten_percent:.2f}% of the food has been eaten.")

dog_food_percent = (total_dog_food / total_food_eaten) * 100
print(f"{dog_food_percent:.2f}% eaten from the dog.")

cat_food_percent = (total_cat_food / total_food_eaten) * 100
print(f"{cat_food_percent:.2f}% eaten from the cat.")
