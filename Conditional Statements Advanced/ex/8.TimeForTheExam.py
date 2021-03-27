exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time = exam_hour * 60 + exam_minute
arrival_time = arrival_hour * 60 + arrival_minute

difference = arrival_time - exam_time

state = ""
if difference < -30:
    state = "Early"
elif -30 <= difference <= 0:
    state = "On time"
else:
    state = "Late"

result = ""
if difference != 0:
    hour = abs(difference) // 60
    minute = abs(difference) % 60

    if hour > 0:
        if difference < 0:
            result = f"{hour}:{minute:02d} hours before the start"
        else:
            result = f"{hour}:{minute:02d} hours after the start"
    else:
        if difference < 0:
            result = f"{minute} minutes before the start"
        else:
            result = f"{minute} minutes after the start"

print(f"{state}")
if difference != 0:
    print(f"{result}")