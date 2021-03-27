number = float(input())
metric = input()
result_metric = input()

if metric == "mm":
    if result_metric == "m":
        number /= 1000
    if result_metric == "cm":
        number /= 10
elif metric == "m":
    if result_metric == "mm":
        number *= 1000
    if result_metric == "cm":
        number *= 100
elif metric == "cm":
    if result_metric == "mm":
        number *= 10
    if result_metric == "m":
        number /= 100

print(f"{number:.3f}")