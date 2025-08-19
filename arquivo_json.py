import json

# Substitua 'seuarquivo.json' pelo nome do seu arquivo JSON
with open('seuarquivo.json', 'r', encoding='utf-8') as jsonfile:
    data = json.load(jsonfile)
    print(data)