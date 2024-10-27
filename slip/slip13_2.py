q=[]
ch=0
while ch!=4:
    print("\n 1-insert 2-del 3-print")
    ch=int(input("Enter Choice"))
    
    if ch==1:
        n=input("enter element")
        q.append(n)
        print(q)
    elif ch==2:
            if len(q)==0:
                print("empty")
            else:
                del q[0]
                print(q)
    elif ch==3:
            print(q)
    else:
        print("invalid")
            
                    
