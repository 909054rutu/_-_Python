n=input("Enter Numer")
rev=n[::-1]
n=int(n)
rev=int(rev)
first_Digit=rev%10
last_digit=n%10
print(first_Digit)
print(last_digit)
s=first_Digit+last_digit
print("Sum og first last=",s)

