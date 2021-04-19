months = int(input())
water = months * 20
internet = months * 15
others = 0
electricity_total = 0

for i in range(1, months + 1):
    electricity = float(input())
    electricity_total += electricity
    others += (electricity + 20 + 15) * 1.20

print(f"Electricity: {electricity_total:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {others:.2f} lv")
average_bills_per_month = (electricity_total + water + internet + others) / months
print(f"Average: {average_bills_per_month:.2f} lv")