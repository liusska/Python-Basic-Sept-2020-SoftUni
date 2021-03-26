flour_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
eggs_quantity = int(input())
yeast_pack = int(input())

flour = flour_kg * flour_price
sugar = sugar_kg * (flour_price * 0.75)
eggs = eggs_quantity * (flour_price * 1.10)
yeast = (flour_price * 0.75) * 0.20 * yeast_pack

total = flour + sugar + eggs + yeast
print(f"{total:.2f}")

