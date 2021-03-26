days = int(input())
hours = int(input())
parking = 0
total = 0
for day in range(1, days + 1):
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            parking += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            parking += 1.25
        else:
            parking += 1
    print(f"Day: {day} - {parking:.2f} leva")
    total += parking
    parking = 0

print(f"Total: {total:.2f} leva")