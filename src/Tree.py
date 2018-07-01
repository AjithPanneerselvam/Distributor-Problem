"""
Binary Search Tree and World Tree
"""
from Utility import FileReader, Message


class BSTNode:
    def __init__(self, startID, endID):
        self.startID = startID
        self.endID = endID
        self.left = None
        self.right = None 



class BinarySearchTree:
    def __init__(self):
        self.root = None 


    def insertNode(self, root, startID, endID):
        if(self.root == None):
            newNode = BSTNode(startID, endID)
            self.root = newNode
            return root
            
        if(root == None):
            newNode = BSTNode(startID, endID)
            return newNode
        
        mid = int((root.startID + root.endID) // 2)
        if(startID < mid):
            root.left = self.insertNode(root.left, startID, endID)
        else:
            root.right = self.insertNode(root.right, startID, endID)
        
        return root
    

    def isInRange(self, root , startID, endID):
        if(root == None):
            return False 
        if(root.startID <= startID and root.endID >= endID):
            return True

        mid = int((root.startID + root.endID) // 2)
        if(startID < mid):
            return self.isInRange(root.left, startID, endID)
        else:
            return self.isInRange(root.right, startID, endID) 


    def printTree(self, root):
        if(root == None):
            return

        self.printTree(root.left)
        print(root.startID, root.endID)
        self.printTree(root.right)



class PlaceNode:
    def __init__(self):
        self.startID = -1
        self.endID = -1
        self.children = dict()
        

class WorldTree:
    def __init__(self):
        self.runningPlaceID = -1
        self.world = PlaceNode()
        self.createWorldTree()
    

    def preprocessString(self, place):
        for i in range(len(place)):
            temp = place[i]
            temp = temp.upper()
            temp = temp.split(' ')
            temp = ''.join(temp)
            place[i] = temp 
        return place  


    def insertNode(self, country, province, city):
        country, province, city = self.preprocessString([country, province, city])
        # print(country, province, city)

        if(country not in self.world.children):
            newNode = PlaceNode()
            self.world.children[country] = newNode
        
        if(province not in self.world.children[country].children):
            newNode = PlaceNode()
            self.world.children[country].children[province] = newNode
        
        if(city not in self.world.children[country].children[province].children):
            newNode = PlaceNode() 
            self.world.children[country].children[province].children[city] = newNode 
    

    def assignID(self, node):
        self.runningPlaceID += 1
        node.startID = self.runningPlaceID
        
        for keyNode in node.children:
            self.assignID(node.children[keyNode])
        
        node.endID = self.runningPlaceID
    

    def getID(self, place):
        node = self.world

        for i in range(len(place)):
            if(place[i] in node.children):
                node = node.children[place[i]]
            else:
                Message().invalidPlaceError(place)
                
        return [node.startID, node.endID]


    def preProcessData(self, places):
        world = dict()

        for place in places: 
            country, province, city = place 
            if(country not in world):
                world[country] = dict() 

            if(province not in world[country]):
                world[country][province] = list()

            if(city not in world[country][province]):
                world[country][province].append(city)
        
        return world

        
    def createWorldTree(self):
        fileReader = FileReader()
        places = fileReader.readCSVFile('./../Dataset/cities.csv')
        preProcessWorld = self.preProcessData(places)
    
        for country in preProcessWorld:
            for province in preProcessWorld[country]: 
                for city in preProcessWorld[country][province]:
                    self.insertNode(country, province, city)
                
        self.assignID(self.world)


# bst = BinarySearchTree()
# bst.insertNode(bst.root, 2, 1000)
# bst.insertNode(bst.root, 4, 81)
# bst.insertNode(bst.root, 501, 600)
# bst.insertNode(bst.root, 549, 549)
# bst.insertNode(bst.root, 550, 550)
# bst.printTree(bst.root)
# print(bst.isInRange(bst.root, 550, 550))
# print(bst.isInRange(bst.root, 5, 80))
# print(bst.isInRange(bst.root, 1, 100))


