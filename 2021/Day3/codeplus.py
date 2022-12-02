def fun(y, n, j):
    x = []
    for i in range(len(y)):
        if y[i][j] == n:
            x.append(y[i])
    
    return x

f = open("input", "r")
x = []
for i in f:
  x.append(i.replace('\n',''))

i = 0
o = x
while i < len(x[0]):
    u = 0
    z = 0 
    for j in range(len(o)):
        if o[j][i] == "1":
            u = u + 1
        else:
            z = z + 1

    if z > u:
      o = fun(o, "0", i)
    else:
      o = fun(o, "1", i)
    
    if len(o) == 1:
        i = len(x[0])
    else:
        i = i + 1

i = 0
c = x
while i < len(x[0]):
    u = 0
    z = 0
    for j in range(len(c)):
        if c[j][i] == "1":
            u = u + 1
        else:
            z = z + 1

    if z > u:
      c = fun(c, "1", i)
    else:
      c = fun(c, "0", i)
    
    if len(c) == 1:
        i = len(x[0])
    else:
        i = i + 1

print(o)
print(int(o[0], 2))
print(c)
print(int(c[0], 2))
print(int(o[0], 2)*int(c[0], 2))
