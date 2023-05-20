import Materi
from abc import ABC, abstractclassmethod
class Workshop:
     
    
    #displays weapon, use if to see if value == to enchated opr not enchanted weapon
    def displayWeapons():
        
    
    #prints all enchatments in an enchantments list   
    def displayEnchantments(enchantmentBlueprints):
        enchantmentBlueprints = {"Holy": [Diamond(), Diamond()],     
                             "Lava": [Ruby(), Onyx()],     
                             "Pyro": [Ruby(), Diamond()],     
                             "Darkness": [Onyx(), Amethyst()],     
                             "Cursed": [Onyx(), Onyx()],     
                             "Hydro": [Sapphire(), Emerald()],     
                             "Venomous": [Emerald(), Amethyst()]} 
    
    
    #prints material name and amount of material remaining
    def displayMaterials():
     
#is an abstract class    
class Crafter(ABC):
    pass

    #crafting method for forge and enchanter(add weapon or enchantment to list)
   
    def craft(self):
        pass
    
    #disassemble method for forge and enchanter(removes weapon or enchantment from list)
    def disassemble(self):
        pass

class Enchanter(Crafter):
    def __init__(self):
     self.recipes = {"Holy": "pulses a blinding beam of light",
                     "Lava": "melts the armour off an enemy",
                     "Pyro": "applies a devastating burning effect",
                     "Darkness": "binds the enemy in dark vines",             
                     "Cursed": "causes the enemy to become crazed",             
                     "Hydro": "envelops the enemy in a suffocating bubble",             
                     "Venomous": "afflicts a deadly, fast-acting toxin"} 
     
     
     
    # copy dictionary from assignment sheet
    
    #crafting method for forge and enchanter(add weapon or enchantment to list)
    def craft(recipes):
        
        
    
    #disassemble method for forge and enchanter(removes weapon or enchantment from workshop)
    def disassemble():
        
    
    def enchant(weaponName, enchantmentName, enchantment):
        

class Forge(Crafter):
        pass

    #crafting method for forge and enchanter(add weapon or enchantment to list)
    def craft():
        pass
    
    #disassemble method for forge and enchanter(removes weapon or enchantment from list)
    def disassemble():
        pass

# uses mateirla to craft
class Enchantment:
    def __init(self,name, magicDamage, effect, primaryMaterial, catalystMaterial):
            self.__name = name
            self.__magicDamage = magicDamage
            self.__effect = effect
            self.__primaryMaterial = primaryMaterial
            self.__secondaryMaterial = catalystMaterial
            
    def getEnchantmentName():
        pass
    
    def getMagicDamage():
        pass
    
    def setMagicDamage():
        pass
    
    def getEffect():
        pass
    
    def setEffect():
        pass
    
    def getPrimaryMaterial():
        pass
        
    def getSecondaryMaterial(materials):
        

    def calculateMagicDamage(materials):
        pass
            
    def useEffect():
        pass
            
    #property to be made for each
            
    pass

class Weapon:
    def __init__(self,name, damage, primaryMaterial, catalystMaterial):
         self.__name = name
         self.__damage = damage
         self.__primaryMaterial = primaryMaterial
         self.__secondaryMaterial = catalystMaterial
         self.__enchanted = None
         
         
         
         
    # get weapon name  
    def getName(name):
        return name
    
    def setName():
        pass
    
    #get damage rating of weapon
    def getDamage():
        pass
    
    def setDamage():
        pass
    
    #do a boolean to see if it is enchated
    def getEnchanted():
        pass
    
    def setEnchanted():
        pass
    
    def getPrimaryMaterial():
        pass
        
    def getSecondaryMaterial():
        pass
    
    #prints the attached enchantment to the weapon
    def getEnchantment():    
        pass
    
    def setEnchantment():
        pass
    
    
    #check type fo materials that the weapon is made out of, and returns in a float what  thwe weapon damage is
    def calculateDamage():
        pass
    
    def attack():
        pass
    #property to be made for each
    

weaponBlueprints = {"Sword": [Steel(), Maple()], 
                    "Shield": [Bronze(), Oak()], 
                    "Axe": [Iron(), Ash()], 
                    "Scythe": [Steel(), Ash()],
                    "Bow": [Oak(), Maple()],
                    "Wand": [Ash(), Oak()],
                    "Staff": [Bronze(), Maple()],
                    "Dagger": [Bronze(), Bronze()]} 

materials = [Maple(), Oak(), Ash(), Bronze(), Iron(), Steel(), 
             Ruby(), Sapphire(), Emerald(), Diamond(), Amethyst(), Onyx()] 