f = open("input", "r")
x = []
for i in f:
  x.append(i.replace('\n',''))

def es_valid(i):
    num = 0
    
    if i[1] == "-":
        min = int(i[0])
        if i[3] == " ":
            max = int(i[2])
            let = i[4]
            text = i[7:]
        else:
            max = int(i[2:4])
            let = i[5]
            text = i[8:]
                      
    else:
        min = int(i[0:2])
        max = int(i[3:5])
        let = i[6]
        text = i[9:]
    
    #for t in text:
        #if t == let:
            #num += 1
    
    #print(min)
    #print(max)
    #print(let)
    #print(text)
    #print(num)
    
    #if min <= num and num <= max:
        #return 1
    #else:
        #return 0
    
    if text[min-1] == let and text[max-1] != let:
        return 1
    elif text[min-1] != let and text[max-1] == let:
        return 1
    else:
        return 0
    

valid_num = 0    
for i in x:
    valid_num += es_valid(i)
    
print(valid_num)
