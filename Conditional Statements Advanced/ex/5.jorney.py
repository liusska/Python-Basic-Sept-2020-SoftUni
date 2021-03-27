money = float(input())
season = input()
camp_or_hotel = ""
place = ""
price = 0

if season == "summer":
    camp_or_hotel = "Camp"
elif season == "winter":
    camp_or_hotel = "Hotel"

if money <= 100:
    place = "Bulgaria"
    if season == "summer":
        price = money * 0.30
    if season == "winter":
        price = money * 0.70
elif money <= 1000:
    place = "Balkans"
    if season == "summer":
        price = money * 0.40
    if season == "winter":
        price = money * 0.80
elif money > 1000:
    place = "Europe"
    camp_or_hotel = "Hotel"
    price = money * 0.90

print(f"Somewhere in {place}")
print(f"{camp_or_hotel} - {price:.2f}")
