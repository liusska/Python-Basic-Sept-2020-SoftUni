price_skumria_per_kilo = float(input())
price_caca_per_kilo = float(input())
palamud_in_kilo = float(input())
safrid_in_kilo = float(input())
shels_in_kilo = float(input())

palamud_price_per_kilo = price_skumria_per_kilo * 1.60
safrid_price_per_kilo = price_caca_per_kilo * 1.80
price_shels = shels_in_kilo * 7.50

price_palamud = palamud_price_per_kilo * palamud_in_kilo
price_safrid = safrid_in_kilo * safrid_price_per_kilo
total = price_shels + price_safrid + price_palamud

print(f"{total:.2f}")