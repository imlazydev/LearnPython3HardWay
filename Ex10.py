""" Exercise 10 What was that """

print("I am 6'2\" tall.")  # escape doule-quote inside a string using \"
print('I am 6\'2" tall.')  # escape quote inside a string using \'

# print("\n")

tabby_cat = "\tI'm tabbed in."  # \t escape character for tab
persian_cat = "I'm split \non a line"
backslash_cat = "I'm \\ a \\ cat."  # \\ escape backslash (\)

fat_cat = '''
I'll do a list
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

fat_cat = """
I'll do a list
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(fat_cat)


#
# Escape character supported by python
# \\ - Backslash
# \' - Single quote
# \" - Double quote
# \a - ASCII bell (BEL)
# \b - ASCII backspace (BS)
# \f - ASCII formfeed(FF)
# \n - ASCII linefeed (LF)
# \r - Carriage return (CR)
# \t - Horizontal Tab (TAB)
# \v - ASCII vertical tab (VT)
