import json

with open('allqs.json', encoding='utf-8') as f:
    data = json.load(f)

print(f'Total entries: {len(data)}')
print(f'1xxx (politica):      {len([q for q in data if 1000 <= q["id"] < 2000])}')
print(f'2xxx (derechos):      {len([q for q in data if 2000 <= q["id"] < 3000])}')
print(f'3xxx (geografia):     {len([q for q in data if 3000 <= q["id"] < 4000])}')
print(f'4xxx (cultura):       {len([q for q in data if 4000 <= q["id"] < 5000])}')
print(f'5xxx (practica):      {len([q for q in data if 5000 <= q["id"] < 6000])}')