rest_days = int(input())

work_days = 365 - rest_days

time_for_games = work_days * 63 + rest_days * 127

if time_for_games > 30000:
    time_in_lot = time_for_games - 30000
    h = time_in_lot // 60
    m = time_in_lot % 60
    print("Tom will run away")
    print(f"{h} hours and {m} minutes more for play")
else:
    time = 30000 - time_for_games
    h = time // 60
    m = time % 60
    print("Tom sleeps well")
    print(f"{h} hours and {m} minutes less for play")
