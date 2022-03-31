Medname=[]
Medstock=[]
Medexp=[]
def funenter():
    a=int(input("Enter the number of Medicines to be required\n "))
    for i in range(a):
        name=input("Enter the name of Medicine\n")
        Medname.append(name)
        stock=int(input("Enter the stock\n"))
        Medstock.append(stock)
        exp=input("Enter the expiry date \nNOTE: dd/mm/yyyy\n")
        Medexp.append(exp)
    choice()
def fundelete():
    nam=input("Enter the name of Medicine to remove it's details\n")
    b=len(Medname)
    c=Medname.count(nam)
    for j in range(b):
        if c==1:
            if nam==Medname[j]:
                Medname.pop(j)
                Medstock.pop(j)
                Medexp.pop(j)
                break;
        elif c>1:
            if nam==Medname[j]:
                exp=input("Expiry date\n")
                if nam==Medname[j] and exp==Medexp[j]:
                        Medname.pop(j)
                        Medstock.pop(j)
                        Medexp.pop(j)
                        break;
    choice()
def funstock():
    nam=input("Enter the name of Medicine whose stock you want to change\n")
    stoc=int(input("Enter the number of stock sold\n"))
    b=len(Medname)
    c=Medname.count(nam)
    for j in range(b):
        if c==1:
            if nam==Medname[j]:
                Medstock[j]=Medstock[j]-stoc
                break;
        elif c>1:
            if nam==Medname[j]:
                exp=input("Expiry date\n")
                for k in range(c):
                    if exp==Medexp[k]:
                        Medstock[k]=Medstock[k]-stoc
                        break;
                break;
    choice()
def zero():
    b=len(Medname)
    i=0
    while i<b:
        if Medstock[i]==0:
            Medname.pop(i)
            Medstock.pop(i)
            Medexp.pop(i)
            b-=1
        i+=1
def fundisplay():
    c=len(Medname)
    #print(c)
    #print(Medname)
    #print(Medstock)
    #print(Medexp)
    for k in range(c):
      print("\n","\t",Medname[k],"\t",Medstock[k],"\t",Medexp[k],"\n")
    #    print(f"{Medname[k]}\t{Medstock[k]}\t{Medexp[k]}\n")
    zero()
    choice()
def choice():
    ch=input("Enter your choice\nPress 1 to add\nPress 2 to delete\nPress 3 to display\nPress 4 to change stock \nPress 5 to exit\n")
    if ch=='1':
        funenter()
    elif ch=='2':
        fundelete()
    elif ch=='3':
        fundisplay()
    elif ch=='4':
        funstock()
    else:
        exit()
choice() 