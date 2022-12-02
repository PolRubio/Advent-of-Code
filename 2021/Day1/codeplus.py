from termcolor import colored

f = open("input", "r")
x = []
for i in f:
  x.append(int(i.replace('\n','')))

n=0  
i = 0

for i in range(len(x)-2):
    print(f"{i+65} - {chr(i%24+65)}: {x[i]+x[i+1]+x[i+2]}", end="")

    A = x[i-1]+x[i]+x[i+1]
    B = x[i]+x[i+1]+x[i+2]

    if i == 0:
        print(" (N/A - no previous sum)")
     
    elif B > A:
        print(colored(" (increased)", "red"))
        n += 1
    
    elif B < A:
        print(" (decreased)")
    
    else:
        print(" (no change)")
    
    i += 1

print(n)