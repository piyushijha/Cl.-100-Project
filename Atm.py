class Atm:
    def __init__(self, cardNumber, pinNumber):
      self.cardNumber = cardNumber
      self.pinNumber = pinNumber

    def CashWithdrawl(self): 
        print("Please enter the amount you wish to withdraw: ")

    def BalanceEnquiry(self): 
        print("Please enter your savings account/current account balance: ")

John = Atm(115670098, 0000)