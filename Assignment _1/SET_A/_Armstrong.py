n=int(input("Enter Number"))
n1=n
s=0
while(n>0):
    d=n%10
    s+=d*d*d
    n//=10

    
if(n1==s):
     print("Number Is Armstrong")
else:
    print("Number Is Not Armstrong")
