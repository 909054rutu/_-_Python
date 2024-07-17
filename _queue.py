a1=[]
ch=0
while ch!=3:
    print("1-insert\n 2-delete \n 3-disp")
    ch=int(input("enter choice"))
    if ch==1:
        num=int(input("enter number"))
        a1.append(num)
        
    elif ch==2:
     if len(a1)==0:
         print("Stack is empty")
         else:
          del a1[-1]
       print(a1)
else:
    print(a1)
