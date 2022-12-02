f = open("input", "r")
x = []
for i in f:
  x.append(i.replace('\n',''))

id_master = 0
ids = []

for y in x:
    z = [0, 127]
    w = [0, 7]    
        
    for i in y[:-4]:
        if i == 'F':
            z[1] = int((z[0] + z[1])/2)
        else:
            z[0] = round((z[0] + z[1])/2)

    if y[6] == 'F':
        z[1] = z[0]
    else:
        z[0] = z[1]
        
    for i in y[-3:-1]:
        if i == 'L':
            w[1] = int((w[0] + w[1])/2)
        else:
            w[0] = round((w[0] + w[1])/2)
        
    if y[-1] == 'L':
        w[1] = w[0]
    else:
        w[0] = w[1]

    ids.append(z[0]*8 + w[0])
    
    if ids[-1] > id_master:
        id_master = ids[-1]
        
ids = sorted(ids)

def cualesmisitio(ids):
    for i in range(872):
        if ids[i] != i+63:
            return("PERO TU ERES GILIPOLLAS??? MENUDO SUBNORMAL ESTE ES TU ASIENTO ", i+63, ids[i])
        
print(cualesmisitio(ids))

print("id master: ", id_master)
print("ids:\n", sorted(ids))
print("length: ", len(ids))
        
