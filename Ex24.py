"""Exercise 24 - More Practice"""

print("Let's practice everything")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs')

poem = """
\tThe lovely world 
with logic so firmly planted 
cannot discern \n the needs of love 
nor comprehend passion from intuition 
and requires an explanation 
\n\t\twhere there is none.
"""
print('-------------------------------')
print(poem)
print('-------------------------------')

five = 10 - 2 + 3 - 6
print(f'This should be: {five}')

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans/1000
    craets = jars/100
    return jelly_beans, jars, craets

start_point = 1000
beans, jars, crates = secret_formula(start_point)

#remember this another way to format string
print('With the starting point of : {}'.format(start_point))
#this is just like with a f"" string
print(f"We do have beans {beans}, jars {jars}, and crates {crates}")

start_point = start_point/10

print("We can also do that this way")
formula = secret_formula(start_point)

#this is an easy way to apply a list to a format string
print("We'd have beans {}, jars {} and crates {}".format(*formula))





