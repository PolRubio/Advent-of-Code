g = open("input", "r")
x = []
for i in g:
  x.append(i.replace('\n',''))

h=0
f=0
a=0  

for i in range(len(x)):
  y = x[i].split(" ")

  if y[0] == "forward":
    f = f + int(y[1])
    h = h + a * int(y[1])
  elif y[0] == "down":
    a = a + int(y[1])
  else:
    a = a - int(y[1])

print(a)
print(h)
print(f)
print(h*f)