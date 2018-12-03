import os

count2 = 0
count3 = 0

def generate_arr(a):
    i = 97
    while (i != 123):
        a.append(word.count(chr(i)))
        i+=1

with open('input.txt') as f:
    for word in f:
        c2 = 0
        c3 = 0
        a = []
        generate_arr(a)
        for val in a:
            if (val == 2):
                c2+=1
            elif(val == 3):
                c3+=1
        if (c2 != 0 and c3 == 0):
            count2 += 1
        elif (c3 != 0 and c2 == 0):
            count3 += 1
        elif (c2!= 0 and c3!= 0):
            count2 += 1
            count3 += 1

print (count2*count3)
