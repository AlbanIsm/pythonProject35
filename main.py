class pub_mod:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def Age(self):
        print("Age:",self.age)
obj=pub_mod("Jason",35)
print("Name:",obj.name)
print("Age:",obj.age)

class details:
    _name="Alban"
    _age=24
    _job="Data Scientist"
class pro_mod(details):
    def __init__(self):
        print(self._name)
        print(self._age)
        print(self._job)

obj=pro_mod
print("Name:",obj._name)
print("Age:",obj._age)
print("Work:",obj._job)

