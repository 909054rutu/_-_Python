n=int(input("Enter Number"))
f=0
for i in range(2,n):
    if n%i==0:
      f=1
if f==0:
    print("Number Is Prime")
else:
    print("Number Is Not Prime")
