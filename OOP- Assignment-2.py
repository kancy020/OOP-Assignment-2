
class Workshop:
     pass
    
    #displays weapon, use if to see if value == to enchated opr not enchanted weapon
    def displayWeapons():
        pass
    
    #prints all enchatments in an enchantments list   
    def displayEnchantments():
        pass
    
    #prints material name and amount of material remaining
    def displayMaterials():
     
#is an abstract class    
class Crafter:
    pass

    #crafting method for forge and enchanter(add weapon or enchantment to list)
    def craft():
        pass
    
    #disassemble method for forge and enchanter(removes weapon or enchantment from list)
    def disassemble():
        pass

class Enchanter(Crafter):
    pass
    # copy dictionary from assignment sheet
    
    #crafting method for forge and enchanter(add weapon or enchantment to list)
    def craft():
        pass
    
    #disassemble method for forge and enchanter(removes weapon or enchantment from workshop)
    def disassemble():
        pass
    
    def enchant(weapon, enchantmentName, enchantment):


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
    def __init(self,name, magicDamage, effect, primaryMaterial, secondaryMaterial):
            self.__name = name
            self.__magicDamage = magicDamage
            self.__effect = effect
            self.__primaryMaterial = primaryMaterial
            self.__secondaryMaterial = secondaryMaterial
            
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
        
    def getSecondaryMaterial():
        pass

    def calculateMagicDamage():
        pass
            
    def useEffect():
        pass
            
    #property to be made for each
            
    pass

class Weapon:
    def __init__(self,name, damage, primaryMaterial, secondaryMaterial):
         self.__name = name
         self.__damage = damage
         self.__primaryMaterial = primaryMaterial
         self.__secondaryMaterial = secondaryMaterial
         self.__enchanted = None
         
         
    # get weapon name  
    def getName():
        pass
    
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