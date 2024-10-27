#Write a Python function that accepts a string and calculate the number of upper case
#letters and lower case letters.

s=input("enter string")
lcnt=0
ucnt=0
for i in range(len(s)):
    ch=s[i]
    if ch.isupper():
        lcnt+=1
    if ch.islower():
        ucnt+=1
print(lcnt)
print(ucnt)
    
