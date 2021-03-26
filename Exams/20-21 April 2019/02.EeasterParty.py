guests = int(input())
plate_price = float(input())
budget = float(input())

if 10 <= guests <= 15:
    plate_price *= 0.85
elif 15 < guests <= 20:
    plate_price *= 0.80
elif guests > 20:
    plate_price *= 0.75

cake = 0.10 * budget

total = (guests * plate_price) + cake

if budget > total:
    print(f"It is party time! {budget - total:.2f} leva left.")
else:
    print(f"No party! {total - budget:.2f} leva needed.")