locations = int(input())
gold = 0

for location in range(1, locations + 1):
    target_gold_per_day = float(input())
    days_location = int(input())
    for day in range(1, days_location + 1):
        gold_per_day = float(input())
        gold += gold_per_day

    average_gold = gold / days_location
    if average_gold >= target_gold_per_day:
        print(f"Good job! Average gold per day: {average_gold:.2f}.")
    else:
        print(f"You need {abs(target_gold_per_day - average_gold):.2f} gold.")
    gold = 0