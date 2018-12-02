s = 0
with open("in.txt") as f:
    for val in f:
        s += int(val)
print(s)
