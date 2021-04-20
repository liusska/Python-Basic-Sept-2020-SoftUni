season = input()
km_per_month = float(input())

total = 0

if 10000 < km_per_month <= 20000:
    total = km_per_month * 1.45 * 4
elif 5000 < km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        total = km_per_month * 0.95 * 4
    elif season == "Summer":
        total = km_per_month * 1.10 * 4
    elif season == "Winter":
        total = km_per_month * 1.25 * 4
elif km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        total = km_per_month * 0.75 * 4
    elif season == "Summer":
        total = km_per_month * 0.90 * 4
    elif season == "Winter":
        total = km_per_month * 1.05 * 4

total *= 0.90

print(f"{total:.2f}")