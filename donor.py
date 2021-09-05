class Donor():
    def __init__(self, cpf, rg):
        self.type = "Donor"
        self.cpf = cpf
        self.rg = rg
        self.donation_history = []