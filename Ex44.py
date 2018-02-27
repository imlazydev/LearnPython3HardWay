"""Exercise 44 Inheritance vs Composition"""

# 1. Actions on the child imply an action on the parent


class Parent(object):
    def implicit(self):
        print("PARENT implicit()")


class Child(Parent):
    pass


dad = Parent()
son = Child()

dad.implicit()
son.implicit()


# 2. Actions on the child override the action on the parent
#  In this case you want to override the function in the child,
# effectively replacing the functionality. To do this just define a function with the same name in Child.

class Parent(object):
    def override(self):
        print("PARENT override()")


class Child(Parent):
    def override(self):
        print("CHILD override()")


dad = Parent()
son = Child()

dad.override()
son.override()


# 3. Actions on the child alter the action on the parent.
# Alter Before or After Parent
# The third way to use inheritance is a special case of overriding
# where you want to alter the behavior before or after the Parent class’s version runs.
# You first override the function just like in the last example,
# but then you use a Python built-in function named super to get the Parent version to call.


class Parent(object):
    def altered(self):
        print("PARENT altered()")





class Child(Parent):
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        # call super with arguments Child and self, then call the function altered
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()

dad.altered()
son.altered()


## COMPOSITION

class Other(object):
    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")


class Child(object):
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD AFTER OTHER altered()")


son = Child()
son.implicit()
son.override()
son.altered()
