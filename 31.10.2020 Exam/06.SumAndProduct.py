n = int(input())
is_exist = False
for a in range(1, 10):
    for b in range(9, a - 1, -1):
        for c in range(1, 10):
            for d in range(9, c - 1, -1):
                aggregate = a + b + c + d
                multiplication = a * b * c * d
                if aggregate == multiplication and n % 10 == 5:
                    print(f"{a}{b}{c}{d}")
                    is_exist = True
                    break
                if multiplication // aggregate == 3 and n % 3 == 0:
                    print(f"{d}{c}{b}{a}")
                    is_exist = True
                    break
                if is_exist:
                    break
            if is_exist:
                break
        if is_exist:
            break
    if is_exist:
        break

if not is_exist:
    print("Nothing found")