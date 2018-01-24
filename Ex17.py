"""Exercise 17 - More Files"""

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#in_file = open(from_file,'r')
#indata = in_file.read()

indata = open(from_file,'r').read()
#indata = open(from_file).read(), 
# which means you don’t need to then do in_file.close() when you reach the end of the script. 
# It should already be closed by Python once that one line runs

print(f"The input file is {len(indata)} byte long")
print(f"Does the output file exists ? {exists(to_file)}")
print("Ready hit RETURN to continue, CTRL + c to abort")
input()

#out_file = open(to_file,'w')
#out_file.write(indata)

open(to_file, 'w').write(indata)

print("Allright all done")

