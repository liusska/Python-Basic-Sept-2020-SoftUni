people = int(input())
nights = int(input())
cards = int(input())
tickets = int(input())

price_night = 20
price_card = 1.60
price_ticket = 6

total = people * (price_night * nights + cards * price_card + price_ticket * tickets)
total *= 1.25
print(f"{total:.2f}")
