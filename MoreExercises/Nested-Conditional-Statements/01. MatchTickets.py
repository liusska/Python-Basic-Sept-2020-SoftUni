budget = float(input())
category = input()
people = int(input())
tickets = 0

if 1 <= people <= 4:
    budget -= budget * 0.75
elif 5 <= people <= 9:
    budget -= budget * 0.60
elif 10 <= people <= 24:
    budget -= budget * 0.50
elif 25 <= people <= 49:
    budget -= budget * 0.40
elif people >= 50:
    budget -= budget * 0.25

if category == "VIP":
    tickets = 499.99 * people
elif category == "Normal":
    tickets = 249.99 * people

if budget >= tickets:
    print(f"Yes! You have {budget - tickets:.2f} leva left.")
else:
    print(f"Not enough money! You need {tickets - budget:.2f} leva.")

