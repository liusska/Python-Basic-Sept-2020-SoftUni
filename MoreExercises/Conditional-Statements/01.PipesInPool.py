v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

first_pipe = h * p1
second_pipe = h * p2
debits = first_pipe + second_pipe

full_percent = (debits / v) * 100

percent_first_pipe = (first_pipe / debits) * 100
percent_second_pipe = (second_pipe / debits) * 100

if debits <= v:
    print(f"The pool is {full_percent:.2f}% full. Pipe 1: {percent_first_pipe:.2f}%. Pipe 2: {percent_second_pipe:.2f}%.")
else:
    print(f"For {h} hours the pool overflows with {abs(v - debits):.2f} liters.")
