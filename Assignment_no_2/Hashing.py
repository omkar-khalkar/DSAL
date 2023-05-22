from record import *


class hashtable:
    def __init__(self):
        self.hashtable = []
        self.m = int(input("Enter The Number OF students:"))
        self.n = int(input("Enter The Size OF hashtable"))
        self.hashtable = [None]*self.n

    def hashfunction(self, key):
        h1 = key % self.n
        return h1

    def hashfunction2(self, key):
        h2 = 1 + (key % 11)
        return h2

    def isfull(self):
        if None in self.hashtable:
            return 0
        else:
            return 1

    def insert(self, record):
        key = record.no
        h1 = self.hashfunction(key)
        h2 = self.hashfunction2(key)
        if (self.isfull() == 0):
            if (self.hashtable[h1] == None):
                self.hashtable[h1] = record
            else:

                i = 0
                while self.hashtable[h1] != None:
                    i += 1
                    h1 = (h1 + (i * h2)) % self.n
                self.hashtable[h1] = record

        else:
            print("HashTable is Full")

    def display(self):
        for k in self.hashtable:
            if (k != None):
                print("INDEX : ", self.hashtable.index(k))
                print("Name-->", k.name, "; Number--->", k.no)

