g = open("input", "r")
x = []
for i in g:
  x.append(i.replace('\n',''))

h=0
f=0  

for i in range(len(x)):
  y = x[i].split(" ")

  if y[0] == "forward":
    f = f + int(y[1])
  elif y[0] == "down":
    h = h + int(y[1])
  else:
    h = h - int(y[1])

print(h)
print(f)
print(h*f)