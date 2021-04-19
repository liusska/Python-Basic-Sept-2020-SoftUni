n = int(input())

first_sum = 0
mid_sum = 0
diff = 0
check = True

for i in range(0, n):
    num1 = int(input())
    num2 = int(input())
    if i % 2 != 0:
        first_sum = num1 + num2
    else:
        mid_sum = num1 + num2

    if first_sum == mid_sum or n < 2:
        check = True
    else:
        diff = abs(mid_sum - first_sum)
        check = False

if check:
    print(f"Yes, value={mid_sum}")
else:
    print(f"No, maxdiff={diff}")