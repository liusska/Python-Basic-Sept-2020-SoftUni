city = input()
sales = float(input())
percent_of_sale = 0

if city == "Sofia":
    if 0 <= sales <= 500:
        percent_of_sale = sales * 0.05
    elif 500 < sales <= 1000:
        percent_of_sale = sales * 0.07
    elif 1000 < sales <= 10000:
        percent_of_sale = sales * 0.08
    elif sales > 10000:
        percent_of_sale = sales * 0.12
    else:
        print("error")
elif city == "Varna":
    if 0 <= sales <= 500:
        percent_of_sale = sales * 0.045
    elif 500 < sales <= 1000:
        percent_of_sale = sales * 0.075
    elif 1000 < sales <= 10000:
        percent_of_sale = sales * 0.10
    elif sales > 10000:
        percent_of_sale = sales * 0.13
    else:
        print("error")
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        percent_of_sale = sales * 0.055
    elif 500 < sales <= 1000:
        percent_of_sale = sales * 0.08
    elif 1000 < sales <= 10000:
        percent_of_sale = sales * 0.12
    elif sales > 10000:
        percent_of_sale = sales * 0.145
    else:
        print("error")
else:
    print("error")

if percent_of_sale != 0:
    print(f"{percent_of_sale:.2f}")
