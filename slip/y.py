def feb(n):
    f=0
    s=1
    for i in range(n+1):
        yield f
        t=f+s
        f=s
        s=t
              
n=int(input("Enter Limit"))
for i in feb(n):
    print(i)
 
