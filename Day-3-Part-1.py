import re
a=[]
def make_matrix(matrix):
    row=[]
    for i in range(1000):
        row=[]
        for j in range(1000):
            row.append('.')
        matrix.append(row)

make_matrix(a)

lines = []
with open("in.txt") as f:
    for line in f:
        lines.append(re.split('[@# ,:x\n,\t]', line)) #1,4,5,7,8

for i in range(len(lines)):
    for k in range (int(lines[i][4]), int(lines[i][4])+int(lines[i][7])):
        for l in range (int(lines[i][5]), int(lines[i][5])+int(lines[i][8])):
            if a[k][l] == '.':
                a[k][l] = "#"
            elif a[k][l] == '#':
                a[k][l] = 'X'
            elif a[k][l] == 'X':
                continue

count = 0
for i in range(len(a)):
    for j in range(len(a)):
        if (a[i][j] == 'X'):
            count +=1
print (count)
    
