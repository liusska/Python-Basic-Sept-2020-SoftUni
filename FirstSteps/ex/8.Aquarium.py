length = int(input())
width = int(input())
height = int(input())
percent = float(input())

capacity = length * width * height
capacity_in_liters = capacity * 0.001
percent_real = percent * 0.01

liters = capacity_in_liters * (1 - percent_real)
print(liters)