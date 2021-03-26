first_name = input()
second_name = input()
first_points = 0
second_points = 0
is_war = False

command = input()
while command != "End of game":
    first_card = int(command)
    second_card = int(input())

    if first_card > second_card:
        first_points += (first_card - second_card)
    elif second_card > first_card:
        second_points += (second_card - first_card)
    elif first_card == second_card:
        is_war = True
        first_card = int(input())
        second_card = int(input())
        print("Number wars!")
        if first_card > second_card:
            print(f"{first_name} is winner with {first_points} points")
        else:
            print(f"{second_name} is winner with {second_points} points")
        break
    command = input()

if not is_war:
    print(f"{first_name} has {first_points} points")
    print(f"{second_name} has {second_points} points")
