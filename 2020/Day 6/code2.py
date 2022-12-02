entrada = open("input", "r")
avion = []
grupo = []
longitud = 0
temp = ""

for persona in entrada:
    if persona == '\n':
      avion.append(grupo[-1])
      grupo = []
  
    elif grupo == []:
      grupo.append(persona.replace('\n', ''))
      
    else:
        for pregunta in persona:
            if pregunta in grupo[-1] and pregunta != '\n':
                temp += pregunta
    
        grupo.append(temp)
        temp = ""

avion.append(grupo[-1])

# print(avion)

for grupo in avion:
    longitud += len("".join(set(grupo)))

print(longitud)
                