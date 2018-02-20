"""Exercise 18 - Names, Variables, Code, Functions"""

def print_two(*args):
    arg1, arg2, arg3, arg4 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I've got nothing")


print_two("Zed", "Shaw","Luke",3)
print_two_again("John", "Doe")
print_one("Python")
print_none()


