# Os dados solicitados são: nome completo, data de nascimento, contato telefônico e/ou e-mail para todos os cadastrados. 
# Acrescente de 3 a 5 informações que julgue ser relevantes para cada categoria. 
# Exemplo: Atendidos - CPF, RG, renda familiar, número de filhos, nome e idade de cada filho, se o filho frequenta escola, se desempregado, 
# quanto tempo desde o último emprego formal, etc.
from atendee import Atendee
from donor import Donor
from employee import Employee
class Person():
    def __init__(self, name, birth, number = "", email = ""):
        self.name = name
        self.birth = birth
        self.number = number
        self.email = email
        self.categories = []

    def add_category(self, category):
        if category["type"] == "atendee":
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
                    print("Person registered as Atendee")

        elif category["type"] == "donor":
            pass
        elif category["type"] == "employee":
            pass
        elif category["type"] == "visitor":
            pass
        elif category["type"] == "volunteer":
            pass
        else:
            pass

    def as_dictionary(self):
        return {
            "name": self.name,
            "birth": self.birth,
            "number": self.number,
            "email": self.email,
            "categories": self.categories_as_dictionary()

        }

    def categories_as_dictionary(self):
        categories = []
        for category in self.categories:
            categories.append(category.__dict__)
        return categories