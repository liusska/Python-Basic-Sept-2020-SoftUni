from math import ceil

average_speed = float(input())
fuel_in_liters_per_100 = float(input())
distance = 384400

total_distance = distance * 2
time_total_distance = ceil(total_distance / average_speed)
total_time = time_total_distance + 3
total_fuel = int((fuel_in_liters_per_100 * total_distance) / 100)

print(total_time)
print(total_fuel)