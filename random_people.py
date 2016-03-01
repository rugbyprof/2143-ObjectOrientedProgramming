import json
import requests

people = []

for i in range(10):
    response = requests.get('http://api.randomuser.me/?nat=us&results=100')
    data = response.json()
    print(i)

    people.extend(data['results'])

fp = open('random_people.json', 'w')
print(len(people))

fp.write(json.dumps(people))

# with open('people.json') as data_file:    
#     data = json.load(data_file)

# pp = pprint.PrettyPrinter(depth=4)
# pp.pprint(data['results'])

# print(len(data['results']))
# for person in data['results']:
#     pp.pprint(person['user'])
#     print()