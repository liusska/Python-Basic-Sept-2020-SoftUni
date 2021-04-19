students = int(input())
top = 0
good = 0
middle = 0
fail = 0
total = 0
for i in range(0, students):
    grade = float(input())
    total += grade
    if grade >= 5:
        top += 1
    elif 4 <= grade <= 4.99:
        good += 1
    elif 3 <= grade <= 3.99:
        middle += 1
    elif 2 <= grade <= 2.99:
        fail += 1

average = total / students
top_percent = top / students * 100
good_percent = good / students * 100
middle_percent = middle / students * 100
fail_percent = fail / students * 100
print(f"Top students: {top_percent:.2f}%")
print(f"Between 4.00 and 4.99: {good_percent:.2f}%")
print(f"Between 3.00 and 3.99: {middle_percent:.2f}%")
print(f"Fail: {fail_percent:.2f}%")
print(f"Average: {average:.2f}")


