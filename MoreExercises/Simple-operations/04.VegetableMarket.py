price_vegetables = float(input())
price_fruits = float(input())
price_per_kilo_vegetables = float(input())
price_per_kilo_fruits = float(input())
vegetables = price_vegetables * price_per_kilo_vegetables
fruits = price_fruits * price_per_kilo_fruits

total_price_in_euro = (vegetables + fruits) / 1.94
print(f"{total_price_in_euro:.2f}")
