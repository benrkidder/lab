class Account:
    def __init__(self, name):
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount):
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdrawal(self, amount):
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name


def main():
    account_one = Account('John')
    account_one.deposit(10)
    account_one.withdrawal(2)
    print(account_one.get_name())
    print(account_one.get_balance())


if __name__ == "__main__":
    main()
