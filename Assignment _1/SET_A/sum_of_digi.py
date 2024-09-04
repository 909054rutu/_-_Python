n=int(input("Enter Number"))
s=0
while(n>0):
    d=n%10
    s=s+d
    n=n//10
    
print("Sum Of Digit",s)
