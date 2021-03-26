food = int(input())
food_in_gr = food * 1000
command = input()
eat_food = 0

while command != "Adopted":
    current_food = int(command)
    eat_food += current_food

    command = input()


diff = abs(eat_food - food_in_gr)

if eat_food > food_in_gr:
    print(f"Food is not enough. You need {diff} grams more.")
else:
    print(f"Food is enough! Leftovers: {diff} grams.")