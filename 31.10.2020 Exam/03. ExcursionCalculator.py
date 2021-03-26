people = int(input())
season = input()
price = 0

if season == "spring":
    if people <= 5:
        price = people * 50
    elif people > 5:
        price = people * 48
elif season == "summer":
    if people <= 5:
        price = people * 48.50
    elif people > 5:
        price = people * 45
elif season == "autumn":
    if people <= 5:
        price = people * 60
    elif people > 5:
        price = people * 49.50
elif season == "winter":
    if people <= 5:
        price = people * 86
    elif people > 5:
        price = people * 85

if season == "summer":
    price = price * 0.85
elif season == "winter":
    price = price * 1.08

print(f"{price :.2f} leva.")