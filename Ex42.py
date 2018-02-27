"""Exercise 42 Is-A, Has-A, Objects and Classes"""


# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass


# Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        # Dog has-a name
        self.name = name


# Cat is-a Animal
class Cat(Animal):

    def __init__(self,name):
        # Cat has-a name
        self.name = name


# Person is-a object
class Person(object):

    def __init__(self,name):
        # Person has-a name
        self.name = name

        # Person has-a pet
        self.pet = None


# Employee is-a Person
class Employee(Person):
    # ?? hmm what is this strange magic
    def __init__(self,name,salary):
        # call super with arguments Employee and self, then call the function(constructor) __init__
        super(Employee,self).__init__(name)
        # ??
        self.salary = salary


class Fish(object):
    pass


class Salmon(Fish):
    pass


class Halibut(Fish):
    pass


# rover is-a Dog or rover is-a Animal
rover = Dog("Rover")

# satan is-a Cat or satan is-a Animal
satan = Cat("Satan")


# mary is a person
mary = Person("Mary")


# mary has-a pet
mary.pet = satan


# frank is-a Employee
frank = Employee("Frank",120000)

# frank has-a pet
frank.pet = rover


# flipper is-a fish
flipper = Fish()


# crouse is-a Salmon
crouse = Salmon()


# harry is-a halibut
harry = Halibut()




