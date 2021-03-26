team = input()
souvenir = input()
count_souvenirs = int(input())
price = 0

if team == "Argentina":
    if souvenir == "flags":
        price = 3.25
    elif souvenir == "caps":
        price = 7.20
    elif souvenir == "posters":
        price = 5.10
    elif souvenir == "stickers":
        price = 1.25
    else:
        print(f"Invalid stock!")
elif team == "Brazil":
    if souvenir == "flags":
        price = 4.20
    elif souvenir == "caps":
        price =8.50
    elif souvenir == "posters":
        price = 5.35
    elif souvenir == "stickers":
        price = 1.20
    else:
        print(f"Invalid stock!")
elif team == "Croatia":
    if souvenir == "flags":
        price = 2.75
    elif souvenir == "caps":
        price = 6.90
    elif souvenir == "posters":
        price = 4.95
    elif souvenir == "stickers":
        price = 1.10
    else:
        print(f"Invalid stock!")
elif team == "Denmark":
    if souvenir == "flags":
        price = 3.10
    elif souvenir == "caps":
        price = 6.50
    elif souvenir == "posters":
        price = 4.80
    elif souvenir == "stickers":
        price = 0.90
    else:
        print(f"Invalid stock!")
else:
    print("Invalid country!")

total_price = count_souvenirs * price

if price != 0:
    print(f"Pepi bought {count_souvenirs} {souvenir} of {team} for {total_price:.2f} lv.")