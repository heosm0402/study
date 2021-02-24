from abc import *


class Character(metaclass = ABCMeta):
    def __init__(self, n, hp, p):
        self.name = n
        self.hp = hp
        self.power = p


    @abstractmethod
    def attack(self, other, attack_kind):
        pass


    @abstractmethod
    def get_damage(self, power, attack_kind):
        pass


    def __str__(self):
        return f"{self.name} : {self.hp}"


class Player(Character):
    def __init__(self, name='player', hp=100, power=10, *attack_kinds):
        super().__init__(name, hp, power)
        self.skills = []

        for attack_kind in attack_kinds:
            self.skills.append(attack_kind)


    def attack(self, other, attack_kind):
        if attack_kind in self.skills:
            other.get_damage(self.power, attack_kind)


    
    def get_damage(self, power, attack_kind):

        if attack_kind in self.skills:
            self.hp -= (power//2)
        else:
            self.hp -= power


class Monster(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)
        self.attack_kind = 'None'


    def attack(self, other, attack_kind):
        if self.attack_kind == attack_kind:
            other.get_damage(self.power, attack_kind)

    
    def get_damage(self, power, attack_kind):
        if self.attack_kind == attack_kind:
            self.hp += power
        else:
            self.hp -= power


    def get_attack_kind(self):
        return self.attack_kind

    
class IceMonster(Monster):
    def __init__(self, name = 'Ice Monster', hp = 50, power = 10):
        super().__init__(name, hp, power)
        self.attack_kind = 'ICE'

class FireMonster(Monster):
    def __init__(self, name='Fire Monster', hp = 50, power = 20):
        super().__init__(name, hp, power)
        self.attack_kind = 'FIRE'


    def fireball(self):
        print('fireball')


if __name__ == "__main__":
    player = Player('sword master', 100, 30, 'ICE')
    print(player.__dict__)
    print()
    monsters = []
    monsters.append(IceMonster())
    monsters.append(FireMonster())

    for mon in monsters:
        print(mon)
    print()

    for mon in monsters:
        player.attack(mon, 'ICE')

    print('after the player attacked')

    for mon in monsters:
        print(mon)
    print()

    print(player)

    for mon in monsters:
        mon.attack(player, mon.get_attack_kind())

    print('after monsters attacked')
    print(player)




