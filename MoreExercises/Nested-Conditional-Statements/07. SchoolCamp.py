season = input()
type_group = input()
students = int(input())
nights = int(input())

sport = ""
total = ""

if season == "Winter":
    if type_group == "girls":
        total = students * nights * 9.60
        sport = "Gymnastics"
    elif type_group == "boys":
        total = students * nights * 9.60
        sport = "Judo"
    elif type_group == "mixed":
        total = students * nights * 10
        sport = "Ski"
elif season == "Spring":
    if type_group == "girls":
        total = students * nights * 7.20
        sport = "Athletics"
    elif type_group == "boys":
        total = students * nights * 7.20
        sport = "Tennis"
    elif type_group == "mixed":
        total = students * nights * 9.50
        sport = "Cycling"
elif season == "Summer":
    if type_group == "girls":
        total = students * nights * 15
        sport = "Volleyball"
    elif type_group == "boys":
        total = students * nights * 15
        sport = "Football"
    elif type_group == "mixed":
        total = students * nights * 20
        sport = "Swimming"

if students >= 50:
    total *= 0.50
elif 20 <= students < 50:
    total *= 0.85
elif 10 <= students < 20:
    total *= 0.95

print(f"{sport} {total:.2f} lv.")