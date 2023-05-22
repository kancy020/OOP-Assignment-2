from Materials import *
from abc import ABC, abstractclassmethod

class Workshop:
    def __init__(self):

   
        self.materials = {Maple(), Oak(), Ash(), Bronze(), Iron(), Steel(), 
            Ruby(), Sapphire(), Emerald(), Diamond(), Amethyst(), Onyx()}

        self.weapons = {}
    
        self.enchantment = {}
    
    
    
     
    
    #displays weapon, use if to see if value == to enchated opr not enchanted weapon
    def displayWeapons(self):
        if weapon.enchanted == True:
            print('the'+ self.weapons.keys() + ' is imbued with a' + self.weapons.get(useEffect) + '.' + Weapon.attack)
        
        else:
            print('the' + self.weapons.keys() + 'is not enchanted. It deals' + Weapon.attack )
        
    
    #prints all enchatments in an enchantments list   
    def displayEnchantments(enchantments):
        print('A', enchantments.name, 'enchantment is stored in the workshop' ) 
    
    
    #prints material name and amount of material remaining
    def displayMaterials(materials):
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
    
class Forge(Crafter):
    

    #crafting method for forge and enchanter(add weapon or enchantment to list)
    def craft(weaponName, primaryMaterial, catalystMaterial):

        weapon = Weapon(weaponName, None, primaryMaterial, catalystMaterial)
        return weapon

    
    #disassemble method for forge and enchanter(removes weapon or enchantment from list)
    def disassemble(weaponName):
        weaponBlueprints.pop(weaponName)
    
class Enchanter(Crafter):
    def __init__(self):
     self.recipes = {"Holy": "pulses a blinding beam of light",
                     "Lava": "melts the armour off an enemy",
                     "Pyro": "applies a devastating burning effect",
                     "Darkness": "binds the enemy in dark vines",             
                     "Cursed": "causes the enemy to become crazed",             
                     "Hydro": "envelops the enemy in a suffocating bubble",             
                     "Venomous": "afflicts a deadly, fast-acting toxin"} 
     
     

    
    #crafting method for forge and enchanter(add weapon or enchantment to list)
    def craft():
        pass
        
        
    
    #disassemble method for forge and enchanter(removes weapon or enchantment from workshop)
    def disassemble():
        pass
        
    
    def enchant():
        pass
        

# uses mateirla to craft
class Enchantment:
    def __init__(self,enchantmentName, magicDamage, effect, primaryMaterial, catalystMaterial):
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
        #if weapon is full wood 
        if self.__primaryMaterial.Materials(Wood) and self.__catalystMaterial.Materials(Wood):
            return ((self.__primaryMaterial.Materials(Wood).strength) + (self.__catalystMaterial.Materials(Wood).strength))
        #if weapon is full metal
        elif self.__primaryMaterial.Materials(Metal) and self.__catalystMaterial.Materials(Metal):
            return ((self.__primaryMaterial.Materials(Metal).strength * primaryMaterial.Materials(Metal).purity) + (self.__catalystMaterial.Materials(Metal).strength * catalystMaterial.Materials(Metal).purity))
        
        elif self.__primaryMaterial.Materials(Wood) and self.__catalystMaterial.Materials(Metal):
            return ((self.__primaryMaterial.Materials(Wood).strength) + (self.__catalystMaterial.Materials(Metal).strength * catalystMaterial.Materials(Metal).purity))
        
        elif self.__primaryMaterial.Materials(Metal) and self.__catalystMaterial.Materials(Wood):
            return ((self.__catalystMaterial.Materials(Metal).strength * catalystMaterial.Materials(Metal).purity) + (self.__primaryMaterial.Materials(Metal).strength))
        
            
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
    
    def setName(self, weaponName):
        self.__name = weaponName
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
    def calculateDamage(self):
        #if weapon is full wood 
        if self.__primaryMaterial.Materials(Wood) and self.__catalystMaterial.Materials(Wood):
            return ((self.__primaryMaterial.Materials(Wood).strength) + (self.__catalystMaterial.Materials(Wood).strength))
        #if weapon is full metal
        elif self.__primaryMaterial.Materials(Metal) and self.__catalystMaterial.Materials(Metal):
            return ((self.__primaryMaterial.Materials(Metal).strength * self.__primaryMaterial.Materials(Metal).purity) + (self.__catalystMaterial.Materials(Metal).strength * self.__catalystMaterial.Materials(Metal).purity))
        
        elif self.__primaryMaterial.Materials(Wood) and self.__catalystMaterial.Materials(Metal):
            return ((self.__primaryMaterial.Materials(Wood).strength) + (self.__catalystMaterial.Materials(Metal).strength * self.__catalystMaterial.Materials(Metal).purity))
        
        elif self.__primaryMaterial.Materials(Metal) and self.__catalystMaterial.Materials(Wood):
            return ((self.__catalystMaterial.Materials(Metal).strength * self.__catalystMaterial.Materials(Metal).purity) + (self.__primaryMaterial.Materials(Metal).strength))
    
    def attack(calculateDamage):
        return ('It deals', calculateDamage, 'damage') 
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