"""Exercise 16 - Reading and Writing Files"""
from sys import argv

script, file_name = argv

print(f"We're going to erase {file_name} file.")
print("If you don't want that hit CTRL + c (^c)")
print("If you do want hit RETURN")
input("?")

print("Opening the file.....")
target = open(file_name,'w')

print("Truncating the file , Goodbye!!")
target.truncate()

print("Now I'm going to ask you for three lines")

line1 = input("Line1:")
line2 = input("Line2:")
line3 = input("Line3:")

print("I am going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")


print("And finally we close the file")
target.close()

