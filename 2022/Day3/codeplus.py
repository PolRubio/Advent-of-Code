import numpy as np
with open("input2.txt") as f: raw=f.read()

priority = {chr(i): i-ord('a')+1 for i in range(ord('a'), ord('z')+1)}
priority.update({chr(i): i-ord('A')+27 for i in range(ord('A'), ord('Z')+1)})



lines = [i for i in raw.splitlines()]

groups = []
group = []
cont  = 0

for l in lines:
    group.append(l)
    cont += 1
    if cont == 3:
        groups.append(group)
        group = []
        cont = 0

print(groups)

# points = sum(np.sum([puntuations[n] for n in np.intersect1d(np.array([j for j in i])[:int(len(i)/2)], np.array([j for j in i])[int(len(i)/2):])]) for i in raw.splitlines())

# print(points)