tax_per_year = int(input())

sneakers = tax_per_year * 0.60
outfit = sneakers * 0.80
ball = outfit / 4
accessories = ball / 5

total = sneakers + outfit + ball + accessories + tax_per_year
print(f"{total:.2f}")