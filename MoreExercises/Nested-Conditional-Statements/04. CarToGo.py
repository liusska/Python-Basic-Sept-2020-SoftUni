budget = float(input())
season = input()

class_car = ""
type_car = ""
price = 0

if budget > 500:
    class_car = "Luxury class"
    type_car = "Jeep"
    price = budget * 0.90
elif 100 < budget <= 500:
    class_car = "Compact class"
    if season == "Summer":
        price = budget * 0.45
        type_car = "Cabrio"
    elif season == "Winter":
        price = budget * 0.80
        type_car = "Jeep"
elif budget <= 100:
    class_car = "Economy class"
    if season == "Summer":
        price = budget * 0.35
        type_car = "Cabrio"
    elif season == "Winter":
        price = budget * 0.65
        type_car = "Jeep"

print(class_car)
print(f"{type_car} - {price:.2f}")