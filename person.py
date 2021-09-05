# Os dados solicitados são: nome completo, data de nascimento, contato telefônico e/ou e-mail para todos os cadastrados. 
# Acrescente de 3 a 5 informações que julgue ser relevantes para cada categoria. 
# Exemplo: Atendidos - CPF, RG, renda familiar, número de filhos, nome e idade de cada filho, se o filho frequenta escola, se desempregado, 
# quanto tempo desde o último emprego formal, etc.

class Person():
    def __init__(self, name, birth, number = "", email = ""):
        self.name = name
        self.birth = birth
        self.number = number
        self.email = email
        self.categories = []