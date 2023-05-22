from Materials import *
from abc import ABC, abstractclassmethod

class Workshop:

    enchantments = {}
    materials = {}
    weapons = {}
    
     
    
    #displays weapon, use if to see if value == to enchated opr not enchanted weapon
    def displayWeapons(weapon):
        if weapon.enchanted is True:
            print('the', weapon.name,' is imbued with a' , weapon.useEffect, '.', weapon.attack)
        
        else:
            print('the' + weapon.name, 'is not enchanted' )
        
    
    #prints all enchatments in an enchantments list   
    def displayEnchantments(enchantments):
        print('A', enchantments.name, 'enchantment is stored in the workshop' ) 
    
    
    #prints material name and amount of material remaining
    def displayMaterials():
        pass
    
    def displayArmoury(weapon):
        print('it deals', weapon.damage, 'damage')
     
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
    def craft():
        pass
        
        
    
    #disassemble method for forge and enchanter(removes weapon or enchantment from workshop)
    def disassemble():
        pass
        
    
    def enchant():
        pass
        

class Forge(Crafter):
        

    #crafting method for forge and enchanter(add weapon or enchantment to list)
    def craft(Crafter):
        pass
    
    #disassemble method for forge and enchanter(removes weapon or enchantment from list)
    def disassemble(Crafter):
        pass

# uses mateirla to craft
class Enchantment:
    def __init(self,enchantmentName, magicDamage, effect, primaryMaterial, catalystMaterial):
            self.__enchantmentName = enchantmentName
            self.__magicDamage = magicDamage
            self.__effect = effect
            self.__primaryMaterial = primaryMaterial
            self.__catalystMaterial = catalystMaterial
            
    def getEnchantmentName(self):
        return self.__enchantmentName
    
    def getMagicDamage(self):
        return self.__magicDamage
    
    def setMagicDamage():
        pass
    
    def getEffect(self):
        return self.__effect
    
    def setEffect():
        pass
    
    def getPrimaryMaterial(self):
        return self.__primaryMaterial 
        
    def getCatalystMaterial(self):
        return self.__catalystMaterial
        
    def calculateMagicDamage(self, primaryMaterial, catalystMaterial):
         return self.__primaryMaterial.magicPower + self.__catalystMaterial.magicPower
        
            
    def useEffect():
        pass
            
    #property to be made for each
            
    pass

class Weapon:
    def __init__(self,name, damage, primaryMaterial, catalystMaterial):
         self.__name = name
         self.__damage = damage
         self.__primaryMaterial = primaryMaterial
         self.__catalystMaterial = catalystMaterial
         self.__enchanted = None
         
         
         
         
    # get weapon name  
    def getName(self):
        return self.__name
    
    def setName(self, newName):
        self.__name = newName
        pass
    
    #get damage rating of weapon
    def getDamage(self, damage):
         return self.__damage
        
    
    def setDamage():
        pass
    
    #do a boolean to see if it is enchated
    def getEnchanted():
        pass
        
    def setEnchanted():
        pass
    
    def getPrimaryMaterial(self, primaryMaterial):
        return self.__primaryMaterial
        
    def getSecondaryMaterial(self, catalystMaterial):
        return self.__catalystMaterial 
        
    
    #prints the attached enchantment to the weapon
    def getEnchantment(self, enchanted):    
        return self.__enchanted
    
    def setEnchantment():
        pass
    
    
    #check type fo materials that the weapon is made out of, and returns in a float what  thwe weapon damage is
    def calculateDamage():
        pass
    
    def attack():
        pass
    #property to be made for each
    
weaponBlueprints = {     "Sword": [Steel(), Maple()],     
                             "Shield": [Bronze(), Oak()],     
                             "Axe": [Iron(), Ash()],     
                             "Scythe": [Steel(), Ash()],     
                             "Bow": [Oak(), Maple()],     
                             "Wand": [Ash(), Oak()],     
                             "Staff": [Bronze(), Maple()],     
                             "Dagger": [Bronze(), Bronze()]} 

enchantmentBlueprints = {     "Holy": [Diamond(), Diamond()],     
                              "Lava": [Ruby(), Onyx()],     
                              "Pyro": [Ruby(), Diamond()],     
                              "Darkness": [Onyx(), Amethyst()],     
                              "Cursed": [Onyx(), Onyx()],     
                              "Hydro": [Sapphire(), Emerald()],     
                              "Venomous": [Emerald(), Amethyst()]}

materials = [Maple(), Oak(), Ash(), Bronze(), Iron(), Steel(), 
             Ruby(), Sapphire(), Emerald(), Diamond(), Amethyst(), Onyx()] 