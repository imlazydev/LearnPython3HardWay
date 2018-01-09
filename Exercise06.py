"""Exercise 06"""
types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"

y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said : {x}")
print(f"I also said '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}, {}"

#format function fills the place holders in the string it's been called. 
# You can have any number of placeholders and you have to pass values to all of them or else you will get an tuple index missing exception
#You can call format function without any placeholders in the called string and you will not get any errors
print(joke_evaluation.format(hilarious, binary))

w = "This is the left side of ..."
e = " a string with a rght side."

# + on string values does string concatnation of those strings.
print(w + e)
