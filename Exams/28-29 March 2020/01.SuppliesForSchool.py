pen = int(input())
markers = int(input())
clear = float(input())
percent = int(input())

pen_price = 5.80
markers_price = 7.20
clear_price = 1.20

total_pens = pen_price * pen
total_markers = markers * markers_price
total_clear = clear_price * clear

total_sum = total_pens + total_markers + total_clear
total = total_sum * ((100 - percent) / 100)

print(f"{total:.3f}")