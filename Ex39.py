"""Exercise 39 - Dictionaries, Oh Lovely Dictionaries"""

stuff = {'name':'Zed', 'age': 39, 'height': 6 * 12 + 2}
print(stuff['name'])

print(stuff['height'])

stuff['city'] = "SF"
print(stuff['city'])

stuff[1] = "wow"
stuff[2] = "Neato"

print(stuff[1])
print(stuff[2])
print(stuff['name'])

print(stuff)

del(stuff[1])

print(stuff)

del(stuff['city'])

print(stuff)

#create a state mapping for abbreviation

states = {
    'Oregan': 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'NewYork' : 'NY',
    'Michigan' : 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('-' * 30)
print("NY state has : ", cities['NY'])
print("OR state has : ", cities['OR'])

# print some states
print('-' * 30)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then the city
print('-' * 30)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbriviation

print('-' * 30)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state

print('-' * 30)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time

print('-' * 30)
for state, abbrev in list(states.items()):
    print(f"{state} has abbrev {abbrev} and has city {cities[abbrev]}")

print('-' * 30)

# safely get a abbreviationi by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry no Texas")

# get a city with a  defautl value

city = cities.get('TX', 'Does not exist')
print(f"The city for the state 'TX' is : {city}")
