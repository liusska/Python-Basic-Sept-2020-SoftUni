yard = float(input())
price_yard = float(yard * 7.61)
discount = float(price_yard * 0.18)
price = float(price_yard - discount)

print(f"The final price is: {price} lv.")
print(f"The discount is: {discount} lv.")