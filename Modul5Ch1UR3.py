class warrior:
    def __init__(self, name, hp, hit):
        self.name = name 
        self.hp = hp 
        self.hit = hit 
    def beats(self, unit):
        unit.hp -= self.hit
        if unit.hp > 0:
            print(f'"{self.name}" атаковал "{unit.name}". У "{unit.name}" осталось {unit.hp} здоровья')
        else:
            print(f'"{self.name}" атаковал "{unit.name}". "{unit.name}" убит')
            unit.hp = 0
        return unit.hp
 
from random import randint as rnd
 
unit = warrior('Maewa', 100, 20)
unit2 = warrior('Furia', 100, 20)
units = [unit, unit2]
 
while True:
    attack_index = rnd(0, 1)
    prot_index = (attack_index + 1)%2
    prot_hp = units[attack_index].beats(units[prot_index])
    if prot_hp == 0:
        print(f'"{units[attack_index].name}" Победил!')
        break

