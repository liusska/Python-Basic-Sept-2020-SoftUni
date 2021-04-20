budget = float(input())
season = input()

place = ""
location = ""
price = 0

if budget > 3000:
    place = "Hotel"
    price = budget * 0.90
    if season == "Summer":
        location = "Alaska"
    elif season == "Winter":
        location = "Morocco"
elif 1000 < budget <= 3000:
    place = "Hut"
    if season == "Summer":
        price = budget * 0.80
        location = "Alaska"
    elif season == "Winter":
        price = budget * 0.60
        location = "Morocco"
elif budget <= 1000:
    place = "Camp"
    if season == "Summer":
        price = budget * 0.65
        location = "Alaska"
    elif season == "Winter":
        price = budget * 0.45
        location = "Morocco"

print(f"{location} - {place} - {price:.2f}")