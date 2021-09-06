class Donor():
    def __init__(self, cpf, rg, donation_history):
        self.type = "donor"
        self.cpf = cpf
        self.rg = rg
        self.donation_history = donation_history