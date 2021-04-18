command = input()
c = 0
o = 0
n = 0
word = ""
count = 0

while command != "End":
    if count == 2:
        break
    if "a" <= command <= "z" or "A" <= command <= "Z":
        if command == "c":
            if c > 0:
                word += command
            c += 1
        elif command == "o":
            if o > 0:
                word += command
            o += 1
        elif command == "n":
            if n > 0:
                word += command
            n += 1
        else:
            word += command

    if c > 0 and o > 0 and n > 0:
        count += 1
        print(word, end=" ")
        c = 0
        o = 0
        n = 0
        word = ""

    command = input()


print(word)