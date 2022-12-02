def bingo(random, taul):
    for n in range(len(random)):
        for i in range(len(taul)):
            for j in range(len(taul[0])):
                for k in range(len(taul[0][0])):
                    if taul[i][j][k] == random[n]:
                        result[i][j][k] = True
                if testRow(result, i, j):
                     return finalScore(int(random[n]), taul, i)

def finalScore(n, taul, i):
    sum = 0
    for j in range(len(taul[0])):
        for k in range(len(taul[0][0])):
            if result[i][j][k] == False:
                sum = sum + int(taul[i][j][k])
    
    return n*sum

def testRow(result, i, j):
    for k in range(len(taul[0][0])):
        if result[i][j][k] == False:
            return False
    return True

f = open("input", "r")
x = []
for i in f:
  x.append(i.replace('\n',''))

random = x[0].split(',')

taul = []
rows = []
global result 
result = []
rowsR = []
rowsR2 = []
for i in range(2, len(x)):
    if x[i] == '':
        taul.append(rows)
        result.append(rowsR)
        rows = []
        rowsR = []
    else:
        rows.append(x[i].replace('  ', ' ').split(' '))
        if rows[-1][0] == '':
            del rows[-1][0]
        for i in range(len(rows[-1])):
            rowsR2.append(False)
        rowsR.append(rowsR2)
        rowsR2 = []

        

taul.append(rows)
result.append(rowsR)
print(bingo(random, taul))