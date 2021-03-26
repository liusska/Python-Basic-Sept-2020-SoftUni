bitcoin = int(input())
chinese_uan = float(input())
percent = float(input())

bitcoin_in_leva = bitcoin * 1168
chinese_uan_in_dollars = chinese_uan * 0.15
chinese_uan_in_leva = chinese_uan_in_dollars * 1.76

total_in_leva = bitcoin_in_leva + chinese_uan_in_leva
total_in_euro = total_in_leva / 1.95

total_sum = total_in_euro * ((100 - percent) / 100)

print(f"{total_sum:.2f}")