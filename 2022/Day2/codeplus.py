f = open("input.txt", "r")
x = []
for i in f:
  x.append(i.replace('\n',''))

n=0
m=[0,0,0]

for y in x:
    if(y != ""):
        n += int(y)

    elif(m[0]<n):
        print(m)
        print(n)
        print()
        m[2] = m[1]
        m[1] = m[0]
        m[0] = n
        n = 0
    
    elif(m[1]<n):
        print(m)
        print(n)
        print()
        m[2] = m[1]
        m[1] = n
        n = 0
    
    elif(m[2]<n):
        print(m)
        print(n)
        print()
        m[2] = n
        n = 0

    else:
        n = 0

if(m[0]<n):
    print(m)
    print(n)
    print()
    m[2] = m[1]
    m[1] = m[0]
    m[0] = n
    n = 0

elif(m[1]<n):
    print(m)
    print(n)
    print()
    m[2] = m[1]
    m[1] = n
    n = 0

elif(m[2]<n):
    print(m)
    print(n)
    print()
    m[2] = n
    n = 0

print(m)
print(sum(m))
