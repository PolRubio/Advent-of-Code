import numpy as np
with open("input.txt") as f: raw=f.read()

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

priorities = 0

for g in groups:
    print(g)
    a = np.array([l for l in g[0]])
    b = np.array([l for l in g[1]])
    c = np.array([l for l in g[2]])
    abc = np.intersect1d(np.intersect1d(a,b),c)
    print(abc)
    priorities += np.sum([priority[i] for i in abc])

# print(groups)

priorities = sum([priority[i] for i in np.intersect1d(np.intersect1d(np.array([l for l in g[0]]), np.array([l for l in g[1]])), np.array([l for l in g[2]])) for g in groups])

# priorities = sum(np.sum([priority[n] for n in np.intersect1d(np.array([j for j in i])[:int(len(i)/2)], np.array([j for j in i])[int(len(i)/2):])]) for i in raw.splitlines())

print(priorities)