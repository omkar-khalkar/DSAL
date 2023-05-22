import SetThory as SetThory

a=SetThory.Set()
b= SetThory.Set()

ch=1
while(ch!=0):
    print("\n**********************************************\n")
    print("\n1.SET A")
    print("2.SET B")
    print("3.Operation on SET A and B")
    print("0.Exit\n")
    ch= int(input("Enter Your Choice: "))
    print("\n**********************************************\n")

    if ch==1:
        ch2=1
        print("\n-----------------------------> SET A <----------------------------")
        while(ch2!=0):
            print("\n1.Add")
            print("2.Remove")
            print("3.Size")
            print("4.Display")
            print("5.Element is Present in Set")
            print("0.Exit From SET A\n")
            ch2 = int(input("Enter Your Choice : "))
            if ch2==1:
                x=int(input("Element To be Added : "))
                a.Add(x)
            elif ch2==2:
                x=int(input("Element To be Removed : "))
                a.Remove(x)
            elif ch2==3:
                print("LENGTH OF THE SET : ",a.size())
            elif ch2==4:
                print("SET A : ",a.elements)
            elif ch2==5:
                x=int(input("Element To be Checked : "))
                print("Element is in The Set :",a.contains(x))
            else:
                break
                
        print("\n---------------------------------><--------------------------------")

    elif ch==2:
        ch3=1
        print("\n----------------------------->SET B<----------------------------\n")
        while(ch3!=0):
            print("\n1.Add")
            print("2.Remove")
            print("3.Size")
            print("4.Display")
            print("5.Element is Present in Set")
            print("0.Exit From SET B\n")
            ch3 = int(input("Enter Your Choice : "))
            if ch3==1:
                x=int(input("Element To be Added : "))
                b.Add(x)
            elif ch3==2:
                x=int(input("Element To be Removed : "))
                b.Remove(x)
            elif ch3==3:
                print("LENGTH OF THE SET : ",b.size())
            elif ch3==4:
                print("SET A")
                b.display()
            elif ch3==5:
                x=int(input("Element To be Checked : "))
                print("Element is in The Set :",a.contains(x))
            else:
                break
        print("\n---------------------------------><--------------------------------\n")
            

    elif ch==3:
        print("---------------------------------->OPERATIONS TO BE PERFORMED<---------------------------------------")
        print("\n1.Union")
        print("2.Intersection")
        print("3.Difference")
        print("4.Symmetric Difference")
        print("5.IsSubset\n")
        ch4=int(input("Enter Your Choice : "))
        if ch4==1:
            print("UNION OF TWO SET :",a.union(b))
        elif ch4==2:
            print("UNION OF TWO SET :",a.intersection(b))
        elif ch4==3:
            print("\n1.A-B")
            print("2.B-A\n")
            ch5=int(input("Enter Your Choice :"))
            if ch5==1:
                print("Difference :",a.diff(b))
            if ch5==2:
                print("Difference :",b.diff(a))
        elif ch4==4:
            print("Symmetric DIfference : ",a.symm_diff(b))
        print("----------------------------------------------->THANK YOU<-----------------------------------------------------")
    else:
        break;
    
       

