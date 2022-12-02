f = open("input", "r")
x = []
for i in f:
  x.append(int(i.replace('\n','')))
  
for i in x:
    for j in x:
        for z in x:
            if i + j + z == 2020:
                print(i, "+", j, "+", z, "=", i+j+z, "==>", i, "*", j, "*", z, "=", i*j*z)
