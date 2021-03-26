type_fuel = input()
quantity_fuel = float(input())
card = input()

price_gasoline = 2.22
price_diesel = 2.33
price_gas = 0.93
total = 0

if type_fuel == "Gas":
    if card == "Yes":
        total = (quantity_fuel * price_gas) - (0.08 * quantity_fuel)
    else:
        total = (quantity_fuel * price_gas)
elif type_fuel == "Gasoline":
    if card == "Yes":
        total = (quantity_fuel * price_gasoline) - (0.18 * quantity_fuel)
    else:
        total = (quantity_fuel * price_gasoline)
elif type_fuel == "Diesel":
    if card == "Yes":
        total = (quantity_fuel * price_diesel) - (0.12 * quantity_fuel)
    else:
        total = (quantity_fuel * price_diesel)

if 20 <= quantity_fuel <= 25:
    total *= 0.92
elif quantity_fuel > 25:
    total *= 0.90

print(f"{total:.2f} lv.")