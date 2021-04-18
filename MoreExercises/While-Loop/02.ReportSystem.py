target = int(input())
card = 0
card_count = 0
kesh = 0
kesh_count = 0
sells = 0

command = input()
while command != "End":
    first_transaction = int(command)
    second_transaction = int(input())
    if first_transaction <= 100:
        kesh += first_transaction
        sells += first_transaction
        kesh_count += 1
        print("Product sold!")
    else:
        print("Error in transaction!")
    if second_transaction >= 10:
        card += second_transaction
        sells += second_transaction
        card_count += 1
        print("Product sold!")
    else:
        print("Error in transaction!")
    if sells >= target:
        print(f"Average CS: {kesh / kesh_count:.2f}")
        print(f"Average CC: {card / card_count:.2f}")
        break
    command = input()

if command == "End":
    print("Failed to collect required money for charity.")
