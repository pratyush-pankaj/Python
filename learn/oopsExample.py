"""
Class - A class is a collection of objects. A class contains the blueprints or the prototype from which the objects are being created.
Objects - The object is an entity that has a state and behavior associated with it. 
Polymorphism - Polymorphism simply means having many forms.
Encapsulation - It describes the idea of wrapping data and the methods that work on data within one unit
Inheritance - Inheritance is the capability of one class to derive or inherit the properties from another class
Data Abstraction- It hides the unnecessary code details from the user. Also,  when we do not want to give out sensitive parts of our code implementation and this is where data abstraction came.

"""

"""
Self - Class methods must have an extra first parameter in the method definition. Points to itself. this keyword in java, c++
"""

"""
The __init__ method is a constructors. It is run as soon as an object of a class is instantiated
"""

class Dog:

    # class attribute
    attr1 = "mammal"

    #instance attribute
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is {}".format(self.name))

# Driver Code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))

#Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))

#Accessing class methods
Rodger.speak()
Tommy.speak()



