count = int(input())

total = 0
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0

for i in range(count):
    group_count = int(input())
    total += group_count
    if group_count <= 5:
        musala += group_count
    elif 6 <= group_count <= 12:
        monblan += group_count
    elif 13 <= group_count <= 25:
        kilimandjaro += group_count
    elif 26 <= group_count <= 40:
        k2 += group_count
    elif group_count >= 41:
        everest += group_count

musala_percent = (musala / total) * 100
monblan_percent = (monblan / total) * 100
kilimandjaro_percent = (kilimandjaro / total) * 100
k2_percent = (k2 / total) * 100
everest_percent = (everest / total) * 100

print(f"{musala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kilimandjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")