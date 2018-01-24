"""Exercise 19 - Functions and Variables"""


def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses.")
    print(f"You have {boxes_of_crackers} boxes of crackers.")
    print("Man that's enough for the party.")
    print("Get a blanket \n")


print("We can just give the functions numbers directly:")
cheese_and_crackers(20, 30)

print("OR we can use variables from our script:")
amount_of_cheese = 50
amount_of_crackers = 100

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do a math inside too:")
cheese_and_crackers(10 + 10, 10 * 2 * 2)

print("And we can combine both variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers * 2)


