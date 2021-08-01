myDictionary = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
myDictionary['size']

spam = {1234: 'Luggage combination', 42: 'The Answer'}

eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
ham = {'species': 'cat', 'name': 'Zophie', 'age': 8}

eggs == ham #true

'name' in eggs #true
'name' not in eggs #false

list(eggs.keys()) #['name', 'species', 'age']
list(eggs.values()) #['Zophie', 'cat', 'age']
list(eggs.items()) #[('name', 'Zophie'), ('species', 'cat'), ('age', 8)]
eggs.keys() #dict_keys(['name', 'species', 'age'])

for k in eggs.keys():
    print(k)

for v in eggs.values():
    print(v)

for k, v in eggs.items():
    print(k, v)

'cat' in eggs.values() #true

if 'color' in eggs:
    print(eggs['color'])

eggs.get('age', 0) #8
eggs.get('color', '') #second parameter if key doesn't exists
eggs.setdefault('color', 'orange') #if key color doesn't exists, create key and put default value as orange
