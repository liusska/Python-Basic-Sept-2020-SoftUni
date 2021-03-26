chicken = int(input())
fish = int(input())
vegetarian = int(input())

fish_price = 12.40
chicken_price = 10.35
vegetarian_price = 8.15
price_menu = chicken * chicken_price + fish * fish_price + vegetarian * vegetarian_price

desert = price_menu * 0.20
total_price = price_menu + desert + 2.50

print(f"Total: {total_price:.2f}")
