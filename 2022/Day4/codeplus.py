import numpy as np
with open("input.txt") as f: raw=f.read()

suchpairs = 0

for p in raw.splitlines():
    n = [int(y) for x in p.split(',') for y in x.split("-")]
    if n[1] >= n[2] and n[0] <= n[2] or n[3] >= n[0] and n[2] <= n[0]:
        print(n)
        suchpairs += 1



print(suchpairs)
