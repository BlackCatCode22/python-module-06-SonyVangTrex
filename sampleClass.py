class PartyAnimal :

    def __init__(self)_:
        self.x = 0

    def party(self) :
        self.x = self.x + 1
        print("So far", self.x)

an = PartyAnimal()

an.party()
an.party()
an.party()

x = list()
type(x)

dir(x)
['_add_', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

y = 'Hello there'
dir(y)

class PartyAnimal :

    def __init__(self)_:
        self.x = 0

    def party(self) :
        self.x = self.x + 1
        print("So far", self.x)

an = PartyAnimal()

print("Type", type(an))
print("Dir ", dir(an))
print ("Type", type(an.x))
print ("Type", type(an.party))