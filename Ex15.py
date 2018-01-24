"""Exercise 15 - Reading Files"""

from sys import argv

script, file_name = argv

#Opens a file and assigns to txt
txt = open(file_name)

print(f"Here is your file {file_name}")
#Reads the opened file and prints to console
print(txt.read())
txt.close()
print("Type the file name again:")
file_again = input(">")

txt_again = open(file_again)
print(txt_again.read())
txt_again.close()
#If the file is not in the correct working directory then you have to provide the full path. Relative path will not work.
