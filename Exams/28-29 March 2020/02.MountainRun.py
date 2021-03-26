
record_in_sec = float(input())
distance_in_meters = float(input())
time_sec_one_meter = float(input())

total_time = distance_in_meters * time_sec_one_meter
lag = (distance_in_meters // 50) * 30
record_george = total_time + lag

if record_george < record_in_sec:
    print(f"Yes! The new record is {record_george:.2f} seconds.")
else:
    print(f"No! He was {(record_george - record_in_sec):.2f} seconds slower.")