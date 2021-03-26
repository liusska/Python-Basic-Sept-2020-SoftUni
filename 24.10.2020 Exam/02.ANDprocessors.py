from math import floor

count_processors = int(input())
count_employees = int(input())
work_days = int(input())

work_hours_employees = count_employees * work_days * 8
processors_in_progress = floor(work_hours_employees / 3)

diff = abs(count_processors - processors_in_progress) * 110.10
if processors_in_progress < count_processors:
    print(f"Losses: -> {diff:.2f} BGN")
else:
    print(f"Profit: -> {diff:.2f} BGN")