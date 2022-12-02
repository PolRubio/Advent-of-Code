entrada = open("input", "r")
avion = []
grupo = ""
longitud = 0

for persona in entrada:
  if persona == '\n':
      avion.append(grupo)
      print(grupo)
      grupo = ""
  
  else:
    for pregunta in persona:
      if pregunta not in grupo and pregunta != '\n':
        grupo += pregunta

avion.append(grupo)

print(avion)

for grupo in avion:
    longitud += len("".join(set(grupo)))

print(longitud)
                
    
          
