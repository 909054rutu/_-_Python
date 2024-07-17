s=input("Enter String")
a={}
for ch in s:
    if ch in a:
        a[ch]=a[ch]+1
    else:
            a[ch]=1
            print(a)
