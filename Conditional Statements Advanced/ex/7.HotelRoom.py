month = input()
nights = int(input())
studio = 0
apartment = 0
total_apartment = 0
total_studio = 0

if month == "May" or month == "October":
    studio = 50
    apartment = 65
    total_apartment = nights * apartment
    if nights > 14:
        total_apartment *= 0.90
    print(f"Apartment: {total_apartment:.2f} lv.")
    total_studio = nights * studio
    if 7 < nights <= 14:
        total_studio *= 0.95
    elif nights > 14:
        total_studio *= 0.70
    print(f"Studio: {total_studio:.2f} lv.")
elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    total_apartment = nights * apartment
    if nights > 14:
        total_apartment *= 0.90
    print(f"Apartment: {total_apartment:.2f} lv.")
    total_studio = nights * studio
    if nights > 14:
        total_studio *= 0.80
    print(f"Studio: {total_studio:.2f} lv.")

elif month == "July" or month == "August":
    studio = 76
    apartment = 77
    total_apartment = nights * apartment
    if nights > 14:
        total_apartment *= 0.90
    print(f"Apartment: {total_apartment:.2f} lv.")
    total_studio = nights * studio
    print(f"Studio: {total_studio:.2f} lv.")


