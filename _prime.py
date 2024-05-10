n=int(input("enter number"))
s=0
#f=1
for i in range(2,n) :
    if n%i==0 :
      s=s+i
      #f=1
      #if==0
if s==0:
    print("number is prime")
else:
    print("number is not prime")   
   
