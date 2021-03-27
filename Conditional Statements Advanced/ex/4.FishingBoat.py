money = int(input())
season = input()
count = int(input())
rent = 0


if season == "Summer" or season == "Autumn":
    rent = 4200
elif season == "Spring":
    rent = 3000
elif season == "Winter":
    rent = 2600

if count <= 6:
    rent *= 0.90
    if count % 2 == 0 and season != "Autumn":
        rent *= 0.95
elif 7 <= count <= 11:
    rent *= 0.85
    if count % 2 == 0 and season != "Autumn":
        rent *= 0.95
elif count >= 12:
    rent *= 0.75
    if count % 2 == 0 and season != "Autumn":
        rent *= 0.95

if money < rent:
    needed_money = rent - money
    print(f"Not enough money! You need {needed_money:.2f} leva.")
elif money >= rent:
    extra_money = money - rent
    print(f"Yes! You have {extra_money:.2f} leva left.")

