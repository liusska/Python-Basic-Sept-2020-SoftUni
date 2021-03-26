deposit_sum = float(input())
period = int(input())
percent = float(input())

result = deposit_sum + period * (((deposit_sum * percent) / 100) / 12)

print(float(result))
