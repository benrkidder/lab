from account import Account


class Test_Account:
    def setup_method(self):
        self.a1 = Account('John')

    def teardown_method(self):
        del self.a1

    def test_init(self):
        # Test Account class initial state
        assert self.a1.get_name() == 'John'
        assert self.a1.get_balance() == 0

    def test_deposit(self):
        # Test deposit method of Account class
        assert self.a1.deposit(-1) is False
        assert self.a1.get_balance() == 0
        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == 0
        assert self.a1.deposit(1) is True
        assert self.a1.get_balance() == 1
        assert self.a1.deposit(0.1) is True
        assert self.a1.get_balance() == 1.1

    def test_withdrawal(self):
        # Test withdrawal method of Account class
        self.a1.deposit(100)

        assert self.a1.withdrawal(-1) is False
        assert self.a1.get_balance() == 100
        assert self.a1.withdrawal(0) is False
        assert self.a1.get_balance() == 100
        assert self.a1.withdrawal(100.1) is False
        assert self.a1.get_balance() == 100
        assert self.a1.withdrawal(1) is True
        assert self.a1.get_balance() == 99
        assert self.a1.withdrawal(0.1) is True
        assert self.a1.get_balance() == 98.9
        assert self.a1.withdrawal(98.9) is True
        assert self.a1.get_balance() == 0
