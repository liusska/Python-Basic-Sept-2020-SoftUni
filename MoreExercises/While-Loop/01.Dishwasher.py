bottles = int(input())
detergent = bottles * 750
day = 1
dishes = 0
pots = 0
enough = True

command = input()
while command != "End":
    quantity = int(command)
    if day % 3 == 0:
        pots += quantity
        detergent -= quantity * 15
    else:
        dishes += quantity
        detergent -= quantity * 5
    if detergent < 0:
        enough = False
        break
    day += 1
    command = input()


if enough:
    print("Detergent was enough!")
    print(f"{dishes} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {detergent} ml.")
else:
    print(f"Not enough detergent, {abs(detergent)} ml. more necessary!")