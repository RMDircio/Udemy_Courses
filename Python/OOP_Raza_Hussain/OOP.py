
#---------------------------------------#
##      An Understanding of Objects    ##
##        and Classes with Details     ## 
#---------------------------------------#

# # syntax of classes
# class myself():
#     pass

# # Instance Attribute - that will execute whenever we instantiate the class
# class Cat():
#     species = 'animal'

#     def __init__(self): # Constructor method that will execute as soon as the class is instantiated
#         print('Nice, we have a cat.')

# Tom = Cat()
# print(Tom)
# print(Tom.species)

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
