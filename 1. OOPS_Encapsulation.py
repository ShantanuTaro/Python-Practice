class Bank:
    def __init__(self):
        self.__balance = 20000

    def account_balance(self):
        return self.__balance

    def credit(self, credit_amount):
        self.__balance += credit_amount

    def debit(self, debit_amount):
        if self.__balance - debit_amount < 0:
            print("Not enough balance!!")
        else:
            self.__balance -= debit_amount

cashier = Bank()
credit = cashier.credit(15000)
debit = cashier.debit(1000)
balance = cashier.account_balance()

print(balance)
