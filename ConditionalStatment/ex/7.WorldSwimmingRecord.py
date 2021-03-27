record_in_sec = float(input())
distance_in_m = float(input())
time_for_one_meter = float(input())

time_distance = distance_in_m * time_for_one_meter
water_resistance = int((distance_in_m / 15)) * 12.5
total = float(time_distance + water_resistance)

if record_in_sec > total:
    print(f"Yes, he succeeded! The new world record is {total:.2f} seconds.")
else:
    print(f"No, he failed! He was {(total - record_in_sec):.2f} seconds slower.")
