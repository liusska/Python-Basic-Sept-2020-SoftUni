w = float(input())
h = float(input())

h_in_meters = (h * 100) - 100
tables = h_in_meters // 70

w_in_meters = w * 100
rows = w_in_meters // 120

places = int(tables * rows - 3)
print(places)

