n = int(input())
day_or_night = input()

price = 0

if n >= 100:
    price = n * 0.06
elif n >= 20:
    price = n * 0.09
else:
    price = 0.70
    if day_or_night == "day":
        price += n * 0.79
    elif day_or_night == "night":
        price += n * 0.90

print(f"{price:.2f}")
