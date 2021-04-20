juniors = int(input())
seniors = int(input())
type_race = input()

tax = 0

if type_race == "trail":
    tax = juniors * 5.50 + seniors * 7
    tax *= 0.95
elif type_race == "cross-country":
    tax = juniors * 8 + seniors * 9.50
    tax *= 0.95
    if juniors + seniors >= 50:
        tax *= 0.75
elif type_race == "downhill":
    tax = juniors * 12.25 + seniors * 13.75
    tax *= 0.95
elif type_race == "road":
    tax = juniors * 20 + seniors * 21.50
    tax *= 0.95

print(f"{tax:.2f}")