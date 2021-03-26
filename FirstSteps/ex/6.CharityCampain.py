days_campaign = int(input())
cookers = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())

cake_price_per_one = 45
waffle_price_per_one = 5.8
pancake_price_per_one = 3.2

cakes_price = cakes * cake_price_per_one
waffles_price = waffles * waffle_price_per_one
pancakes_price = pancakes * pancake_price_per_one

sum_per_day = (cakes_price + waffles_price + pancakes_price) * cookers
sum_per_all_days = sum_per_day * days_campaign
result = sum_per_all_days - sum_per_all_days / 8

print(result)




