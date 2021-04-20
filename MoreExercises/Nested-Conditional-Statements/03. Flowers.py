chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
day = input()

total = 0

if season == "Spring" or season == "Summer":
    total = chrysanthemums * 2 + roses * 4.10 + tulips * 2.50
    if day == "Y":
        total *= 1.15
    if season == "Spring" and tulips > 7:
        total *= 0.95
elif season == "Winter" or season == "Autumn":
    total = chrysanthemums * 3.75 + roses * 4.50 + tulips * 4.15
    if day == "Y":
        total *= 1.15
    if season == "Winter" and roses >= 10:
        total *= 0.90
if tulips + chrysanthemums + roses > 20:
    total *= 0.80

total += 2
print(f"{total:.2f}")