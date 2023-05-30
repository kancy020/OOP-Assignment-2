from Materials import *
from abc import ABC, abstractclassmethod
'''
File: OOP-Assignment-2.py
Description: The assignment 2 comprises of creation of workshop crafting game, where you can create weapons, and enchantments. you can also disassemble
the weapons and enchantments.
Author: Christopher Kanaris
StudentID: 110352617
EmailID: kancy020
This is my own work as defined by the university's Academic Miscounduct Policy.
'''

'''The Workshop method is used to hold the lists of weapons, enchantments and materials, it also holds the display methods
which display all the contents of the list in it.
'''
class Workshop:
    def __init__(self):
        
        self.WeaponList = {}
        self.EnchantmentList = {}
        self.materialsList = {}
        
        
        
        self.materials = {Maple(), Oak(), Ash(), Bronze(), Iron(), Steel(), 
            Ruby(), Sapphire(), Emerald(), Diamond(), Amethyst(), Onyx()}
        
        
        self.weaponBlueprints = {   "Sword": [Steel(), Maple()],     
                                    "Shield": [Bronze(), Oak()],     
                                    "Axe": [Iron(), Ash()],     
                                    "Scythe": [Steel(), Ash()],     
                                    "Bow": [Oak(), Maple()],     
                                    "Wand": [Ash(), Oak()],     
                                    "Staff": [Bronze(), Maple()],     
                                    "Dagger": [Bronze(), Bronze()]
                                    } 
    
        self.enchantmentBlueprints = {     
                                 "Holy": [Diamond(), Diamond()],     
                                 "Lava": [Ruby(), Onyx()],     
                                 "Pyro": [Ruby(), Diamond()],     
                                 "Darkness": [Onyx(), Amethyst()],     
                                 "Cursed": [Onyx(), Onyx()],     
                                 "Hydro": [Sapphire(), Emerald()],     
                                 "Venomous": [Emerald(), Amethyst()],
                                }
    
    
    
     
    
    '''displays all the weapon listed in the dictionary, both displaying enchanted weapons or not enchanted weapons'''
    def displayWeapons(self):#test method 
        if WeaponList.enchanted == True:
            print("the" + self.WeaponList.keys() + "is imbued with a" + self.WeaponList.get(useEffect) + "." + Weapon.attack)
        else:
            print("the" + self.WeaponList.keys() + "is not enchanted. It deals" + Weapon.attack() )
    '''prints all enchatments in an enchantments list''' 
     
    def displayEnchantments(enchantmentBlueprints): #testmethod
        for enchantment in enchantmentBlueprints:
            print("A",enchantmentBlueprints.key , "enchantment is stored in the workshop" ) 
    
    '''prints material name and amount of material remaining'''
    def displayMaterials(self): #testmethod
                pass
           
    '''displays the weapons created with the damage calcuated'''
    def displayArmoury(weapon): #test method
        print("it deals", Weapon.calculateDamage, "damage")
     

'''abstract Crafter class created to pass through its methods of craft and disassemble. the forge and the enchanter will gain access to these abstract methods.
they will be overidden and have their own methods pass through.
'''    
class Crafter(ABC):
    pass
    '''abstract method pass down to forge and enchanter'''
    def craft():
        pass
    
    '''abstract method pass down to forge and enchanter'''
    def disassemble():
        pass

'''Forge class created, inheritated from the abstract Crafter class, the class is used to forge weapons weapons used from the craft method
and to disasemble the weapons used from the disassemble method'''
class Forge(Crafter):
    

    '''method pass down form the Crafter abstract class method, used to form weapons using material and weapon name'''
    def craft(weaponName, primaryMaterial, catalystMaterial): #test method

        weapon = Weapon(weaponName, None, primaryMaterial, catalystMaterial)
        return weapon

    
    '''disassemble method passed down from Crafter abstract class, used to delete item from weapon dictionary'''
    def disassemble(weaponName): #test method
        pass

'''The Enchanter has an init which holds the recipe dictionary used for when a a weapon wants imbued a enchantment into it, this applied through
the craft method of this enchanter class.'''
class Enchanter(Crafter):
    def __init__(self):
     self.recipes = {"Holy": "pulses a blinding beam of light",
                     "Lava": "melts the armour off an enemy",
                     "Pyro": "applies a devastating burning effect",
                     "Darkness": "binds the enemy in dark vines",             
                     "Cursed": "causes the enemy to become crazed",             
                     "Hydro": "envelops the enemy in a suffocating bubble",             
                     "Venomous": "afflicts a deadly, fast-acting toxin"} 
     
    '''method pass down form the Crafter abstract class method, used to form enchantments'''
    def craft():# test method
        pass
    '''disassemble method passed down from Crafter abstract class, used to delete item from enchantment dictionary'''
    def disassemble(): #test method
        pass
    '''enchant method take the wepaon and imbues it into the weapons through the weapons enchated attribute'''
    def enchant(): #test method
        pass

'''Weapon class has init of name damage and the two materials used to create the weapon inside of the weapon classed. with created getters and setters use d\
    to get the return result of specified information, accompanied with an  '''
class Weapon:
    def __init__(self,name, damage, primaryMaterial, catalystMaterial):
         self.__name = name
         self.__damage = damage
         self.__primaryMaterial = primaryMaterial
         self.__catalystMaterial = catalystMaterial
         self.__enchanted = None
         
    def getName(self):
        return self.__name
    
    def setName(self, weaponName):
        self.__name = weaponName
    
    name = property(getName, setName)
    
    
    def getDamage(self):
        return self.__damage
        
    
    def setDamage(self, damage):
        self.__damage = damage
    
    damage = property(getDamage, setDamage)
   
    def getEnchanted(self):
        return self.__enchanted
        
    def setEnchanted():
        pass
    
    enchanted = property(getEnchanted, setEnchanted)
    
    def getPrimaryMaterial(self):
        return self.__primaryMaterial
        
    primaryMaterial = property(getPrimaryMaterial)
    
    def getCatalystMaterial(self):
        return self.__catalystMaterial 
    
    catalystMaterial = property(getCatalystMaterial)
        
    def getEnchantment(self):    
        return self.__enchanted
    
    def setEnchantment():
        pass
    
    enchantment = property(getEnchantment, setEnchantment)
    
    '''calculateDamage, uses the two material classes and calulates each materials attributes for the final damage result'''
    def calculateDamage(self): # test method
         
        if self.__primaryMaterial == Wood and self.__catalystMaterial == Wood:
            return self.__primaryMaterial.strength + self.__catalystMaterial.strength
        
        elif self.__primaryMaterial == Metal and self.__catalystMaterial == Metal:
            return Metal.purity * Metal.purity + self.__catalystMaterial.strength * self.__catalystMaterial.purity
        
        elif self.__primaryMaterial.Materials(Wood) and self.__catalystMaterial.Materials(Metal):
            return self.__primaryMaterial.strength + self.__catalystMaterial.strength * self.__catalystMaterial.purity
        
        elif self.__primaryMaterial.Materials(Metal) and self.__catalystMaterial.Materials(Wood):
            return self.__catalystMaterial.strength * self.__catalystMaterial.purity + self.__primaryMaterial.strength
    
    '''attack method returns the calculatedDamage results and applies then in workshop displayArmoury'''
    def attack(calculateDamage): #test method
        return ("It deals", calculateDamage, "damage") 
    
    
    '''the Enchantment class holds a set of setters and getter, with init attributes as name, damage, effect, and the two material classes.
the enchanment is made from the recipes dictionary from enchater'''
class Enchantment:
    def __init__(self,enchantmentName, magicDamage, effect, primaryMaterial, catalystMaterial):
            self.__enchantmentName = enchantmentName
            self.__magicDamage = magicDamage
            self.__effect = effect
            self.__primaryMaterial = primaryMaterial
            self.__catalystMaterial = catalystMaterial
    
       
    def getEnchantmentName(self):
        return self.__enchantmentName
    
    enchantmentName = property(getEnchantmentName)  
    
    def getMagicDamage(self):
        return self.__magicDamage
    
    def setMagicDamage():
        pass
    
    magicDamage = property(getMagicDamage, setMagicDamage)
    
    def getEffect(self):
        return self.__effect
    
    def setEffect():
        pass
    
    effect = property(getEffect, setEffect)
    
    def getPrimaryMaterial(self):
        return self.__primaryMaterial 
        
    primaryMaterial = property(getPrimaryMaterial)
    
    def getCatalystMaterial(self):
        return self.__catalystMaterial
    
    catalystMaterial = property(getCatalystMaterial)
    
    '''calculateMagicDamage, uses the two material classes and calulates each materials magicPower for the final damage result'''
    def calculateMagicDamage(self): # test method
       
        return self.__primaryMaterial.magicPower + self.__catalystMaterial.magicPower
      
        
    '''useEffect is implemented on the displayArmoury section, pass throught he effect that relates to the enchantment'''       
    def useEffect(): #test method
        pass
    
    
