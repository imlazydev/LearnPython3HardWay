""" Exercise 08 Printing, Printing """

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format('1', '2', '3', '4'))
print(formatter.format("One", "Two", "Three", "Four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
"Try your",
"own text here",
"may be a poem",
"or a song about fear"
))

