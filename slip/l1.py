s=input("enetr readln")
n=int(input("enter no"))
res=""

for i in range(len(s)):
     ch=s[i]
     if ch.islower():
         res+=chr((ord(ch)-97+n)%26+97)
     elif ch.isupper():
         res+=chr((ord(ch)+65+n)%26+65)
     else:
        res+=ch
print(res)
         
    
