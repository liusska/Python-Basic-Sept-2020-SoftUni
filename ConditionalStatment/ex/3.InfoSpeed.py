speed = float(input())

if speed <= 10:
    print("slow")
elif speed > 10:
    if speed <= 50:
        print("average")
    else:
        if speed <= 150:
            print("fast")
        elif speed <= 1000:
            print("ultra fast")
        else:
            print("extremely fast")