walk_in_min = int(input())
count_walk_in_day = int(input())
calories_per_day = int(input())

calories_burn = count_walk_in_day * walk_in_min * 5
total_calories = calories_per_day - calories_burn

if calories_burn >= total_calories / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burn}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burn}.")
