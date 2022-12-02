f = open("input", "r")
x = []
for i in f:
  x.append(i.replace('\n',''))

g = "" 
e = ""
for i in range(len(x[0])):
    u = 0
    z = 0 
    for j in range(len(x)):
        if x[j][i] == "1":
            u = u + 1
        else:
            z = z + 1

    if z > u:
        g = g + "0"
        e = e + "1"
    else:
        g = g + "1"
        e = e + "0"

print(g)
print(int(g, 2)*int(e, 2))