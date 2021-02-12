import json

with open('countries.json', 'r+', encoding='utf-8') as f:
    data = f.readlines()

print(len(data))
print(len(set(data)))

with open('countries_w_d.json', 'w', encoding='utf-8') as f:
    f.write('\n'.join(set(data)))