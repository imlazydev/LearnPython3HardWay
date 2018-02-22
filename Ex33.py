
numbers = []

def printNumbers(number):
    i = 0
    while i < number:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += 1
        print("Numbers now :", numbers)
        print(f"At the bottom i is {i}")

printNumbers(3)

print("The numbers :")

for num in numbers:
    print(num)  