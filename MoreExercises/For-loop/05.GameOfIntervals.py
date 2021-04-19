iteration = int(input())

from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
invalid_numbers = 0
total = 0
for i in range(1, iteration + 1):
    number = int(input())
    if number < 0 or number > 50:
        invalid_numbers += 1
        total /= 2
    elif 40 <= number <= 50:
        total += 100
        from_40_to_50 += 1
    elif 30 <= number <= 39:
        total += 50
        from_30_to_39 += 1
    elif 20 <= number <= 29:
        total += number * 0.40
        from_20_to_29 += 1
    elif 10 <= number <= 19:
        total += number * 0.30
        from_10_to_19 += 1
    elif 0 <= number <= 9:
        total += number * 0.20
        from_0_to_9 += 1

print(f"{total:.2f}")

print(f"From 0 to 9: {from_0_to_9 / iteration * 100:.2f}%")
print(f"From 10 to 19: {from_10_to_19 / iteration * 100:.2f}%")
print(f"From 20 to 29: {from_20_to_29 / iteration * 100:.2f}%")
print(f"From 30 to 39: {from_30_to_39 / iteration * 100:.2f}%")
print(f"From 40 to 50: {from_40_to_50 / iteration * 100:.2f}%")
print(f"Invalid numbers: {invalid_numbers / iteration * 100:.2f}%")

