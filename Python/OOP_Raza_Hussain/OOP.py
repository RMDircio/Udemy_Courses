
#---------------------------------------#
##      An Understanding of Objects    ##
##        and Classes with Details     ## 
#---------------------------------------#

# syntax of classes
class myself():
    pass

# Instance Attribute - that will execute whenever we instantiate the class
class Cat():
    species = 'animal'

    def __init__(self): # Constructor method that will execute as soon as the class is instantiated
        print('Nice, we have a cat.')

Tom = Cat()
print(Tom)
print(Tom.species)

# ''' -------------------------------------------------------------- '''

class Peacock():
    # class attributes
    species = 'bird'

    # instance
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def run(self, run):
        return '{} runs {}'.format(self.name, run)

# Instantiating is a fancy term for creating a new, unique instance of the class.
# Instantiate the Peacock class
# these are objects
blu = Peacock('Blu', 10)
woo = Peacock('Woo', 15)
# call our instance methods
print(blu.run('Happily'))

# access the instance attributes
print("Peacock's name is {}. Peacock's age is {}.".format(blu.name, blu.age))


print('--------------------------------------------')

#---------------------------------------#
##      Instantiating the Class as     ##
##       Objects with More Details     ## 
#---------------------------------------# 

'''
Instance Attribute:
    Different for each class. We use '__init__()' method to initialize to specify an 
    object's initial attributes by giving them their default values/states. This method
    must have at least one argument as well as the 'self' variable. 
    'Self' refers to the object itself.
'''

# Demonstrating that each instance is actually different
white = Peacock('White', 4)
white2 = Peacock('White', 4)

# each object created from the class is unique
print('Does "white" equal "white2"? -->', white == white2)

# access the class attributes
print(f'Blue is a {blu.species}')
print(f'Woo is a {woo.species}')

print('--------------------------------------------')



#---------------------------------------#
##      Inheritance, Parents and       ##
##        Child Class the Class        ##
##      and Use of Super Functions     ## 
#---------------------------------------# 

# parent class
class Bird:
    color = 'red'
    def __init__(self):
        print('Bird is ready')

    def whoisthis(self):
        print('Bird')
    
    def swim(self):
        print('Swim faster')

# child class
class Penguin(Bird):
    def __init__(self):
        # use super() function
        super().__init__() # calls upon parent class
        print('Penguin is ready')
    
    # overwrites parent class
    def whoisthis(self):
        print('Penguin')

    def run(self):
        print('Run faster')

peggy = Penguin()
print(peggy.whoisthis())
print(peggy.swim())
print(peggy.run())
print('-----------------------------')
jerry = Bird()
print(jerry.whoisthis())

# you can override the Parent class within the Child class - redefining it
class SomeOtherBird(Bird):
    color = 'White'

print('----------------------------')
newbird = SomeOtherBird()
print(newbird.color)

''' Trying on my own '''

# make a parent animal class

class Animal():
    legs = 4
    def __init__(self):
        print('This is from the Animal Class')
    
class Hawk(Animal):
    legs = 2
    def __init__(self):
        super().__init__()
        print('This is from the Hawk Class')

print('----------------------------')
greg = Animal()
print(greg.legs)

hank = Hawk()
print(hank.legs)












print('--------------------------------------------')