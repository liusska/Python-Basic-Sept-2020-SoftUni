days = int(input())
wins = 0
lose = 0
current_wins = 0
current_lose = 0
total_money = 0
money = 0


for i in range(0, days):
    command = input()
    while command != "Finish":
        game = command
        game_result = input()
        if game_result == "win":
            current_wins += 1
            money += 20
        else:
            current_lose += 1
        command = input()

    if current_wins > current_lose:
        money *= 1.10
        total_money += money
        wins += 1
    else:
        total_money += money
        lose += 1
    current_lose = 0
    current_wins = 0
    money = 0

if wins > lose:
    total_money *= 1.20
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
