# Os dados solicitados são: nome completo, data de nascimento, contato telefônico e/ou e-mail para todos os cadastrados. 
# Acrescente de 3 a 5 informações que julgue ser relevantes para cada categoria. 
# Exemplo: Atendidos - CPF, RG, renda familiar, número de filhos, nome e idade de cada filho, se o filho frequenta escola, se desempregado, 
# quanto tempo desde o último emprego formal, etc.
from volunteer import Volunteer
from visitor import Visitor
from atendee import Atendee
from donor import Donor
from employee import Employee
import re
class Person():
    def __init__(self, name, birth, number = "", email = ""):
        self.name = name
        self.birth = birth
        self.number = number
        self.email = email
        self.categories = []

    def add_category(self, category):
        if category["type"] in self.category_list():
            print("Person already os the chosen category")

        elif category["type"] == "atendee":
            if any(isinstance(c, Donor) for c in self.categories):
                print("Atendee cannot be Donor")
            elif any(isinstance(c, Employee) for c in self.categories):
                print("Atendee cannot be Employee")
            else:
                atendee = Atendee(
                    category["cpf"],
                    category["rg"],
                    category["income"]
                )
                self.categories.append(atendee)

        elif category["type"] == "donor":
            if any(isinstance(c, Atendee) for c in self.categories):
                    print("Donor cannot be Atendee")
            else:
                donor = Donor(
                    category["cpf"],
                    category["rg"],
                    category["donation_history"],
                )
                self.categories.append(donor)
            
        elif category["type"] == "employee":
            if any(isinstance(c, Atendee) for c in self.categories):
                    print("Employee cannot be Atendee")
            else:
                employee = Employee(
                    category["cpf"],
                    category["rg"],
                    category["job"],
                    category["admission"],
                )
                self.categories.append(employee)
        
        elif category["type"] == "visitor":
            visitor = Visitor(
                    category["cpf"],
                    category["rg"],
                    category["visit_date"]
                )
            self.categories.append(visitor)
        
        elif category["type"] == "volunteer":
            volunteer = Volunteer(
                    category["cpf"],
                    category["rg"],
                    category["admission"]
                )
            self.categories.append(volunteer)

        else:
            print("Error while checking category type")

    def as_dictionary(self):
        return {
            "name": self.name,
            "birth": self.birth,
            "number": self.number,
            "email": self.email,
            "categories": self.categories_as_dictionary()

        }

    def as_dictionary_with_no_categories(self):
        return {
            "name": self.name,
            "birth": self.birth,
            "number": self.number,
            "email": self.email,
        }

    def categories_as_dictionary(self):
        categories = []
        for category in self.categories:
            categories.append(category.__dict__)
        return categories
        
    def category_list(self):
        categories_list = []
        for category in self.categories:
            categories_list.append(category.type)
        return categories_list

    def search(self, term):
        for k, v in self.as_dictionary().items():
            if term in v:
                return True
    
        for category in self.categories_as_dictionary():
            for k, v in category.items(): 
                if term in v:
                    return True
        return False

    def calculate_weight(self):
        weight = 0
        for category in self.categories_as_dictionary():
            if category["type"] == "atendee":
                weight += 100        
            elif category["type"] == "donor":
                weight += 4
            elif category["type"] == "visitor":
                weight += 3
            elif category["type"] == "volunteer":
                weight += 2
            elif category["type"] == "employee":
                weight += 1

        return weight