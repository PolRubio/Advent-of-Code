f = open("input.txt", "r")
x = []
for i in f:
  x.append(i.replace('\n',''))

n=0
m=0

for y in x:
    if(y != ""):
        n += int(y)
    
    elif(m<n):
        m = n
        n = 0
    else:
        n = 0

print(m)