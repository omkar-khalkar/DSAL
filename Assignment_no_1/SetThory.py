"""
To create ADT that implement the "set" concept.
a. Add (new Element) -Place a value into the set , 
b. Remove (element) Remove the value
c. Contains (element) Return true if element is in collection, 
d. Size () Return number of values in collection Iterator () Return an iterator used to loop over collection,
e. Intersection of two sets , 
f. Union of two sets, 
g. Difference between two sets,
h. Subset
"""


class Set:
    def __init__(self):
        self.elements = []

    def display(self):
        print(self.elements)

    def Add(self, x):
        if x not in self.elements:
            self.elements.append(x)
        else:
            return -1

    def size(self):
        return len(self.elements)

    def intersection(self, b):
        inter = []
        for i in self.elements:
            if i in b.elements:
                inter.append(i)
        return inter

    def union(self, b):
        un = self.elements.copy()
        for i in b.elements:
            if i not in un:
                un.append(i)
        return un

    def diff(self, b):
        diff = []
        for i in self.elements:
            if i not in b.elements:
                diff.append(i)
        return diff

    def symm_diff(self, b):
        symm = self.elements.copy()
        for i in b.elements:
            if i in symm:
                symm.remove(i)
            else:
                self.elements.append(i)
        return symm

    def contains(self, x):
        if x in self.elements:
            return 1
        else:
            return 0

    def Remove(self, x):
        self.elements.remove(x)
