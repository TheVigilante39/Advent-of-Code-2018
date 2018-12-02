import os

a = []
b = []

with open('in2.txt') as f:
    for word in f:
        a.append(word)

for i in range (0,len(a)):
    for j in range (0, len(a)-1):
        count = 0
        for k in range (0, len(a[i])-1):
            if (a[i][k] == a[j][k]):
                count += 1
        if (len(a[i]) - count == 2):
            b.append(a[i])
            break

for i in range(0, len(b)):
    for j in range(0, len(b)):
        for k in range(0, len(b[i])):
            if(b[i][k] != b[j][k]):
                x = k
                y = b[i]

print(y[0:x] + y[x+1:])
