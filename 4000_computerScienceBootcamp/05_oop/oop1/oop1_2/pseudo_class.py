def person_init(name, money):
	obj = {'name': name, 'money': money}
	obj['give_money'] = Person[1]
	obj['get_money'] = Person[2]
	obj['show'] = Person[3]
	return obj


def give_money(self, other, money):
	self['money'] -= money
	other['get_money'](other, money)


def get_moeny(self, money):
	self['money'] += money


def show(self):
	print(f"{self['name']} : {self['money']}")


Person = person_init, give_money, get_moeny, show


if __name__ == '__main__':

	g = Person[0]('greg', 5000)
	j = Person[0]('john', 2000)

	g['show'](g)
	j['show'](j)
	print('')

	g['give_money'](g, j, 2000)
	g['show'](g)
	j['show'](j)