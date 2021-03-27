days = int(input())
type_room = input()
rating = input()

room_for_one_person = 18
apartment = 25
president_apartment = 35
total = 0

if type_room == "room for one person":
    total = (days - 1) * room_for_one_person
elif type_room == "apartment":
    total = (days - 1) * apartment
    if days < 10:
        total *= 0.70
    elif 10 <= days <= 15:
        total *= 0.65
    elif days > 15:
        total *= 0.50
elif type_room == "president apartment":
    total = (days - 1) * president_apartment
    if days < 10:
        total *= 0.90
    elif 10 <= days <= 15:
        total *= 0.85
    elif days > 15:
        total *= 0.80

if rating == "positive":
    total *= 1.25
elif rating == "negative":
    total *= 0.90

print(f"{total:.2f}")