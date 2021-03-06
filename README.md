# Family Tree

Find family connections between people born thousands of years apart. Information from over 600,000 individuals has been pulled from [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page) using [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/) and [requests](https://requests.readthedocs.io/en/master/) in python.


From Arnie to Liz, via JFK!
![alt text](path_example.png) 

##### Person.py 
The `path()` method in the Person object uses breadth-first search to find the shortest path between 2 people, and prints out all individuals in the path.


##### tree_builder.py
This is the script used to scrape wikidata.org. I let it run on a AWS Micro server, which took about 12 days to pull all 600,000 people


##### ancestorsFinal.txt
ancestorsFinal.txt holds all the data that was extracted by running the tree_builder.py script. One person per line, and columns are separated with an asterisk character (*) due to issues with comma in peoples names causing parsing issues

**Disclaimer**: As the data is from Wikidata, which is a collaboratively edited knowledge base, not all connections can be verified. References are included on the individuals wikidata page where available.
