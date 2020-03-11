import requests, gc
from bs4 import BeautifulSoup as soup


def Person(id):
    url = 'https://www.wikidata.org/wiki/' + id
    data = requests.get(url).text
    html = soup (data, 'lxml')
    attributes = {"id":id, "name":"","url":url,"wiki":"" ,"birth":"", "death":"", "sex":"", "mother":"", "father":"",
                  "spouse":"", "children":[]}

    ### Name ###
    if html.find ("span" , {"class": "wikibase-title-label"}) != None:
        attributes['name'] = html.find ("span" , {"class": "wikibase-title-label"}).string

    ### Wikipedia ###
    wiki = html.find ("ul" , {"class": "wikibase-sitelinklistview-listview"})
    if wiki != None:
        wiki = wiki.findAll ("li")
    
        for li in wiki:
            if li.find ("span" , {"lang": "en"}) != None:
                attributes['wiki'] = li.find ("a")['href']

    ### Birth ###
    birth = html.find ("div" , {"id": "P569"})
    if birth != None:
        birth = birth.findAll ("div" , {"class": "wikibase-snakview-variation-valuesnak"})
        if len(birth) > 0:
            attributes['birth'] = birth[0].string

    ### Death ###
    death = html.find ("div" , {"id": "P570"})
    if death != None:
        death = death.findAll ("div" , {"class": "wikibase-snakview-variation-valuesnak"})
        if len(death) > 0:
            attributes['death'] = death[0].string

    ### Sex ###
    sexData = html.find ("div" , {"id": "P21"})

    if sexData != None:
        for item in sexData.strings:
            if item == 'male' or item == 'female':
                attributes['sex'] = item

    ### Mother ###
    mother = html.find ("div" , {"id": "P25"})
    if mother != None:
        mother = mother.findAll ("div" , {"class": "wikibase-snakview-variation-valuesnak"})
        if len(mother) > 0 and "title" in mother[0].find('a'):
            attributes['mother'] = mother[0].find('a')['title']

    ### Father ###
    father = html.find ("div" , {"id": "P22"})
    if father != None:
        father = father.findAll ("div" , {"class": "wikibase-snakview-variation-valuesnak"})
        if len(father) > 0:
            attributes['father'] = father[0].find ('a')['title']

    ### Children ###
    children = html.find("div" , {"id": "P40"})
    if children != None:
        children = children.findAll("div" , {"class": "wikibase-statementview"})

        for child in children:
            a = child.find('a')
            if a != None and a['title'][0] == 'Q':
                    attributes['children'].append (a['title'])

    return attributes


ancestors = ['Q3044']
all = []

file = open('ancestorsFinal2.txt', 'w+');
file.write("ID*Name*Wikipedia Link*Birth*Death*Mother*Father\n")

i = 1

while ancestors != []:
    next = ancestors.pop(0)
    person = Person(next)

    for child in person['children']:
        if child not in all:
            all.append(child)
            ancestors.append(child)

    if person['mother'] != "" and person['mother'] not in all:
        all.append(person['mother'])
        ancestors.append(person['mother'])

    if person['father'] != "" and person['father'] not in all:
        all.append(person['father'])
        ancestors.append(person['father'])


    file.write(person['id'] + "*" + str(person['name']) + "*" + str(person['wiki']) + "*" 
            + str(person['birth']) + "*" + str(person['death']) + "*" + str(person['mother']) 
            + "*" + str(person['father']) + "*" + str(person['children']) + "\n")

    if i % 1000 == 0:
        print(person['name'] + " (" + person['id'] + ")" + " - " + str (len (all)) + " - " + str (len (ancestors)))

    i += 1

file.close()
print("\nDone!")
