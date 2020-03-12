class Person:

    def __init__(self, id, name, wiki):
        self.id = id
        self.name = name
        self.wiki = wiki
        self.mother = None
        self.father = None
        self.children = []

    def __str__(self):
        return self.name

    def addMother(self, mother):
        if self.mother == None:
            self.mother = mother
            mother.addChild(self)

    def addFather(self, father):
        if self.father == None:
            self.father = father
            father.addChild(self)

    def addChild(self, child):
        isAdded = False

        for myChild in self.children:
            if child.id == myChild.id:
                isAdded = True

        if not isAdded:
            self.children.append(child)

    def path(self, person):

        found = False
        queue = [{"level" : 0, "node" : self, "parent" : None}]
        dequeue = []
        peopleFound = [self]
        testNode = {}
        x = 0

        while not found and len(queue):
            x += 1
            if x % 10000 == 0 : print(len(peopleFound), len(queue), len(peopleFound)-len(queue))

            node = queue.pop(0)
            dequeue.append(node)

            if node['node'].mother != None and node['node'].mother not in peopleFound:
                queue.append({"level": node['level'] + 1, "node": node['node'].mother, "parent": node['node']})
                peopleFound.append(node['node'].mother)

                if node['node'].mother == person:
                    found = True
                    testNode = queue[-1]

            if node['node'].father != None and node['node'].father not in peopleFound:
                queue.append({"level": node['level'] + 1, "node": node['node'].father, "parent": node['node']})
                peopleFound.append(node['node'].father)

                if node['node'].father == person:
                    found = True
                    testNode = queue[-1]

            if node['node'].children != []:
                for child in node['node'].children:
                    if child not in peopleFound:
                        queue.append({"level": node['level'] + 1, "node": child, "parent": node['node']})
                        peopleFound.append(child)

                        if child == person:
                            found = True
                            testNode = queue[-1]

        if found == True:
            print(str(testNode['level']) + ": " + testNode['node'].id + " - " + testNode['node'].name + "(" + testNode['node'].wiki + ")")

            node = testNode
            parent = testNode['parent']

            while parent != self:
                discovered  = False
                i = 0

                while not discovered:
                    if i < len(dequeue) and dequeue[i]['node'] == parent:
                        discovered = True
                        print(str(dequeue[i]['level']) + ": " + dequeue[i]['node'].id + " - " + dequeue[i]['node'].name + "(" + dequeue[i]['node'].wiki + ")")
                        parent = dequeue[i]['parent']
                        # print(parent)
                    elif i < len(queue) and queue[i]['node'] == parent:
                        discovered = True
                        print(str(queue[i]['level']) + ": " + dequeue[i]['node'].id + " - " + queue[i]['node'].name + "(" + queue[i]['node'].wiki + ")")
                        parent = queue[i]['parent']
                        # print(parent)

                    i += 1

            print("0: " + self.id + " - " + self.name + "(" + self.wiki + ")")

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

    # print(attr[1], mother, father)
    if mother != '' and mother in people:
        people[attr[0]].addMother(people[mother])

    if father != '' and father in people:
        people[attr[0]].addFather(people[father])

person = people['Q9682']
person2 = people['Q2685']

# print(person, person.wiki, person.mother, person.father, person.father.wiki, person.children)

person2.path(person)
