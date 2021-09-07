from person_tree import PersonTree
from re import search
from person import Person
from factory import Factory
from random import randrange
import json

factory = Factory()


# 1. Fazer o cadastro das pessoas para a ONG. (recomendamos em JAVA, mas Python também é uma opção caso queira), 
# separando os envolvidos em cinco categorias (atributos do registro): 
# Funcionários, Voluntários, Doadores, Atendidos e Visitantes. Uma pessoa pode pertencer a mais de uma categoria, 
# no entanto, os Atendidos não podem ser doadores ou funcionários.
# Os dados solicitados são: nome completo, data de nascimento, contato telefônico e/ou e-mail para todos os cadastrados. 
# Acrescente de 3 a 5 informações que julgue ser relevantes para cada categoria. 
# Exemplo: Atendidos - CPF, RG, renda familiar, número de filhos, nome e idade de cada filho, se o filho frequenta escola, se desempregado, 
# quanto tempo desde o último emprego formal, etc.

people = []

for i in range(randrange(1, 20)):
    person = Person(
        factory.generate_random_text(),
        factory.generate_random_date(),
        factory.generate_random_number(),
        factory.generate_random_email()
    )

    for i in range(randrange(1,5)):
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

# 2. Ao fazer isso, você deve implementar métodos de busca desses cadastros 
# dentro de um Array ou lista usando recursão/ laço;
matches = []
for p in people:
    print(p.category_list())
    if p.search("a") == True:
        matches.append(p)

print(matches)

# 3. Armazenar os dados em uma AVL, ordenado pelo nome e categoria, a fim de permitir a 
# consulta de uma determinada pessoa. 
# Assim, sempre que realizar a busca na AVL (pelo nome), contar e apresentar quantas comparações 
# foram necessárias, ou seja, ao buscar as pessoas de uma categoria específica, 
# uma lista de nomes em ordem alfabética deve ser gerada (percurso de árvore).

# 4. Ordenar o arquivo de registros (usando algum método de ordenação) para que os primeiros 
# registros em um dia de atividade sejam os primeiros a serem atendidos. 
# Portanto, o critério de ordenação deve ser: colocar nas primeiras posições do Array 
# os registros dos atendidos e, em ordem crescente, 
# uma das informações que foi colocada como relevante no item 1.
person_tree = PersonTree()

root = None
for p in people:
    root = person_tree.insert(root, p)

print("Preorder traversal of the",
      "constructed AVL tree is")
person_tree.preOrder(root)
print()

root = person_tree.remove(root, people[0])

print("Preorder traversal of the",
      "constructed AVL tree is")
person_tree.preOrder(root)
print()