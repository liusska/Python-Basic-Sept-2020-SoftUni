from math import floor

hours_needed = int(input())
days_in_firm = int(input())
workers_overtime = int(input())

days_real = 0.90 * days_in_firm
days_in_hours = days_real * 8
overtime = workers_overtime * days_in_firm * 2
total_hours = floor(days_in_hours + overtime)

if total_hours >= hours_needed:
    print(f"Yes!{total_hours - hours_needed} hours left.")
else:
    print(f"Not enough time!{hours_needed - total_hours} hours needed.")