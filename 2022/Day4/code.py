import numpy as np
with open("input.txt") as f: raw=f.read()

suchpairs = 0

for p in raw.splitlines():
    n = [int(y) for x in p.split(',') for y in x.split("-")]
    if n[0] >= n[2] and n[1] <= n[3] or n[2] >= n[0] and n[3] <= n[1]:
        print(n)
        suchpairs += 1



print(suchpairs)
