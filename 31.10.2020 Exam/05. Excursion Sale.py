sea_exc = int(input())
mountain_exc = int(input())
total = 0
command = input()
while command != "Stop":
    if command == "sea":
        if sea_exc != 0:
            total += 680
            sea_exc -= 1
    elif command == "mountain":
        if mountain_exc != 0:
            total += 499
            mountain_exc -= 1
    if sea_exc == 0 and mountain_exc == 0:
        break
    command = input()

if sea_exc == 0 and mountain_exc == 0:
    print(f"Good job! Everything is sold.")

print(f"Profit: {total} leva.")