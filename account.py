class Account:
    '''
    A class representing details for a bank account object
    '''
    def __init__(self, name: str) -> None:
        '''
        Constructor to create initial state of an account object
        :param name: Account owner's name
        '''
        self.__account_name = name
        self.__account_balance: float = 0

    def deposit(self, amount: float) -> bool:
        '''
        Method to increase account balance if amount is valid.
        :param amount: Value added to account
        :return: Boolean value representing if deposit was successful or not
        '''
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdrawal(self, amount: float) -> bool:
        '''
        Method to decrease account balance if amount is valid.
        :param amount: Value subtracted from account
        :return: Boolean value representing if withdrawal was successful or not
        '''
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        '''
        Method to access account name.
        :return: Account Name
        '''
        return self.__account_balance

    def get_name(self) -> str:
        '''
        Method to access account balance.
        :return: Account Balance
        '''
        return self.__account_name


def main():
    account_one = Account('John')
    account_one.deposit(10)
    account_one.withdrawal(2)
    print(account_one.get_name())
    print(account_one.get_balance())


if __name__ == "__main__":
    main()
