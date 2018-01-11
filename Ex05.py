x = 'Python'
my_name = "Zed A. Shaw"
my_age = 35
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Hello {x}")

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

my_height_in_cm = my_height * 2.20
my_weight_in_kg = round(my_weight * 2.2,2)

print(f"His weight in kg is {my_weight_in_kg}")
print(f"His height in cm is {my_height_in_cm}")

print(round(1.77777,2)) # rounds a floating point number to give number of decimals(2nd parameter), if it's empty it will round to whole number

