from math import ceil

guests = int(input())
budget = int(input())

easter_bread = ceil(guests / 3)
eggs = guests * 2

total = easter_bread * 4 + eggs * 0.45

diff = abs(budget - total)
if budget >= total:
    print(f"Lyubo bought {easter_bread} Easter bread and {eggs} eggs.")
    print(f"He has {diff:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {diff:.2f} lv. more.")