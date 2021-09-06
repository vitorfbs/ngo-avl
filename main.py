from re import search
from person import Person
from factory import Factory
from random import randrange
import json

factory = Factory()

people = []

for i in range(randrange(1, 20)):
    person = Person(
        factory.generate_random_text(),
        factory.generate_random_date(),
        factory.generate_random_number(),
        factory.generate_random_email()
    )

    person.add_category(
        factory.generate_new_category()
    )

    people.append(person)


unsorted_people = []
for person in people:
    unsorted_people.append(person.as_dictionary())

with open('output/unsorted.json', 'w') as f:
    json.dump(unsorted_people, f)

people.sort(key=lambda person: (person.name, person.categories))


sorted_people = []

for person in people:
    sorted_people.append(person.as_dictionary())

with open('output/people.json', 'w') as f:
    json.dump(sorted_people, f)

matches = []
for p in people:
    if p.search("a") == True:
        matches.append(p)

print(matches)