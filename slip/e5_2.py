

def feb(n):
    f=0
    s=1
    for i in range(0,n):
        yield f
        t=f+s
        f=s
        s=t

n=int(input("enter no"))
for show in feb(n):
    print(show)
