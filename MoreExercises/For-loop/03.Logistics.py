load = int(input())
minibus = 0
truck = 0
train = 0
total_price = 0
for i in range(1, load + 1):
    load_in_tones = int(input())
    if load_in_tones <= 3:
        total_price += load_in_tones * 200
        minibus += load_in_tones
    elif 4 <= load_in_tones <= 11:
        total_price += load_in_tones * 175
        truck += load_in_tones
    elif load_in_tones >= 12:
        total_price += load_in_tones * 120
        train += load_in_tones

total_load = train + truck + minibus
total_average = total_price / total_load

print(f"{total_average: .2f}")
print(f"{minibus / total_load * 100 :.2f}%")
print(f"{truck / total_load * 100 :.2f}%")
print(f"{train / total_load * 100 :.2f}%")

