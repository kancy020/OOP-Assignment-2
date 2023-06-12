from Materials import *
from abc import ABC, abstractclassmethod
#File: Assignment2.py
#Description: The assignment 2 comprises of the creation of a workshop crafting game, where you can create weapons, and enchantments. you can also disassemble
#the weapons and enchantments within given classes and methods.
#Author: Christopher Kanaris
#StudentID: 110352617
#EmailID: kancy020
#This is my own work as defined by the university's Academic Miscounduct Policy.

"""
A class which holds dictionaries for weapons, enchantments and materials whilst nesting forge and enchanter for testing code.

Attributes
----------
weapons : dictionary
    crafted weapons returned to dictionary.
enchantments : dictionary
    crafted weapons returned to the dictionary.
materials : dictionary
    materials listed in dictionary for crafting.
forge : string
    links Forge class in Workshop when running code.
enchanter : string
    Links Enchanter class in Workshop when running code.
"""
class Workshop:
    def __init__(self, forge, enchanter):
        
        self.weapons = []
        self.enchantments = []
        self.materials = {}
        self.forge = forge
        self.enchanter = enchanter
        
    """add material to specified material in dictionary."""
    def addMaterial(self, name, value):#test
      addMaterial = self.materials[name] = value
      return addMaterial
    
    """add weapon into weapons dictionary."""
    def addWeapon(self, weapon):#test
        self.weapons.append(weapon)
        return self.weapons
    
    """remove last imported weapon from weapons dictionary."""    
    def removeWeapon(self):#test
        pass
    
    """add enchantment into enchantments."""
    def addEnchantment(self, enchantment):#test
        self.enchantments.append(enchantment)
        return self.enchantments
    
    """remove last imported enchantment from enchantments."""
    def removeEnchantment(self):#test
        pass
        
    """displays all the weapon listed in the dictionary, both displaying enchanted weapons or non-enchanted weapons."""
    def displayWeapons(self):#test method
        weaponlist = ""
        if Weapon.getEnchanted == True:
            for weapon in self.weapons:
                self.weapons += f"The {enchantedWeapons[i]} is imbued with a {enchantment.useEffect}.\n"
            return  weaponlist
        else:
            weaponlist = ""
            for weapon in self.weapons:
                weaponlist += f"The {weapon} is not enchanted.\n"
            return weaponlist

            
        
    """prints all enchatments in an enchantments list."""
    def displayEnchantments(self): #testmethod
        enchantmentsList = ""
        for enchantment in self.enchantments:
            enchantmentsList += f"A {enchantment} enchantment is stored in the workshop.\n"
        return enchantmentsList 
        

    """prints material name and amount of material remaining."""
    def displayMaterials(self): #testmethod
        displayMaterials = ""    
        for material, value in sorted(self.materials.items(), key=lambda kv: kv[1], reverse=True):
           displayMaterials += f"{material}: {value} remaining.\n"
        return displayMaterials
        
    
"""
abstract Crafter class created to pass through its methods of craft and disassemble. the forge and the enchanter will gain access to these abstract methods.
they will be overidden and have their own methods pass through.

Attributes
----------
None.
""" 
class Crafter(ABC):
    pass

    '''abstract method pass down to forge and enchanter'''
    def craft():
        pass
    
    '''abstract method pass down to forge and enchanter'''
    def disassemble():
        pass


"""
Forge class created, inheritated from the abstract Crafter class, the class is used to forge weapons weapons used from the craft method
and to disasemble the weapons used from the disassemble method.

Attributes
----------
None.
"""
class Forge(Crafter):
    
    """method pass down form the Crafter abstract class method, used to update materials value and form weapons using material and weapon name."""
    def craft(self, name, primaryMaterial, catalystMaterial, materials): #test method
            craftedWeapon = Weapon(name, primaryMaterial, catalystMaterial)
            materials[primaryMaterial.__class__.__name__] -= 1
            materials[catalystMaterial.__class__.__name__] -= 1 
            return craftedWeapon
        
    """disassemble method passed down from Crafter abstract class method, used to update materials value and remove item from weapon dictionary."""
    def disassembles(self): #test method
            materials[primaryMaterial.__class__.__name__] += 1
            materials[catalystMaterial.__class__.__name__] += 1 
            
            
"""
The Enchanter has an init which holds the recipe dictionary used for when a a weapon wants imbued a enchantment into it, this applied through
the craft method of this enchanter class.

Attributes
----------
recipies : dictionary
    holds key of enchantment name and value of effect.
"""
class Enchanter(Crafter):
    def __init__(self):
     self.recipes = {"Holy": "pulses a blinding beam of light",
                     "Lava": "melts the armour off an enemy",
                     "Pyro": "applies a devastating burning effect",
                     "Darkness": "binds the enemy in dark vines",             
                     "Cursed": "causes the enemy to become crazed",             
                     "Hydro": "envelops the enemy in a suffocating bubble",             
                     "Venomous": "afflicts a deadly, fast-acting toxin"} 
     
    """method pass down from the Crafter abstract class method, used to form enchantments and remove and update mataerial value."""
    def craft(self, enchantmentName, primaryMaterial, catalystMaterial, materials):# test method
        
        for key in self.recipes.keys():
            craftedEnchantment = Enchantment(enchantmentName, primaryMaterial, catalystMaterial)
            key = enchantmentName
            if craftedEnchantment.enchantmentName == key:
                effect = self.recipes.get(key)
                craftedEnchantment.setEffect(effect)
                materials[primaryMaterial.__class__.__name__] -= 1
                materials[catalystMaterial.__class__.__name__] -= 1   
                return craftedEnchantment

    """disassemble method passed down from Crafter abstract class method, used to delete item from enchantment dictionary and update materials value."""
    def disassemble(): #test method
        return
        materials[primaryMaterial.__class__.__name__] += 1
        materials[catalystMaterial.__class__.__name__] += 1
        
    
    """enchant method take the weapon and imbues it into the weapons through the weapons enchanted attribute."""
    def enchant(self, weapon, enchantmentName, enchantment): #test method
        pass
        
                
        
        
"""
Weapon class has init of name damage and the two materials used to create the weapon inside of the weapon classed. with created getters and setters use d\
to get the return result of specified information, accompanied with an.

Attributes
----------
name : string
    name achieved via instansiated weapon.
damage : integar
    damage calculated by algorithm.
primaryMaterial : string
    string resulting from material class.
catalystMaterial : string
    string resulting from material class.
enchanted : boolean
    boolean updated by weapon values.
enchantment : string
    string resulted by imbued enchantment on string.
"""
class Weapon:
    def __init__(self, name, primaryMaterial, catalystMaterial):
         self.__name = name
         self.__damage = None
         self.__primaryMaterial = primaryMaterial
         self.__catalystMaterial = catalystMaterial
         self.__enchanted = False
         self.__enchantment = ""
           
    def getName(self):
        return self.__name
    
    def getDamage(self):
        return self.__damage
    
    def getEnchanted(self):
        return self.__enchanted
    
    def getPrimaryMaterial(self):
        return self.__primaryMaterial
    
    def getCatalystMaterial(self):
        return self.__catalystMaterial 
    
    def getEnchantment(self):    
        return self.__enchantment
    
    def setName(self, weaponName):
         self.__name = weaponName
        
    def setDamage(self, damage):
         self.__damage = damage
         return damage
 
    def setEnchanted(enchanted):
        if enchantment == "":
            pass
        else:
            return True
    
    def setEnchantment(self, enchantment):
        self.__enchantment = enchantment
        return enchantment
    
    gsName = property(getName, setName)
    gsDamage = property(getDamage, setDamage)
    gsEnchanted = property(getEnchanted, setEnchanted)
    gsPrimaryMaterial = property(getPrimaryMaterial)
    gsCatalystMaterial = property(getCatalystMaterial)
    gsEnchantment = property(getEnchantment, setEnchantment)
    
    """calculateDamage, uses the two material classes and calulates each materials attributes for the final damage result."""
    def calculateDamage(self): # test method
        
            if self.gsPrimaryMaterial == Material(Wood) and self.gsCatalystMaterial == Material(Wood):
                return self.gsPrimaryMaterial.strength * self.gsCatalystMaterial.strength
            
            elif self.gsPrimaryMaterial == Material(Metal) and self.gsCatalystMaterial == Material(Metal):
                return (self.gsPrimaryMaterial. strength * self.gsPrimaryMaterial.purity) + (self.gsCatalystMaterial.strength * self.gsCatalystMaterial.purity)
            
            elif self.gsPrimaryMaterial == Material(Wood) and self.gsCatalystMaterial == Material(Metal):
                return self.gsPrimaryMaterial.strength * (self.gsCatalystMaterial.strength * self.gsCatalystMaterial.purity)
            
            elif self.gsPrimaryMaterial == Material(Metal) and self.__catalystMaterial == Material(Wood):
                return (self.gsPrimaryMaterial.strength * self.gsPrimaryMaterial.purity) * self.gsCatalystMaterial.strength
            
    """attack method returns the calculatedDamage results and applies then in workshop displayArmoury."""
    def attack(self): 
        self.__damage = self.calculateDamage()
        return f"It deals {self.__damage} damage."
    
    
"""the Enchantment class holds a set of setters and getter, with init attributes as name, damage, effect, and the two material classes,
the enchanment is made from the recipes dictionary from enchater.

Attributes
----------
enchantmentName : string
    name achieved via instansiated enchantment.
magicDamage : integar
    damage calculated by algorithm.
effect : string
    effect resulted by values of key in enchantments.
primaryMaterial : string
    string resulting from material class.
catalystMaterial : string
    string resulting from material class.
"""
class Enchantment:
    def __init__(self, enchantmentName, primaryMaterial, catalystMaterial):
            self.__enchantmentName = enchantmentName
            self.__magicDamage = None
            self.__effect = ""
            self.__primaryMaterial = primaryMaterial
            self.__catalystMaterial = catalystMaterial
    
    def getEnchantmentName(self):
        return self.__enchantmentName
    
    def getMagicDamage(self):
        return self.__magicDamage
    
    def getEffect(self):
        return self.__effect
    
    def getPrimaryMaterial(self):
        return self.__primaryMaterial
    
    def getCatalystMaterial(self):
        return self.__catalystMaterial 
    
    def setMagicDamage():
        pass
    
    def setEffect(self, effect):
        self.__effect = effect
        return effect
        
        
    
    enchantmentName = property(getEnchantmentName)
    magicDamage = property(getMagicDamage, setMagicDamage)
    effect = property(getEffect, setEffect)
    primaryMaterial = property(getPrimaryMaterial)
    catalystMaterial = property(getCatalystMaterial)
    
    """calculateMagicDamage, uses the two material classes and calulates each materials magicPower for the final damage result"""
    def calculateMagicDamage(self): # test method
        return self.__primaryMaterial.magicPower + self.__catalystMaterial.magicPower
      
    """useEffect is implemented on the displayArmoury section, pass throught he effect that relates to the enchantment"""      
    def useEffect(self, enchantmentName, effect): #test method
        return f"{enchantmentName} enchantment and {effect}"
    
    
"""testing code"""
workshop = Workshop(Forge(), Enchanter())

materials = {Maple(), Oak(), Ash(), Bronze(), Iron(), Steel(), 
    Ruby(), Sapphire(), Emerald(), Diamond(), Amethyst(), Onyx()}

weaponBlueprints = {   "Sword": [Steel(), Maple()],     
                            "Shield": [Bronze(), Oak()],     
                            "Axe": [Iron(), Ash()],     
                            "Scythe": [Steel(), Ash()],     
                            "Bow": [Oak(), Maple()],     
                            "Wand": [Ash(), Oak()],     
                            "Staff": [Bronze(), Maple()],     
                            "Dagger": [Bronze(), Bronze()]
                            } 

enchantmentBlueprints = {     
                            "Holy": [Diamond(), Diamond()],     
                            "Lava": [Ruby(), Onyx()],     
                            "Pyro": [Ruby(), Diamond()],     
                            "Darkness": [Onyx(), Amethyst()],     
                            "Cursed": [Onyx(), Onyx()],     
                            "Hydro": [Sapphire(), Emerald()],     
                            "Venomous": [Emerald(), Amethyst()],
                            "Earthly": [Emerald(), Amethyst()]
                        }

enchantedWeapons = ["Holy Greatsword", "Molten Defender", "Berserker Axe", "Soul Eater",     
                    "Twisted Bow", "Wand of the Deep", "Venemous Battlestaff"]  

# Adds a number of materials to use for crafting. 
for material in materials:
    if isinstance(material, Wood):         
        workshop.addMaterial(material.__class__.__name__, 20)     
    elif isinstance(material, Metal):         
        workshop.addMaterial(material.__class__.__name__, 10)     
    else:         
        workshop.addMaterial(material.__class__.__name__, 5)  
        
print("--------------------------------Material Store--------------------------------") 
print(workshop.displayMaterials())  

# Crafts the following: Sword, Shield, Axe, Scythe, Bow, Wand and Staff weapons. 
for weapon, materials in weaponBlueprints.items():     
    craftedWeapon = workshop.forge.craft(         
        weapon, materials[0], materials[1], workshop.materials)     
    workshop.addWeapon(craftedWeapon)  
    
#Disassemble the extra weapon. 
workshop.removeWeapon(workshop.forge.disassemble(     
    workshop.weapons[7], workshop.materials))  

print("------------------------------------Armoury-----------------------------------") 
print(workshop.displayWeapons())  
# Crafts the following: Holy, Lava, Pyro, Darkness, Cursed, Hydro and Venomous enchantments. 
for enchantment, materials in enchantmentBlueprints.items():     
    craftedEnchantment = workshop.enchanter.craft(enchantment, materials[0], materials[1], workshop.materials)     
    workshop.addEnchantment(craftedEnchantment)  
    
#Disassemble the extra enchantment 
# workshop.removeEnchantment(workshop.enchanter.disassemble(     
#     workshop.enchantments[7], workshop.materials))  

print("------------------------------------Enchantments------------------------------------") 
print(workshop.displayEnchantments())  

print("-----------------------------------Material Store-----------------------------------") 
print(workshop.displayMaterials())  

# Enchant the following weapons: Sword, Shield, Axe, Scythe, Bow, Wand and Staff. for i in range(len(enchantedWeapons)): 
for i in range(len(enchantedWeapons)):
     workshop.enchanter.enchant(         
        workshop.weapons[i], enchantedWeapons[i], workshop.enchantments[i])  
     
     print("-----------------------------------Enchanted Armoury----------------------------------") 
     print(workshop.displayWeapons()) 