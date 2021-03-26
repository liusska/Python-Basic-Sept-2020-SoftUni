capacity = float(input())
count = 1
space = True

command = input()
while command != "End":
    suitcase = float(command)
    if count % 3 == 0:
        capacity -= suitcase * 1.10
    else:
        capacity -= suitcase
    if capacity < 0:
        space = False
        break
    count += 1
    command = input()

if space:
    print("Congratulations! All suitcases are loaded!")
else:
    print("No more space!")
print(f"Statistic: {count - 1} suitcases loaded.")