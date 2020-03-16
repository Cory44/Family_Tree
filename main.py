from Person import Person

file = open("ancestorsFinal.txt", "r")
file.readline()

people = {}

for line in file:
    attr = line.split("*")
    people[attr[0]] = Person(attr[0], attr[1], attr[2])

file.close()
file = open("ancestorsFinal.txt", "r")
file.readline()

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
person2 = people['Q9439']

person1.path(person2)