class Person:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    
    def give_money(self, other, money):
        self.money -= money
        other.get_money(money)

    
    def get_money(self, money):
        self.money += money

    
    def show(self):
        print(f"{self.name} : {self.money}")


if __name__ == '__main__':
    greg = Person('greg', 5000)
    john = Person('john', 2000)

    greg.show()
    john.show()

    greg.give_money(john, 2000)

    print('')

    greg.show()
    john.show()

