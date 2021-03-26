budget = float(input())
count = 1
total_price = 0
is_enough = True
command = input()
while command != "Stop":
    product_name = command
    product_price = float(input())
    if count % 3 == 0:
        total_price += product_price / 2
    else:
        total_price += product_price
    if budget < total_price:
        is_enough = False
        break
    count += 1
    command = input()

if is_enough:
    print(f"You bought {count - 1} products for {total_price:.2f} leva.")
else:
    diff = abs(total_price - budget)
    print(f"You don't have enough money!")
    print(f"You need {diff:.2f} leva!")