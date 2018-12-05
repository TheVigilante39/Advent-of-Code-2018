import re
with open("input.txt") as f:
    a = f.read()
#------------------------------Part 1 Start --------------------------------
def func(a):
    i = 0
    while i < len(a)-1:
        if a[i] != a[i+1] and a[i].upper() == a[i+1].upper():
            a = a[:i]+a[i+2:]
            i = max(0, i-1)
        else:
            i += 1
    return a

print("Part 1: " + str(len(func(a))))
#------------------------------Part 1 End ----------------------------------

#------------------------------Part 2 Start --------------------------------
j = 97
y = []
while (j < 123):
    b = a
    b = re.sub(chr(j), '', b)
    b = re.sub(chr(j-32), '', b)
    y.append(len(func(b)))
    j+=1
print("Part 2: " + str(min(s for s in y)))
#------------------------------Part 2 End ----------------------------------
