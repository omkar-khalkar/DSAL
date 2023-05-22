from record import *


class hashtable:
    def __init__(self):
        self.size = int(input("Enter the size of hashtable : "))
        self.table = list(None for i in range(self.size))
        self.elementcount = 0
        self.comparison = 0
        self.m=int(input("Enter the prime no which is nearly less than table size : "))
    
    def isFull(self):
        if (self.elementcount == self.size):
            return True
        else:
            return False

    def hashfunction(self, key):
        return key % self.size
    
    def hashfunction2(self,key):
        return self.m-(key%self.m)

    def linear_probing(self, c):
        if (self.isFull()):
            print("Hashtable is full !!!")
            return False
        position = self.hashfunction(c.get_no())
        if (self.table[position] == None):
            self.table[position] = c
            print("Record inserted sucessfully ")
            self.elementcount += 1
        else:
            print("\tCollision occured !!!")
            print("\tLinear probing is applied ")
            while (self.table[position] != None):
                position += 1
                self.comparison+=1
                if (position >= self.size):
                    position = 0
            self.table[position] = c
            print("Record inserted sucessfully ")
            self.elementcount += 1

    def double_hashing(self,c):
        if (self.isFull()):
            print("Hashtable is full !!!")
            return False
        position = self.hashfunction(c.get_no())
        if(position>=self.size):
            position=0
        if (self.table[position] == None):
            self.table[position] = c
            print("Record inserted sucessfully ")
            self.elementcount += 1
        else:
            print("\tCollision occured !!!")
            print("\tDouble Hashing Technique  is applied ")
            while(self.table[position]!=None):
                position=self.hashfunction(c.get_no())+self.hashfunction2(c.get_no())
                self.comparison+=1
                if(position>=self.size):
                    position=position%self.size
            self.table[position]=c
            print("Record inserted sucessfully ")
            self.elementcount += 1
            
                

    def display(self):
        print("\n")
        for i in range(self.size):
            print("Hash value : "+str(i)+"\t\t"+str(self.table[i].no))
        print("\nTotal no. of elements are : ", self.elementcount)
        print("\nTotal no. of comparisons are (Probe Value) : ", self.comparison)


def main():
    a = hashtable()
    while (True):
        print("\n_______________________MENU______________________________\n")
        print("\t1.Dispaly Table ")
        print("\t2.Insert Record with Linear Probing")
        print("\t3.Insert Recors with Double Hashing")
        print("\t4.Check table is Full or not ")
        print("\t5.Exit")
        ch = int(input("\nEnter your choice : "))
        if (ch == 1):
            a.display()
        elif (ch == 2):
            n=int(input("Enter the no of records you want to insert : "))
            for i in range(n):
                b = record()
                x = str(input("Enter tha name : "))
                k = int(input("Enter tha number : "))
                b.set_name(x)
                b.set_no(k)
                a.linear_probing(b)
        elif (ch == 3):
            n = int(input("Enter the no of elements you want to insert : "))
            for i in range(n):
                b = record()
                x=str(input("Enter tha name : "))
                k=int(input("Enter tha number : "))
                b.set_name(x)
                b.set_no(k)
                a.double_hashing(b)
        elif (ch == 4):
            if (a.isFull()):
                print("\tTable is full !!!")
            else:
                print("\tTable is not full ")
        else:
            break


main()
