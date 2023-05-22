class hashf:
    def __init__(self):
        self.ht = []

    def hashfunction1(self, key, m):
        return key % m
    
  
    
    def isfull(self):
        if -1 in self.ht:
            return False
        return True

    def display(self):
        print(self.ht)
        
    


a = hashf()
data = []
n = int(input("Enter Number of Students :- "))
m = int(input("Enter The Size Of Hash Table : "))
print("Enter Phone Numbers --\n")
a.ht = [-1]*m

for i in range(n):
    n = input("Name-->")
    x = int(input("Ph.no.-->"))
    data.append([n, x])
    hk = a.hashfunction1(x, m)
    if a.ht[hk] == -1:
        a.ht[hk] = [n,x]
    else:
        # hk = 0
        while a.ht[hk] != -1:
            hk += hk%1
        a.ht[hk] = [n,x]
    a.display()
    ch = input("you want Remove Element(y/n)")
    if ch=="y":
        x = int(input("Enter The Value To be Removed : "))
        for j in range(len(a.ht)):
            if(a.ht[j]!=-1):
                if(a.ht[j][1]==x):
                    a.ht.remove(a.ht[j])
        a.display()
           

    

