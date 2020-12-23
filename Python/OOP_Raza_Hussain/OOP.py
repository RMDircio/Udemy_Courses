
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

''' -------------------------------------------------------------- '''

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

# instantiate the Peacock class
# these are objects
blu = Peacock('Blu', 10)
woo = Peacock('Woo', 15)
# call our instance methods
print(blu.run('Happily'))

# access the instance attributes
print("Peacock's name is {}. Peacock's age is {}.".format(blu.name, blu.age))


print('--------------------------------------------')

#---------------------------------------#
##      An Understanding of Objects    ##
##        and Classes with Details     ## 
#---------------------------------------#

print('--------------------------------------------')
















print('--------------------------------------------')
