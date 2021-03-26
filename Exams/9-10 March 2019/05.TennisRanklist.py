tournaments = int(input())
start_points = int(input())
points = 0
wins = 0
for i in range(1, tournaments + 1):
    result = input()
    if result == "W":
        wins += 1
        points += 2000
    elif result == "F":
        points += 1200
    elif result == "SF":
        points += 720

total_points = start_points + points
print(f"Final points: {total_points}")
print(f"Average points: {int(points / tournaments)}")
print(f"{wins / tournaments * 100 :.2f}%")