####################################################################
#
#                           Person.py
#
# Creates a Person object, with ID, name and wikipedia links.
# Person objects can then be connected with a mother and father
# Person object which then creates a 2 way edge (parent-child and
# child-parent). Using these connections, a graph structure can
# be created to represent a family tree
#
####################################################################

class Person:

    # Initialize with given ID, Name and Wikipedia Link. All relationships start empty
    def __init__(self, id, name, wiki):
        self.id = id
        self.name = name
        self.wiki = wiki
        self.mother = None
        self.father = None
        self.children = []

    # Return the persons name when printed
    def __str__(self):
        return self.name

    # Adds a Person object as a mother attribute and appends 'self' to the children attribute list
    # of the mother
    def addMother(self, mother):
        if self.mother == None:
            self.mother = mother
            mother.__addChild(self)

    # Adds a Person object as a father attribute and appends 'self' to the children attribute list
    # of the father
    def addFather(self, father):
        if self.father == None:
            self.father = father
            father.__addChild(self)

    # Adds a Person object to the children list attribute.
    # Private method, designed to only be called within the addmother() or addFather() methods
    def __addChild(self, child):
        isAdded = False

        for myChild in self.children:
            if child.id == myChild.id:
                isAdded = True

        if not isAdded:
            self.children.append(child)

    # Uses a breath-first search to find the given Person object within the Graph structure
    # Then, if found a match, prints the Person details of every node in the shortest path
    def path(self, person):

        found = False
        queue = [{"level" : 0, "node" : self, "parent" : None}]
        dequeue = []
        peopleFound = [self]
        testNode = {}
        x = 0

        while not found and len(queue):
            x += 1
            if x % 25000 == 0 : print(len(peopleFound), len(queue), len(peopleFound)-len(queue))

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

            parent = testNode['parent']

            while parent != self:
                discovered  = False
                i = 0

                while not discovered:
                    if i < len(dequeue) and dequeue[i]['node'] == parent:
                        discovered = True
                        print(str(dequeue[i]['level']) + ": " + dequeue[i]['node'].id + " - " + dequeue[i]['node'].name + "(" + dequeue[i]['node'].wiki + ")")
                        parent = dequeue[i]['parent']
                    elif i < len(queue) and queue[i]['node'] == parent:
                        discovered = True
                        print(str(queue[i]['level']) + ": " + dequeue[i]['node'].id + " - " + queue[i]['node'].name + "(" + queue[i]['node'].wiki + ")")
                        parent = queue[i]['parent']

                    i += 1

            print("0: " + self.id + " - " + self.name + "(" + self.wiki + ")")
        else:
            print("Person not Found")