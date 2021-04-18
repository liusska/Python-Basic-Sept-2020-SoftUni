x = float(input())
y = float(input())
h = float(input())

side = x * y
window = 1.5 * 1.5
two_sides = 2 * side - 2 * window
back_side = x * x
door = 1.2 * 2
total_back_side = 2 * back_side - door
total_walls = two_sides + total_back_side
green = total_walls / 3.4

roof_ride = 2 * (x * y)
roof_triangle = 2 * (x * h / 2)
total_roof = roof_ride + roof_triangle
red = total_roof / 4.3

print(f"{green:.2f}")
print(f"{red:.2f}")
