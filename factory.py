import random
import string
from datetime import date

class Factory():
    def __init__(self):
        pass

    def generate_random_text(self):
        letters = string.ascii_letters
        
        return ''.join(random.choice(letters) for i in range(10))
        
    def generate_random_email(self):
        letters = string.ascii_letters
        user = ''.join(random.choice(letters) for i in range(5))
        handle = ''.join(random.choice(letters) for i in range(5))
        return f"{user}@{handle}.com"

    def generate_random_number(self):        
        return ''.join(random.choice("1234567890") for i in range(9))

    def generate_random_date(self):
       return date.today().strftime("%d/%m/%Y")

    def generate_random_cpf(self):
        sequence_1 = ''.join(random.choice("1234567890") for i in range(3))
        sequence_2 = ''.join(random.choice("1234567890") for i in range(3))
        sequence_3 = ''.join(random.choice("1234567890") for i in range(3))
        sequence_4 = ''.join(random.choice("1234567890") for i in range(2))
        return f"{sequence_1}.{sequence_2}.{sequence_3}-{sequence_4}"

    def generate_random_rg(self):
        sequence_1 = ''.join(random.choice("1234567890") for i in range(2))
        sequence_2 = ''.join(random.choice("1234567890") for i in range(3))
        sequence_3 = ''.join(random.choice("1234567890") for i in range(3))
        
        return f"{sequence_1}.{sequence_2}.{sequence_3}"

    def generate_random_income(self):
        return ''.join(random.choice("1234567890") for i in range(4))

    def generate_random_date_list(self):
        dates = []
        
        for i in range(random.randrange(10)):
            dates.append(date.today().strftime("%d/%m/%Y"))
        
        return dates

    def generate_new_category(self):
        type = random.choice("12345")

        if type == "1":
            return self.generate_new_atendee()
        elif type == "2":
            return self.generate_new_donor()
        elif type == "3":
            return self.generate_new_employee()
        elif type == "4":
            return self.generate_new_visitor()
        else:
            return self.generate_new_volunteer()

    def generate_new_atendee(self):
        return {
            "type": "atendee",
            "cpf": self.generate_random_cpf(),
            "rg":  self.generate_random_rg(),
            "income": self.generate_random_income()
        }

    def generate_new_donor(self):
        return {
            "type": "donor",
            "cpf": self.generate_random_cpf(),
            "rg":  self.generate_random_rg(),
            "donation_history": self.generate_random_date_list()
        }
    
    def generate_new_employee(self):
        return {
            "type": "employee",
            "cpf": self.generate_random_cpf(),
            "rg":  self.generate_random_rg(),
            "job": self.generate_random_text(),
            "admission": self.generate_random_date(),
        }
    
    def generate_new_visitor(self):
        return {
            "type": "visitor",
            "cpf": self.generate_random_cpf(),
            "rg":  self.generate_random_rg(),
            "visit_date": self.generate_random_date(),
        }
    
    def generate_new_volunteer(self):
        return {
            "type": "volunteer",
            "cpf": self.generate_random_cpf(),
            "rg":  self.generate_random_rg(),
            "admission": self.generate_random_date(),
        }
