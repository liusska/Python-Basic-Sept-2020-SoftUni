strawberry_price = float(input())
bananas_in_kilo = float(input())
oranges_in_kilo = float(input())
raspberries_in_kilo = float(input())
strawberries_in_kilo = float(input())

raspberries_price = strawberry_price / 2
oranges_price = raspberries_price * 0.6
bananas_price = raspberries_price * 0.2

strawberries = strawberries_in_kilo * strawberry_price
raspberries = raspberries_in_kilo * raspberries_price
oranges = oranges_in_kilo * oranges_price
bananas = bananas_in_kilo * bananas_price

sums = strawberries + raspberries + bananas + oranges

print(float(sums))
