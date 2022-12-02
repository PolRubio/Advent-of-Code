f = open("input", "r")
x = []
for i in f:
  x.append(int(i.replace('\n','')))

n=0  
for i in range(len(x)):
  print(x[i])
  
  if i == 0:
    print(" (N/A - no previous measurement)\n")
  
  elif x[i] > x[i-1]:
    print(" (increased)\n")
    n += 1

  elif x[i] == x[i-1]:
    print(" (equal)\n")
  
  else:
    print(" (decreased)\n")

print(n)