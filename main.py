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

print(people)

unsorted_people = []
for person in people:
    p = {
        "name": person.name,
        "birth": person.birth,
        "number": person.number,
        "email": person.email
    }
    unsorted_people.append(p)

with open('output/unsorted.json', 'w') as f:
    json.dump(unsorted_people, f)

people.sort(key=lambda person: (person.name, person.categories))

print(people)

sorted_people = []

for person in people:
    sorted_people.append(person.as_dictionary())

with open('output/sorted.json', 'w') as f:
    json.dump(sorted_people, f)