n = 3
wins = 0
lost = 0
equals = 0

while n > 0:
    result = input()
    first = int(result[0])
    second = int(result[2])

    if first > second:
        wins += 1
    elif first == second:
        equals += 1
    else:
        lost += 1
    n -= 1

print(f"Team won {wins} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {equals}")
