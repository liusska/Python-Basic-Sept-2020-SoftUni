from math import ceil, floor

days = int(input())
food = int(input())
food_per_first_deer = float(input())
food_per_second_deer = float(input())
food_per_third_deer = float(input())

first_deer = days * food_per_first_deer
second_deer = days * food_per_second_deer
third_deer = days * food_per_third_deer
total_needed_food = first_deer + second_deer + third_deer

diff = abs(total_needed_food - food)

if total_needed_food <= food:
    print(f"{floor(diff)} kilos of food left.")
else:
    print(f"{ceil(diff)} more kilos of food are needed.")