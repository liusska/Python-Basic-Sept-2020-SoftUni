import sys

n = int(input())

OddSum = 0
OddMin = sys.maxsize
OddMax = - sys.maxsize
EvenSum = 0
EvenMin = sys.maxsize
EvenMax = - sys.maxsize


for i in range(0, n):
    num = float(input())
    if i % 2 == 0:
        if num > OddMax:
            OddMax = num
        if num < OddMin:
            OddMin = num
        OddSum += num
    else:
        if num < EvenMin:
            EvenMin = num
        if num > EvenMax:
            EvenMax = num
        EvenSum += num

print(f"OddSum={OddSum:.2f},")
if OddMin != sys.maxsize:
    print(f"OddMin={OddMin:.2f},")
else:
    print(f"OddMin=No,")
if OddMax != -sys.maxsize:
    print(f"OddMax={OddMax:.2f},")
else:
    print(f"OddMax=No,")

print(f"EvenSum={EvenSum:.2f},")

if EvenMin != sys.maxsize:
    print(f"EvenMin={EvenMin:.2f},")
else:
    print(f"EvenMin=No,")
if EvenMax != -sys.maxsize:
    print(f"EvenMax={EvenMax:.2f}")
else:
    print(f"EvenMax=No")
