class Account:
    num_account = 0


    @classmethod
    def get_num_account(cls):
        return cls.num_account

    
    def __init__(self, name, money):
        self.user = name
        self.balance = money
        Account.num_account += 1

    
    def deposit(self, money):
        if money < 0:
            return
        self.balance += money


    def withdraw(self, money):
        if money > 0 and money <= self.balance:
            self.balance -= money
            return money
        else:
            return None

    
    def transfer(self, other, money):
        mon = self.withdraw(money)

        if mon:
            other.deposit(money)
            return True
        else:
            return False

    
    def __str__(self):
        return f"user: {self.user}, balance: {self.balance}"


if __name__ == "__main__":
    my_account = Account('greg', 5000)
    your_account = Account('john', 2000)

    print('object created')
    print(my_account)
    print(your_account)
    print()


    my_account.deposit(500)

    print('deposit')
    print(my_account)
    print(your_account)
    print()

    print('Account memmer')
    print(Account.num_account)
    print()

    print('class method')
    n_acnt = Account.get_num_account()

    print(f"the number of accounts : {n_acnt}")
    print()

    print('message passing')
    print(my_account)
    print(your_account)

    res = my_account.transfer(your_account, 2000)
    if res:
        print('transfer succeeded')
    else:
        print('transfer failed')

    print(my_account)
    print(your_account)