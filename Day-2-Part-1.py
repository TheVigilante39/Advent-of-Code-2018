import os

s = 0
found = False
a = [s]
while not found:
    with open('in.txt') as f:
        for x in f:
            s += int(x)
            if s in a:
                print(s)
                found = True
                break
            a.append(s)
