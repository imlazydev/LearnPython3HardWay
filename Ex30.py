""" Exercise 30 - Else and If """
people = 30
cars = 40
trucks = 15

if cars> people :
    print("We should take the cars")
elif cars < people:
    print("We should not take the cars")
else:
    print("We can't decide")

if(trucks > cars):
    print("That's too many trucks")
elif (trucks < cars):
    print("May be we could take the trucks")
else:
    print("We still can't decide")

if people > trucks:
    print("Alright, let's just take the trucks")
else:
    print("Fine, let's stay home then")

if people > trucks or cars > trucks:
    print("People take cars")
elif not(cars<=trucks) and (people != cars) or (people >= cars):
   print("Complex if statement") 
else:
    print("Do anything you like")

if people > trucks or cars > trucks:
    print("People take cars")
    if(trucks == cars):
        print("Nested if")
    else:
        print("Nested if else")
elif not(cars<=trucks) and (people != cars) or (people >= cars):
   print("Complex if statement") 
else:
    print("Do anything you like")


#To check if number is in a range
#Option 1 : 0 < x < 10 or else 1 <= x < 10
#Option 2 : x in range(1,10)
#both are similar 