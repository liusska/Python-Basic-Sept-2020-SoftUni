t = float(input())

if 26 <= t <= 35:
    print("Hot")
elif 20.1 <= t <= 25.9:
    print("Warm")
elif 15 <= t <= 20:
    print("Mild")
elif 12 <= t <= 14.9:
    print("Cool")
elif 5 <= t <= 11.9:
    print("Cold")
else:
    print("unknown")