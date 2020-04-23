####################################################################
#
#                            Main.py
#
# Find the path between 2 individuals from Wikidata.org by entering
# their Wikidata IDs in the spots provided on lines 41 & 42
#
####################################################################

from Person import Person

file = open("ancestorsFinal.txt", "r")
file.readline() # Skip the header

# Create dictionary to hold all Person objects
people = {}

# Loop through the file and add all people to the dictionary
for line in file:
    attr = line.split("*")
    people[attr[0]] = Person(attr[0], attr[1], attr[2])

file.close()
file = open("ancestorsFinal.txt", "r")
file.readline()

# This loop creates mother-father relationships in the Person object, connecting the nodes and creating the family tree
# When calling the addMother()/addfather() method, it also creates a child relationship the other way
for line in file:
    attr = line.split("*")

    mother = attr[5]
    father = attr[6][:len(attr[6])-1]

    if mother != '' and mother in people:
        people[attr[0]].addMother(people[mother])

    if father != '' and father in people:
        people[attr[0]].addFather(people[father])

# Enter the person IDs here
person1 = people['Q9682']
person2 = people['Q76']

# Call the path() method to display the path between 2 people
person1.path(person2)