"""Exercise 12 - Prominting People """

name = input("Name ?")
age = input("How old are you?")
height = input("How tall are you?")
weight = input('How much\'d you weigh?')

print("So you are", age ,"old", height, "tall and", weight, "heavy.")
print(f"So you are {age} old {height} tall and {weight} heavy.")

x = "So you are {} old {} tall and {} heavy."
print(x.format(age, height, weight))


