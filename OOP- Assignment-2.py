from abc import ABC 
import Materials

class Crafter(ABC):

    def craft():
        pass

    def disassemble():
        pass

class Weapon():
    def __init__(self, weaponName, material):
        self.weaponName = weaponName
        self.material = material
        
    def displayInfo(self):
        print('Weapon name is ' + self.weaponName +' material is', self.material.__class__.__name__, 'strength is', self.material.strength)
        
sword = Weapon('sword', Materials.Wood(5))   
anotherweapon = Weapon('bow', Materials.Metal(4,5))  
weapon = {}

weapon['weapon 2'] = anotherweapon
weapon['weapon 1'] = sword   

for name in weapon.keys():
    if name == 'weapon 1':
        print(name)