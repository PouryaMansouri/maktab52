class Account:
    name: str
    balance_account: int
    minimum_balance: int
    __minimum_balance = 100

    def __init__(self, name: str, balance_account: int):
        self.__check_balance(balance_account)
        self.__balance_account = balance_account
        self.name = name

    def deposit(self, amount: int):
        # amount should be more than 1 and int
        assert amount > 1 and int(amount)
        self.__balance_account += amount
        return f"{self.name}: deposit complete and {amount}$ add to your account " \
               f"and new account balance is {self.__balance_account}"

    def withdraw(self, amount: int):
        # amount should be more than 1 and int
        assert amount > 1 and int(amount)
        self.__check_balance(self.__balance_account - amount)
        self.__balance_account -= amount
        return f"{self.name}: withdraw complete and {amount}$ decrease from your account " \
               f"and new account balance is {self.__balance_account}"

    def __repr__(self):
        return f"{self.name} has {self.__balance_account}$ in account"

    # @staticmethod
    # def __check_balance(amount):
    #     if amount >= __minimum_balance:
    #         raise Exception("You hove not enough account balance to withdraw this amount")

    def __check_balance(self, amount):
        if amount <= self.__class__.__minimum_balance:
            raise Exception("You hove not enough account balance")

    # TODO: better way to return result
    def transaction(self, account, amount):
        r = ''
        r += self.withdraw(amount) + '\n'
        r += account.deposit(amount)
        return r


pourya = Account("Pourya", 200)
ali = Account("Ali", 700)

print(pourya)
print(pourya.deposit(300))
print(pourya)
print(pourya.withdraw(100))
print(pourya)
print()
print(ali)
print()
print(ali.transaction(pourya, 400))
print(ali.transaction(pourya, 9000))
