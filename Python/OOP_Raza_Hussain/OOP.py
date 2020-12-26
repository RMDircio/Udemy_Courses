
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
print('----------------------------')


#---------------------------------------#
##        Levels of Inheritance        ##
##     and Method Resolution Order     ##
#---------------------------------------# 

# syntax for multiple inheritance

class Inheritance1:
    pass

class Inheritance2:
    pass

class MultiInheritance(Inheritance1, Inheritance2):
    pass

# example

# class Both(Bird, Penguin): # order is from left to right
    pass

print('--------------------------------------------')



#---------------------------------------#
##        Operator Overloading         ##
#---------------------------------------# 

''' Some operators have different meanings depending on the context when used '''

# string
a = 'He'
b = 'llo'
c = a + b
print(c)

# Integers
d = 5
e = 6
f = d + e
print(f)

# lists
Students = ['John', 8, 'Ami', 5, 'Ali', 4]
New_Studnets = ['Joseph', 8, 'Alex', 7]
Total_Students = Students + New_Studnets
print(Total_Students)

# define a class
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

P1 = Point(2,3)
print(P1) # this prints an object - a point in memory

# add the str and add function to the class
class Point_Update:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'{self.x}, {self.y}'
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point_Update(x,y)

P2 = Point_Update(7,9)
P3 = Point_Update(7,9)
print(P2+P3) # add the two set of points together

'''
                Some of the Common Operator Overloading Special Functions in Python
    -------------------------------------------------------------------------
    |       Operator         |       Expression      |       Interally      |
    -------------------------------------------------------------------------
    |       Addition        -->     p1 + p2         -->     p1.__add__(p2)    
    |       Subtraction     -->     p1 - p2         -->     p1.__sub__(p2)   
    |       Multiplication  -->     p1 * p2         -->     p1.__mul__(p2)   
    |       Power           -->     p1 ** p2        -->     p1.__pow__(p2)   
    |       Division        -->     p1 / p2         -->     p1.__truediv__(p2)   
    -------------------------------------------------------------------------

