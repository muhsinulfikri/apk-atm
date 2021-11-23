from atm_card import ATMCard


class Customer:
    def __init__(self, id, custPin=1234, custBalance=10000):
        self.id = id
        self.custPin = custPin
        self.custBalance = custBalance

    def checkId(self):
        return self.id

    def checkPin(self):
        return self.custPin

    def checkBalance(self):
        return self.custBalance

    # proses debet dan simpan
    def withDrawBalance(self, nominal):
        self.custBalance -= nominal

    def depositBalance(self, nominal):
        self.custBalance += nominal
