class doublehash:
    # def display(self,)
    def __init__(self) :
        self.ht=[]
        self.n = int(input("Enter The Size of The Hash Table:"))
        self.m = int(input("Enter The Total of The Number of Student:"))
        self.ht=[-1]*self.n
    
    def display(self):
        print(self.ht)
    
    def hashfunction1(self,key):
        return key%11;
    
    def hashfunction2(self,key):
        return 1+11-(key%11);

a = doublehash()
data = []
for i in range(a.m):
    no = int(input("Number-->"))
    data.append(no)
# print(data)
for k in data:
    # print(k)
    h1 = a.hashfunction1(k)
    h2 = a.hashfunction2(k)

    if(a.ht[h1]==-1):
        a.ht[h1]==k
        a.display()
    else:
        i=0
        while(a.ht[h] != -1):
            i += 1
            h = (h1 + (i * h2)) %11
        a.ht[h] = k
        a.display()
            

   
       




        
        

    

        




   











    


    

        
    
        
