import json 

with open('person.json', 'r') as arquivo:
    info = json.load(arquivo)
    
print(info)