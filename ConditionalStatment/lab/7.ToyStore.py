price_trip = float(input())
puzzles_count = float(input())
dolls_count = float(input())
bears_count = float(input())
minions_count = float(input())
trucks_count = float(input())

puzzles_price = 2.60
dolls_price = 3
bears_price = 4.10
minions_price = 8.20
trucks_price = 2

puzzles = puzzles_count * puzzles_price
dolls = dolls_count * dolls_price
bears = bears_count * bears_price
minions = minions_count * minions_price
trucks = trucks_count * trucks_price

toys_count = puzzles_count + dolls_count + bears_count + minions_count + trucks_count
sum_toys = puzzles + dolls + bears + minions + trucks

if toys_count >= 50:
    sum_toys = sum_toys * 0.75


sum_toys = sum_toys * 0.90

if sum_toys >= price_trip:
    print(f"Yes! {(sum_toys - price_trip):.2f} lv left.")
else:
    print(f"Not enough money! {(price_trip - sum_toys):.2f} lv needed.")



