g = open("input2", "r")
x = []
for i in g:
  x.append(i.replace('\n',''))

coor = []
for i in range(len(x)):
  if i != 0: 
    coor.append(z)
  z = []
  y = x[i].split(" -> ")
  for j in range(len(y)):
      z.append(y[j].split(","))
      z[j][0] = int(z[j][0])
      z[j][1] = int(z[j][1])
coor.append(z)

m = [0,0]
for i in range(len(coor)):
  for j in range(len(coor[0])):
    if coor[i][j][0] > m[0]:
      m[0] = coor[i][j][0]
    if coor[i][j][1] > m[1]:
      m[1] = coor[i][j][1]

d = []
dd = []
for i in range(m[0]+1):
  if i != 0: 
    d.append(dd)
  dd = []
  for j in range(m[1]+1):
    dd.append('.')
d.append(dd)

# print(coor)
# for i in range(len(coor)):
#   for j in range(len(coor[0][0])):
#     if coor[i][0][j] > coor[i][1][j]:
#       coor[i][0][j], coor[i][1][j] = coor[i][1][j], coor[i][0][j]
# print(coor)

n = 0
for i in range(len(coor)):
  print(f"================ {i}:")
  if coor[i][0][0] == coor[i][1][0] or coor[i][0][1] == coor[i][1][1]:
    if coor[i][0][0] > coor[i][1][0]:
      coor[i][0][1] = coor[i][1][1]
    if coor[i][0][1] > coor[i][1][1]:
      coor[i][0][1] = coor[i][1][1]
    for j in range(coor[i][0][0], coor[i][1][0]+1):
      for k in range(coor[i][0][1], coor[i][1][1]+1):
        # print(j, " - ", k)
        if d[k][j] == '.':
          d[k][j] = 1
        elif d[k][j] == 1:
          d[k][j] = 2
          n = n + 1
        else:
          d[k][j] = d[k][j] + 1
  
  else:
    x = coor[i][0][0]
    xb =  coor[i][0][0] < coor[i][1][0]
    y = coor[i][0][1]
    yb = coor[i][0][1] < coor[i][1][1]

    print(f"{coor[i][1][0]} - {coor[i][1][1]}")
    print(f"{xb} - {yb}")

    while x != coor[i][1][0]+1:
      print(f"{x} - {y}")
      
      if d[y][x] == '.':
        d[y][x] = 1
      elif d[y][x] == 1:
        d[y][x] = 2
        n = n + 1
      else:
        d[y][x] = d[y][x] + 1
      
      # for j in range(len(d)):
      #   for k in range(len(d[0])):
      #     print(d[j][k], end=" ")
      #   print()

      print()
      
      if xb:
        x = x + 1
      else:
        x = x - 1
      
      if yb:
        y = y + 1
      else:
        y = y - 1

# print(coor)
# print(d)
for j in range(len(d)):
  for k in range(len(d[0])):
    print(d[j][k], end=" ")
  print()
print(m)
print(n)
 